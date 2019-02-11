from enum import Enum


class AdType(Enum):
    BUY = 1
    SELL = 2


class AdStatus(Enum):
    ONLINE = 1 # 正常
    PAUSE = 2 # 暂停
    OFFLINE = 4 # 下线
    DELETED = 5 # 逻辑删除

#广告额外状态
class AdExtraStatus(Enum):
    NONE = 0 #无
    SOLDOUT = 1  # 卖完了
    LOWBALANCE = 2  # 余额不足
    REACHTOPLIMIT = 3  # 同时处理数达到上限
    REACH_FLUID = 4 # 达到流动性限制
    NEW_AD = 5 # 新广告

#图片审核状态
class PictureAuditsStatus(Enum):
    PENDING = 1# 待审核
    DENY = 2 # 不通过
    ALLOW = 3 # 已通过

#处理订单申诉
class OrderAppealAction(Enum):
    APPEAL = 1#申诉
    CLAIM = 2#客服认领
    INTERVENTION = 3#客服介入
    CANCELCLAIM = 4#客服取消认领
    TRANSFRE = 5#客服转交申述
    APPEAL_DONE = 6#客服处理完成订单
    APPEAL_CANCEL = 7#客服处理取消订单
    REAPPEAL = 8#重新发起申述
    REMARK = 9#增加备注

#订单额外状态
class OrderExtraStatus(Enum):
    NONE = 0 #无
    GUARANTEE_TIMEOUT = 1  #保障时间超时,自动释放
    CHECK_TIMEOUT = 2  #查收时间超时，自动取消
    SEND_TIMEOUT = 3  #发卡时间超时，自动取消
    FIVE_MIN_TO_LIMIT = 4  #还有五分钟超保障时间
    FIFTEEN_MIN_TO_LIMIT = 5  #还有十五分钟超保障时间


class CardStatus(Enum):
    UNUSED = 0 # 未使用
    BOOKED = 1 # 已预订
    USED = 2 # 已使用
    INVALID = 3 # 无效


class OrderType(Enum):
    BUY = 1
    SELL = 2


class OrderStatus(Enum):
    OPENED = 1 # 打开
    WAIT_CHECK = 2 # 等待查收
    PROTECTION = 3 # 保障中
    APPEAL = 4 # 申述中
    DONE = 5 # 已完成
    CANCEL = 6 # 已取消
    CHECK_TIMEOUT = 7 # 查收超时


class OrderQueryStatus(Enum):
    QUERYING = 1 # 查询中(只有支持自动检测的卡才有这个状态)
    QUERY_TIMEOUT = 2#查询超时
    QUERY_END = 3#查询结束


class TransTermStatus(Enum):
    DENY = 1 # 未通过
    PENDING = 2 # 审核中
    ALLOW = 3 # 已通过
    DELETED = 4 # 已删除（逻辑删除）


class UserAuthType(Enum):
    REALNAME = 1
    VIDEO = 2


class UserAuthStatus(Enum):
    INIT = 1 # 未认证
    PENDING = 2 # 认证中
    DENY = 3 # 未通过
    ALLOW = 4 # 已通过


class UserPaymentMethodStatus(Enum):
    INIT = 1  # 未认证
    PENDING = 2  # 认证中
    DENY = 3  # 未通过
    ALLOW = 4  # 已通过


class VerifyCodeScene(Enum):
    REGISTER = 1 # 注册


class GoodsType(Enum):
    ACCOUNT = 1 # 账号
    CARD = 2 # 礼品卡
    CHARGE = 3#自动充值交易


class UserStatus(Enum):
    VALID = 1 # 正常
    BLOCK = 2 # 封号

class UserPubAdStatus(Enum):
    VALID = 1  # 正常
    BLOCK = 2  # 封号

class InfoStatus(Enum):
    INIT = 1 # 未发布
    PENDNG = 2 # 待发布
    PUBLISHED = 3 # 已发布
    WITHDRAW = 4 # 撤回


class InviteCodeStatus(Enum):
    UNUSED = 1 # 未使用
    USED = 2 # 已使用
    EXPIRED = 3 # 已过期
    NOT_VALID = 4 # 未生效


class ShortcutWordStatus(Enum):
    DRAFT = 1 # 草稿
    OFFLINE = 2 # 已下线
    ONLINE = 3 # 已上线


class CardTypeStatus(Enum):
    DRAFT = 1 # 草稿
    OFFLINE = 2 # 已下线
    ONLINE = 3 # 已上线
    DELETED = 4 # 已删除


class AreaTypeStatus(Enum):
    DRAFT = 1 # 草稿
    OFFLINE = 2 # 已下线
    ONLINE = 3 # 已上线
    DELETED = 4 # 已删除


class AccountTypeStatus(Enum):
    DRAFT = 1 # 草稿
    OFFLINE = 2 # 已下线
    ONLINE = 3 # 已上线
    DELETED = 4 # 已删除


class ItunesQuestionStatus(Enum):
    DRAFT = 1 # 草稿
    OFFLINE = 2 # 已下线
    ONLINE = 3 # 已上线
    DELETED = 4 # 已删除


class ItunesTypeStatus(Enum):
    DRAFT = 1 # 草稿
    OFFLINE = 2 # 已下线
    ONLINE = 3 # 已上线
    DELETED = 4 # 已删除

class PaidType(Enum):
    SITE_TRANSFER = 'site'
    WXPAY = 'wechat'
    ALIPAY = 'alipay'
    BANK = 'bank'

