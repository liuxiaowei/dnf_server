from enum import Enum


class UserErrorCode(Enum):
    G2FA_NEED = 1000 # 需要进行google验证
    G2FA_FAIL = 1001 # Google验证失败
    GENERATE_CAPTCHA_FAILED = 1002#生成验证码失败
    CAPTCHA_ERROR = 1003#图形验证码错误
    USER_NOT_EXIST = 1004#用户不存在
    PASSWORD_VERIFY_FAILED = 1005#用户名或密码错误
    USER_DENY_LOGIN = 1006#尊敬的客户，很抱歉您的账号已被封号，如需恢复，请及时联系客服400XX
    QUERY_USER_INFO_FAILED = 1007#查询用户信息不存在
    EMAIL_USED = 1008#邮箱已被注册
    NICKNAME_USED = 1009#用户名已被注册
    WRONG_CAPTCHA = 1010#验证码错误
    WRONG_INVITE_CODE = 1011#邀请码错误
    INVITE_CODE_EXPIRED = 1012#邀请码已过期
    INVITE_CODE_USED = 1013#邀请码已被使用
    INVALID_INVITE_CODE = 1014#邀请码无效
    TRAN_TERM_NOT_EDITABLE = 1015#不允许更改交易条款
    TRAN_TERM_NOT_DELETEABLE = 1016#不允许删除交易条款
    ALIPAY_CODE_USED = 1017#支付宝账号已被使用
    PAYMENT_ACCOUNT_BINDED = 1018#支付账号已被绑定
    PAYMENT_METHOD_PENDING = 1019#支付方式待审核，无法更改
    PAYMENT_METHOD_REACH_MAX = 1020#只能创建十条支付方式
    USER_AUTH_BINDED = 1021#用户认证已被绑定
    WRONG_PASSWORD = 1022#密码错误
    PHONE_NUMBER_USED = 1023#手机号码已被使用
    WRONG_PHONE_CAPTCHA = 1024#手机验证码错误
    INVITE_TOKEN = 1025#token已失效
    GOOGLE_OTP_NOT_BINDED = 1026#用户未绑定谷歌验证码
    EMAIL_NOT_REGISTERED = 1027#邮箱未被注册
    SEND_EMAIL_FAILED = 1028#发送邮件失败
    SEND_SMS_FAILED = 1029#发送短信验证码失败
    GOOGLE_OTP_INPUT = 1030#请输入谷歌验证码
    INVALID_PAYMENT_METHOD = 1031#无效的付款方式
    WITHDRAW_FEE_NOT_CONFIG = 1032#提现手续费尚未配置
    CAPTCHA_EXPIRED = 1033#验证码已过期
    IDCARD_BINDED = 1034 #身份证已被他人绑定
    G2FA_NOT_GENERATE = 1035 #用户未生成Google验证码
    WITHDRAW_FEE_BEYOND_LIMIT = 1036 #提现超出最大金额

class CommonErrorCode(Enum):
    PERMISSION_DENY = 2000#权限不足
    MISSING_PARAMETER = 2001#参数缺失
    FILE_NAME_NULL = 2002#文件名为空
    WRONG_PARAMETER = 2003#参数错误
    OPEN_FILE_ERROR = 2004#打开文件失败
    NO_EXCLE_SHEET = 2005#Excel 没有sheet
    NO_EXCLE_ROW = 2006#Excel 文件是空的
    WRONG_EXCLE_FORMAT = 2007#错误的Excel格式
    UNSUPPORT_BANK = 2008#不支持的银行
    NO_HEADERS = 2009#缺少请求头{}
    INVALID_HEADERS = 2010#请求头: {}无效
    NO_USER = 2011#无此用户
    NO_TOKEN = 2012#token查询失败
    VERIFY_USER_FAILED = 2013#用户验证失败
    NO_CONFIG = 2014#未配置
    MISSING_HTTP_PARAMS = 2015#http参数缺失{}
    CONVERSION_PARAMS_FAILED = 2016#转换参数:{}失败
    PARAM_ILLEGAL = 2017#参数:{}不合法
    WRONG_DATA_FORMAT = 2018#请求数据格式错误
    NOT_SUPPORT_CHECK = 2019#不支持自动检测的卡类型
    CHECK_NOT_COMPLETE = 2020#自动检测尚未完成


