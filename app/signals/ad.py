from blinker import Namespace


from app.libs.log import APP_LOGGER
from app.logic.ad import push_ad_info



ns_signals = Namespace()
sig_ad_status_change = ns_signals.signal('ad_status_change')


@sig_ad_status_change.connect
def on_ad_status_change(sender, ad, exstatus = 0, admin = None, **kwargs):
    # 这里面是订单状态发生改变后需要实现的业务逻辑
    ret = push_ad_info(ad, exstatus, admin)
    if ret:
        APP_LOGGER.info('推送广告状态变化消息成功')

