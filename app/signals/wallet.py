from blinker import Namespace

from app.models import TWallet, TAdCard
from app.logic.user import push_user_wallet
from app.logic.ad import ad_min_order_amount
from app.libs.defines import AdType, AdStatus,AdExtraStatus
from app.libs.log import APP_LOGGER
from app.signals.ad import sig_ad_status_change

ns_signals = Namespace()
sig_wallet_change = ns_signals.signal('wallet_change')
sig_wallet_change_user = ns_signals.signal('wallet_change_user')


@sig_wallet_change.connect
def on_wallet_change(sender, order, **kwargs):
    dealer_wallet = TWallet.get_by_userid(order.userid)
    owner_wallet = TWallet.get_by_userid(order.ad_owner_userid)

    push_user_wallet(dealer_wallet)
    push_user_wallet(owner_wallet)

    check_ad_buy(dealer_wallet)
    check_ad_buy(owner_wallet)


@sig_wallet_change_user.connect
def on_wallet_change_user(sender, wallet, **kwargs):
    push_user_wallet(wallet)
    check_ad_buy(wallet)


def check_ad_buy(wallet):
    userid = wallet.userid
    ads = TAdCard.query.filter(TAdCard.userid == userid, TAdCard.ad_type == AdType.BUY.value,
                               TAdCard.status == AdStatus.ONLINE.value).all()
    for ad in ads:
        min_amount = ad_min_order_amount(ad)
        if min_amount is None:
            APP_LOGGER.error('计算广告：{}的最小订单额度失败'.format(ad.id))
            continue

        if wallet.amount < min_amount:
            ad.status = AdStatus.PAUSE.value
            ad.save()
            sig_ad_status_change.send(ad=ad, exstatus=AdExtraStatus.LOWBALANCE.value)
            APP_LOGGER.info('用户：{}余额不足，暂停广告：{}'.format(userid, ad.id))
