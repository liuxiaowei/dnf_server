from blinker import Namespace

from app.models import TAdCard
from app.libs.defines import OrderStatus, AdStatus, OrderType
from app.libs.log import APP_LOGGER
from app.logic.order import push_order_info
from app.logic.ad import ad_has_stock, push_ad_info
from app.libs.defines import AdExtraStatus


ns_signals = Namespace()
sig_order_status_change = ns_signals.signal('order_status_change')


def check_stock_on_creation(order):
    if ad_has_stock(order.ad_id):
        return

    ad = TAdCard.get_by_id(order.ad_id)
    if ad.status == AdStatus.ONLINE.value:
        ad.status = AdStatus.PAUSE.value
        ad.save()
        push_ad_info(ad=ad, exstatus = AdExtraStatus.SOLDOUT.value)


@sig_order_status_change.connect
def on_order_status_change(sender, order, userid, auto=False, exstatus = 0, admin = None, **kwargs):
    # 这里面是订单状态发生改变后需要实现的业务逻辑
    ret = push_order_info(order, userid, auto, exstatus, admin)
    if ret:
        APP_LOGGER.info('推送订单状态变化消息成功')

    if order.order_type == OrderType.BUY.value:
        if order.status == OrderStatus.PROTECTION.value:
            check_stock_on_creation(order)