class AdErrorCode(Enum):
    AD_DATA_CHANGE = 3000#广告数据已变化，请刷新页面重新下单
    INVALID_CARD_DATA = 3001#无卡片信息
    FORBIDEN_TO_AD = 3002#禁止发布广告
    INVALID_CARD_TYPE = 3003#无效的卡类型
    AD_EXCEEDS_THE_LIMIT = 3004#广告数量超过限制
    INVALID_TRAN_TERM = 3005#无效的交易条款
    INVALID_AD = 3006#无效的广告
    INVALID_CARD_INFO = 3007#卡片信息不存在
    INVALID_CONDITION = 3008#未指定面额
    AD_OFFLINE = 3009#广告已下线
    WRONG_STATUS = 3010#广告状态错误
    ONLINE_FAILED = 3011#恢复失败，并发订单数达到限制
    ONLINE_FAILED_LOW_BALANCE = 3012#恢复失败，余额不足
    ONLINE_FAILED_LOW_STOCK = 3013#恢复失败，库存不足
    CARD_TYPE_NOT_MODIFIED = 3014#卡类型不可修改
    REACH_FLUID_LIMIT = 3015 # 广告已达到流动性
    QUERY_NOT_COMPLETE = 3016 # 卡未完全检测，不可发布广告
    AD_CAN_NOT_BE_PUBLISHED = 3017 #您的广告包含无效卡，不能发布
    AREA_TYPE_NOT_MODIFIED = 3018 #地区类型不可修改
    FORBIDEN_PUBLISH = 3019 # 平台休整期间暂时仅支持账户提现业务


class OrderErrorCode(Enum):
    PERMISSION_DENY_TO_APPEAL = 4000 #无权发起申诉
    ORDER_OWNER_YOURSELF = 4001#不能对自己的广告下单
    ORDER_COUNT_LIMIT = 4002#一个广告不能超过{}笔订单
    ORDER_REACH_THE_LIMIT = 4003#并发订单数达到限制
    LACK_OF_STOCK = 4004#面额：{}库存不足
    WRONG_MULTIPLE = 4005#倍数不正确
    NUMBER_OF_DENOMINATION_WRONG = 4006#额度：{}的数量不满足要求
    WRONG_DENOMINATION = 4007#额度不正确
    ORDER_NOT_EXIST = 4008#订单不存在
    PERMISSION_DENY_TO_RELEASE = 4009 #无权限释放订单
    WRONG_ORDER_STATUS = 4010 #订单状态错误
    WRONG_ORDER_DETAIL = 4011 #订单信息不正确,请重新提交
    WRONG_SHIP_COUNT = 4012 #发卡数量不正确，请重新提交
    CHECK_FAILED = 4013 #查收失败
    PERMISSION_DENY_TO_CANCEL = 4014 #无权限取消订单
    PERMISSION_DENY = 4015 #无权限查看订单
    PERMISSION_DENY_TO_OPERATE = 4016 #无操作订单的权限
    DISSATISFY_ORDER_LIMIT = 4017 # 不满足广告的最小最大金额限制
    ORDER_CAN_NOT_BE_PUBLISHED = 4018 # 您的订单包含无效卡，无法发卡
    REPEAT_RATE_ORDER = 4019 #不能重复评价订单


class WalletErrorCode(Enum):
    NO_WALLET_DATA = 5000#钱包数据不存在
    BALANCE_NOT_ENOUGH = 5001#余额不足
    BUYER_BALANCE_NOT_ENOUGH = 5002#买家余额不足


class TradeAccountErrorCode(Enum):
    EXIST_ACCOUNT = 6000#账号已存在
    ACCOUNT_CANNOT_EDIT = 6001#账号暂不能修改
    ACCOUNT_NOT_EXIST = 6002#账号不存在
    ACCOUNT_CANNOT_DELETE = 6003#账号暂不能删除