class TransactionTradeType(Enum):
    TRADE = 1
    RECHARGE = 2
    WITHDRAW = 3
    ITUNES = 4

class TransactionStatus(Enum):
    INIT = 1 # 待提交
    PENDING = 2  # 待审核
    DENY = 3  # 未通过
    ALLOW = 4  # 已通过

class WithdrawStatus(Enum):
    INIT = 1
    PENDING = 2  # 待审核
    DENY = 3  # 未通过
    ALLOW = 4  # 已通过


class RechargeStatus(Enum):
    INIT = 1
    PENDING = 2  # 待审核
    DENY = 3  # 未通过
    ALLOW = 4  # 已通过

class AppealStatus(Enum):
    INIT = 1 # 待认领
    PENDING = 2 # 待处理
    DONE = 3 # 已处理

class BasicConfig(Enum):
    ITUNES_FEE = 1
    GIFT_FEE = 2
    WITHDRAW_BANK_FEE = 3
    WITHDRAW_ALIPAY_FEE = 4
    ITUNES_ACCOUNT_MAX = 5
    ITUNES_DOC = 6
    ITUNES_UNIT_PRICE = 7
    GUARANTEE_TIME = 8
    RECHARGE_TIME = 9
    TRADE_REALNAME= 10

class UserOpsAction(Enum):
    BLOCK_LOGIN = 1
    UNBLOCK_LOGIN = 2
    CREATE_USER = 3
    UNBIND_G2FA = 4
    UPDATE_PASSWORD = 5
    BLOCK_AD = 6
    UNBLOCK_AD = 7
    REAL_NAME_AUTH_DENY = 8
    REAL_NAME_AUTH_ALLOW = 9
    VIDEO_NAME_AUTH_DENY = 10
    VIDEO_NAME_AUTH_ALLOW = 11

    @classmethod
    def action_str(cls, action):
        m = {
            cls.BLOCK_LOGIN.value: '封号',
            cls.UNBLOCK_LOGIN.value: '解封',
            cls.CREATE_USER.value: '新增账户',
            cls.UNBIND_G2FA.value: '解绑谷歌验证',
            cls.UPDATE_PASSWORD.value: '修改登录密码',
            cls.BLOCK_AD.value: '禁止发布广告',
            cls.UNBLOCK_AD.value: '解除禁止发布广告',
            cls.REAL_NAME_AUTH_DENY.value: '实名认证不通过',
            cls.REAL_NAME_AUTH_ALLOW.value: '实名认证通过',
            cls.VIDEO_NAME_AUTH_DENY.value: '视频认证不通过',
            cls.VIDEO_NAME_AUTH_ALLOW.value: '视频认证通过',
        }
        return m.get(action, '未知操作')


class BannerStatus(Enum):
    INIT = 1
    ONLINE = 2
    OFFLINE = 3


class CardQueryStatus(Enum):
    INIT = 1#未查询
    QUERYING = 2#正在查询
    QUERY_SUCCESS = 3#查询成功
    QUERY_FAILED = 4#查询失败,无效卡
    QUERY_USED = 5#已使用
    MONEY_NOT_MATCH = 6#面额不匹配


class PunishedStatus(Enum):
    UNPUNISHED = 1#未惩罚
    ADCANCLE = 2#取消
    ADBLOCK = 3#禁止发布广告
    ACCOUNTBLOCK =4#封号


class AuditsType(Enum):
    AD = 1#广告
    ORDER = 2#订单


class AuditsAdType(Enum):
    ACCOUNT = 1#账号交易
    CARD = 2#礼品卡交易
    CHARGE = 3#自动充值交易


class OrderAdType(Enum):
    ACCOUNT = 1#账号交易
    CARD = 2#礼品卡交易
    CHARGE = 3#自动充值交易


class OrderDeadlineFreeze(Enum):
    UNFREEZING = 1#未冻结
    FREEZING = 2#冻结中


class CardAreaStatus(Enum):
    NORMAL = 1#正常
    DELETED = 2#已删除


class AccountStatus(Enum):
    NORMAL = 1#正常，未处理
    CHECKING = 2#检测中
    CHECK_FAILED = 3#检测失败
    SALE_CHECKING = 4#销售检测中
    ON_SALE = 5#出售中
    OFF_SALE = 6#暂停出售
    SELF_CHARGING = 7#正在自充
    AD_CHARGING = 8#正在广告充值中
    CHARGING_PAUSE = 9#暂停充值中
    DELETED = 10#已删除


# class AccountRechargeStatus(Enum):
#     INIT = 1#初始化
#     SELF_CHARGING = 2#正在自充
#     AD_CHARGING = 3#正在广告充值中
#     CHARGING_PAUSE = 4#暂停充值中
#     CHARGING_CANCEL = 5#取消充值中


class ConfigAccountTypeStatus(Enum):
    NORMAL = 1#正常
    DELETED = 2#已删除


class HadTradeStatus(Enum):
    NOT_TRADE = 1#未交易过
    HAD_TRADE = 2#交易过


class FlagStatus(Enum):
    OFF = 1#开关关闭
    ON = 2#开关开启


class YesOrNo(Enum):
    NO = 1
    YES = 2

class ItunesQueryStatus(Enum):
    INIT = 1#未查询
    QUERYING = 2#正在查询
    QUERY_SUCCESS = 3#查询成功
    QUERY_FAILED = 4#查询失败

class ItunesRechargeStatus(Enum):
    INIT = 1#未查询
    RECHARGING = 2#正在充值
    RECHARGE_SUCCESS = 3#充值成功
    RECHARGE_FAILED = 4#充值失败