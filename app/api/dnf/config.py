from . import dnf_bp
import json
from app.libs.http_utils import *
from app.models import TUser, TUserConfig


# 获取定义
@dnf_bp.route('/config/defines', methods=['GET'])
def defines():
    data = {
	"role_name_type": "小写字母和数字;简体中文汉字;简体中文和字母;简体中文和数字",
	"risk_group_type": "小写字母和数字;简体中文汉字;简体中文和字母;简体中文和数字",
	"first_role": "枪剑士(男);圣职者(女);魔枪士(男);鬼剑士(男);鬼剑士(女);神枪手(男);神枪手(女);魔法师(男);魔法师(女);守护者(女);格斗家(男);格斗家(女);圣职者(男);暗夜使者(男);黑暗武士(男);缔造者(女)",
	"second_role": "不创建角色;枪剑士(男);圣职者(女);魔枪士(男);鬼剑士(男);鬼剑士(女);神枪手(男);神枪手(女);魔法师(男);魔法师(女);守护者(女);格斗家(男);格斗家(女);圣职者(男);暗夜使者(男);黑暗武士(男);缔造者(女)",
	"profession": [{
			"name": "不创建角色",
			"profession": []
		},
		{
			"name": "枪剑士(男)",
			"profession": [
				"暗刃",
				"特工",
				"战线佣兵",
				"源能专家"
			]
		},
		{
			"name": "圣职者(女)",
			"profession": [
				"圣骑士",
				"异端审判者",
				"巫女",
				"诱魔者"
			]
		},
		{
			"name": "魔枪士(男)",
			"profession": [
				"征战者",
				"决战者",
				"狩猎者",
				"暗枪士"
			]
		},
		{
			"name": "鬼剑士(男)",
			"profession": [
				"剑魂",
				"鬼泣",
				"狂战士",
				"阿修罗"
			]
		},
		{
			"name": "鬼剑士(女)",
			"profession": [
				"驭剑士",
				"暗殿骑士",
				"契魔者",
				"流浪武士"
			]
		},
		{
			"name": "神枪手(男)",
			"profession": [
				"漫游枪手",
				"枪炮师",
				"机械师",
				"弹药专家"
			]
		},
		{
			"name": "神枪手(女)",
			"profession": [
				"漫游枪手",
				"枪炮师",
				"机械师",
				"弹药专家"
			]
		},
		{
			"name": "魔法师(男)",
			"profession": [
				"元素爆破师",
				"冰结师",
				"血法师",
				"逐风者",
				"次元行者"
			]
		},
		{
			"name": "魔法师(女)",
			"profession": [
				"元素师",
				"召唤师",
				"战斗法师",
				"魔道学者"
			]
		},
		{
			"name": "守护者(女)",
			"profession": [
				"精灵骑士",
				"混沌魔灵",
				"帕拉丁",
				"龙骑士"
			]
		},
		{
			"name": "格斗家(男)",
			"profession": [
				"气功师",
				"散打",
				"街霸",
				"柔道家"
			]
		},
		{
			"name": "格斗家(女)",
			"profession": [
				"气功师",
				"散打",
				"街霸",
				"柔道家"
			]
		},
		{
			"name": "圣职者(男)",
			"profession": [
				"圣骑士",
				"蓝拳圣使",
				"驱魔师",
				"复仇者"
			]
		},
		{
			"name": "暗夜使者(男)",
			"profession": [
				"刺客",
				"死灵术士",
				"忍者",
				"影舞者"
			]
		},
		{
			"name": "黑暗武士(男)",
			"profession": [
				"自我觉醒"
			]
		},
		{
			"name": "缔造者(女)",
			"profession": [
				"自我觉醒"
			]
		}
	],
	"profession_position": [
	{
			"name": "枪剑士(男)",
			"positionX": 349,
			"positionY": 699
	},
	{
			"name": "圣职者(女)",
			"positionX": 464,
			"positionY": 699
	},
	{
			"name": "魔枪士(男)",
			"positionX": 579,
			"positionY": 699
	},
	{
			"name": "鬼剑士(男)",
			"positionX": 694,
			"positionY": 699
	},
	{
			"name": "鬼剑士(女)",
			"positionX": 809,
			"positionY": 699
	},
	{
			"name": "神枪手(男)",
			"positionX": 924,
			"positionY": 699
	},
	{
			"name": "神枪手(女)",
			"positionX": 1039,
			"positionY": 699
	},
	{
			"name": "魔法师(男)",
			"positionX": 1154,
			"positionY": 699
	},
	{
			"name": "魔法师(女)",
			"positionX": 349,
			"positionY": 800
	},
	{
			"name": "守护者(女)",
			"positionX": 464,
			"positionY": 800
	},
	{
			"name": "格斗家(男)",
			"positionX": 579,
			"positionY": 800
	},
	{
			"name": "格斗家(女)",
			"positionX": 694,
			"positionY": 800
	},
	{
			"name": "圣职者(男)",
			"positionX": 809,
			"positionY": 800
	},
	{
			"name": "暗夜使者(男)",
			"positionX": 924,
			"positionY": 800
	},
	{
			"name": "黑暗武士(男)",
			"positionX": 1039,
			"positionY": 800
	},
	{
			"name": "缔造者(女)",
			"positionX": 1154,
			"positionY": 800
	}
	],
	"area":
	[
		{
		"name":"广东区",
		"group": "Telecom",
		"index": 0,
		"server":
		[
			"广东1区",
			"广东2区",
			"广东3区",
			"广州1/2区",
			"广东4区",
			"广东5区",
			"广东6区",
			"广东7区",
			"广东8区",
			"广东9区",
			"广东10区",
			"广东11区",
			"广东12区",
			"广东13区"
		]
		},
		{
		"name":"西北区",
		"group": "Telecom",
		"index": 1,
		"server":
		[
			"西北1区",
			"西北2/3区"
		]
		},
		{
		"name":"江西区",
		"group": "Telecom",
		"index": 2,
		"server":
		[
			"江西1区",
			"江西2区",
			"江西3区"
		]
		},
		{
		"name":"广西区",
		"group": "Telecom",
		"index": 3,
		"server":
		[
			"广西1区",
			"广西2/4区",
			"广西3区",
			"广西5区"
		]
		},
		{
		"name":"西南区",
		"group": "Telecom",
		"index": 4,
		"server":
		[
			"西南1区",
			"西南2区",
			"西南3区"
		]
		},
		{
		"name":"湖南区",
		"group": "Telecom",
		"index": 5,
		"server":
		[
			"湖南1区",
			"湖南2区",
			"湖南3区",
			"湖南4区",
			"湖南5区",
			"湖南6区",
			"湖南7区"
		]
		},
		{
		"name":"陕西区",
		"group": "Telecom",
		"index": 6,
		"server":
		[
			"陕西1区",
			"陕西2/3区"
		]
		},
		{
		"name":"湖北区",
		"group": "Telecom",
		"index": 7,
		"server":
		[
			"湖北1区",
			"湖北2区",
			"湖北3区",
			"湖北4区",
			"湖北5区",
			"湖北6区",
			"湖北7区",
			"湖北8区"
		]
		},
		{
		"name":"云贵区",
		"group": "Telecom",
		"index": 8,
		"server":
		[
			"云南1区",
			"贵州1区",
			"云贵1区"
		]
		},
		{
		"name":"上海区",
		"group": "Telecom",
		"index": 9,
		"server":
		[
			"上海1区",
			"上海2区",
			"上海3区",
			"上海4/5区"
		]
		},
		{
		"name":"四川区",
		"group": "Telecom",
		"index": 10,
		"server":
		[
			"四川1区",
			"四川2区",
			"四川3区",
			"四川4区",
			"四川5区",
			"四川6区"
		]
		},
		{
		"name":"江苏区",
		"group": "Telecom",
		"index": 11,
		"server":
		[
			"江苏1区",
			"江苏2区",
			"江苏3区",
			"江苏4区",
			"江苏5/7区",
			"江苏6区",
			"江苏8区"
		]
		},
		{
		"name":"重庆区",
		"group": "Telecom",
		"index": 12,
		"server":
		[
			"重庆1区",
			"重庆2区"
		]
		},
		{
		"name":"浙江区",
		"group": "Telecom",
		"index": 13,
		"server":
		[
			"浙江1区",
			"浙江2区",
			"浙江3区",
			"浙江4/5区",
			"浙江6区",
			"浙江7区"
		]
		},
		{
		"name":"新疆区",
		"group": "Telecom",
		"index": 14,
		"server":
		[
			"新疆1区"
		]
		},
		{
		"name":"安徽区",
		"group": "Telecom",
		"index": 15,
		"server":
		[
			"安徽1区",
			"安徽2区",
			"安徽3区"
		]
		},
		{
		"name":"福建区",
		"group": "Telecom",
		"index": 16,
		"server":
		[
			"福建1区",
			"福建2区",
			"福建3/4区"
		]
		},
		{
		"name":"东北区",
		"group": "Unicom",
		"index": 0,
		"server":
		[
			"东北1区",
			"东北2区",
			"东北3/7区",
			"东北4/5/6区"
		]
		},
		{
		"name":"北京区",
		"group": "Unicom",
		"index": 1,
		"server":
		[
			"北京1区",
			"北京2/4区",
			"北京3区"
		]
		},
		{
		"name":"天津区",
		"group": "Unicom",
		"index": 2,
		"server":
		[
			"天津1区"
		]
		},
		{
		"name":"内蒙古区",
		"group": "Unicom",
		"index": 3,
		"server":
		[
			"内蒙古1区"
		]
		},
		{
		"name":"辽宁区",
		"group": "Unicom",
		"index": 4,
		"server":
		[
			"辽宁1区",
			"辽宁2区",
			"辽宁3区"
		]
		},
		{
		"name":"吉林区",
		"group": "Unicom",
		"index": 5,
		"server":
		[
			"吉林1/2区"
		]
		},
		{
		"name":"黑龙江区",
		"group": "Unicom",
		"index": 6,
		"server":
		[
			"黑龙江1区",
			"黑龙江2/3区"
		]
		},
		{
		"name":"河南区",
		"group": "Unicom",
		"index": 7,
		"server":
		[
			"河南1区",
			"河南2区",
			"河南3区",
			"河南4区",
			"河南5区",
			"河南6区",
			"河南7区"
		]
		},
		{
		"name":"华北区",
		"group": "Unicom",
		"index": 8,
		"server":
		[
			"华北1区",
			"华北2区",
			"华北3区",
			"华北4区"
		]
		},
		{
		"name":"山东区",
		"group": "Unicom",
		"index": 9,
		"server":
		[
			"山东1区",
			"山东2/7区",
			"山东3区",
			"山东4区",
			"山东5区",
			"山东6区"
		]
		},
		{
		"name":"河北区",
		"group": "Unicom",
		"index": 10,
		"server":
		[
			"河北1区",
			"河北2/3区",
			"河北4区",
			"河北5区"
		]
		},
		{
		"name":"山西区",
		"group": "Unicom",
		"index": 11,
		"server":
		[
			"山西1区",
			"山西2区"
		]
		}
	]

    }
    return render_ok(data)

@dnf_bp.route('/config/user', methods=['POST'])
def post_config_user():
	mac = request.headers.get('mac')
	config = get_json_arg('config')
	user = TUser.query.filter(TUser.mac == mac).first()
	if not user:
		return render_ok()

	config_info = TUserConfig.query.filter(TUserConfig.user_id == user.id).first()
	if config_info:
		config_info.config = config
		config_info.save()
	else:
		userconfig = TUserConfig()
		userconfig.user_id = user.id
		userconfig.config = config
		userconfig.save()

	return render_ok()


@dnf_bp.route('/config/user', methods=['GET'])
def get_config_user():
	mac = request.headers.get('mac')
	user = TUser.query.filter(TUser.mac == mac).first()
	if not user:
		return render_ok()

	config_info = TUserConfig.query.filter(TUserConfig.user_id == user.id).first()
	data ={}
	if config_info:
		data ['config'] = config_info.config

	return render_ok(data)


