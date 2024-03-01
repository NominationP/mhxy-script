fuzzy_match = {
    "价格较高请自行购买": ["价偬愆高~自贸"],
    "师门任务完成": ["师门任务完咸", "师门任务完屐"],
    "龙王之怒": ["龙壬之怒"],
}


def fuzzy_match_def(text_to_check):
    # Iterate through the dictionary
    for key, values in fuzzy_match.items():
        if any(text_to_check == value for value in values):
            print(f"The text '{text_to_check}' is contained in the value of key '{key}'")
            return key
    else:
        # print(f"No match found for the text '{text_to_check}' in any values.")
        return None


custom_operate = {
    "价格较高请自行购买": ["购买"],
    "师门任务完成": ["师门任务完成确认", "退出师门任务界面"],
    "听听无妨": [700]
}

anchors_time = {
    "被撞破的妖魔": 30,
    "决裂": 20,
    "逼问妖魔下落": 30,
    "击败恶虎寅将军": 30,
    "击败恶龙": 20,
    "琉璃生性羞怯": 20,
    "利刃相迎": 30,
    "心性试炼": 20,
    "搅海弄云": 10,
    "天兵捉拿天蓬": 20,
    "地府相会": 20,
    "绿烟仙子现身": 10,
    "康太尉诬陷天蓬调戏嫦": 10,
    "再战阎罗王": 10,
    "老龙王的愤怒": 10
}

# 先检查有没有,再去点击, 目前只用于跑镖
anchors_check_then = [
    "押送普通镖银",
    "押送高级镖银(有难度",
]


# def remove_certain_anchors_time(key_to_remove):
#     # Check if the key exists before removal
#     if key_to_remove in anchors_time:
#         del anchors_time[key_to_remove]
#         print(f"'{key_to_remove}' removed from the dictionary.")
#     else:
#         print(f"'{key_to_remove}' not found in the dictionary.")


def remove_certain_value(value_to_remove):
    # Iterate through the list and remove the specified value
    for item in anchors:
        _, value_list = item  # Unpack the tuple to access the list
        if value_to_remove in value_list:
            value_list.remove(value_to_remove)


anchors = [
    # 师门任务
    # (10099, ["日常-师门任务", "日常-师门赐教","日常-师门历练", "师门-修习试炼", "师门-扬名立万", "去完成", "价格较高请自行购买"]),

    # 宝图任务
    (10088, ["听听无妨", "日常-宝图任务"]),

    (2, ["跳过剧情动画", "跳过剧懵~画", "通关", "加为好友"]),
    (0, ["进入战斗", "迸入战斗", "日常-捉鬼", "曰常-捉鬼", "捉鬼任务", "白晓仙子"]),
    (1, ["噩梦浮现", "副本已完成", "副本己完咸"]),
    (3, ["选择副本"]),
    (4, ["果断出手", "陷入噩梦"]),  # 左下角 黄框
    (6, ["秘境降妖"]),

    # 二重影-侠士
    (10, ["与六耳切磋", "六耳大脑方寸山", "从菩提祖师手中救下六", ]),

    # 掏海去-普通
    (12, ["龙王之怒", "偷习秘法", "搅海弄云", "搅海舜云"]),

    # 琉璃碎-普通
    (14, ["琉璃生性羞怯", "卷帘的挣扎", "争执", ]),

    # 明珠还-普通
    (16, ["心性试炼", "天庭来拿", "天庭来r", "天庭来享", "火烧明珠", "天庭来辜", ]),

    # 明珠还-侠士
    (3, ["地府相会", "击败恶龙", "天命如何"]),

    # 绿烟如梦-侠士
    (18, ["不行 !", "好重的杀气"]),
    (19, ["打败康太尉", "打败魔化康太尉", "阻止嫦娥"]),

    # 桃花定情-侠士
    (20, ["不要被他蛊惑 !", "怎么又是你 !", "休得无礼", "小心", "小心 !"]),
    (21,
     ["打败九宫心魔", "意外遇到福陵老妖", "蕙外遇到褐陵老妖", "遇到拦路妖怪", "打败魔化福陵老妖", "打败赝化褐凌老妖",
      "打败厦化褐陵老妖"
      "战胜孟婆", "战胜孟窭"]),

    # 金蝉心-普通
    (23, ["同门相争", "回门相争", "清者自清", "金蝉之力", "金蝉2力"]),

    # 流沙净-普通
    (23, ["袭人妖怪", "少女不愿意嫁人", "少女不愿匮嫔人", "利刃相迎"]),

    (24, ["少侠已经捉完1轮鬼。是否继续捉鬼?"]),

    # 绿烟如梦-普通
    (23, ["绿烟仙子现身", "康太尉诬陷天蓬调戏嫦", "天兵捉拿天蓬", "天兵捉挛天莲"]),

    # 桃花定情-普通
    (23, ["打败鬼将", "打败鬼格", "打败孟婆", "帮助猪八戒", "打败福陵老妖", "打败褐陵老妖"]),

    # 琉璃碎-侠士
    (14, ["蛊惑失败", "蛊惑失效", "求而不得的过去", "打碎琉璃盏"]),

    # 流沙净-侠士
    (14, ["被撞破的妖魔", "决裂", "逼问妖魔下落", ]),

    # 流沙净-普通
    (14, ["击败恼人的猢狲们", "击败水帘洞灵", "六耳与石猴大打出手"]),

    # 流沙净-普通
    (14, ["师徒过招", "击败恶虎寅将军", "从虎寅将军手里救下小猴"]),

    # 蹈海去-侠士
    (14, ["挣脱梦赝", "挣脱梦魇", "攘除贼寇", "渔港境", ]),

    # 金蝉心-侠士
    (23, ["谈判失败", "五行禁地", "师徒之争"]),

    # 西行-侠士
    (23, ["自我证明", "大圣报恩", "心魔难解", "金蝉之力", "金蝉2力"]),

    # 踏西行-普通

    (23, ["灵力苏醒", "超度万鬼", "真魔假皇", "真赓假皇"]),

    # 方丈山-侠士
    (8, ["再战阎罗王", "老龙王的愤怒", "我命由我不由天"]),

]

# 点完这些字段,自动去下面固定坐标点击 {"快速应战"}
next_is_down = [
    "再战阎罗王", "老龙王的愤怒", "我命由我不由天",
    "灵力苏醒", "真魔假皇", "真赓假皇",
    "自我证明", "大圣报恩", "心魔难解",
    "五行禁地", "师徒之争", "谈判失败",
    "超度万鬼", "打败魔化福陵老妖", "打败赝化褐凌老妖",
    "打败九宫心魔", "打败康太尉", "绿烟仙子现身", "康太尉诬陷天蓬调戏嫦",
    "天兵捉拿天蓬", "天兵捉挛天莲", "打败鬼将", "打败孟婆", "帮助猪八戒", "打败福陵老妖", "打败褐陵老妖",
    "蛊惑失败", "求而不得的过去", "决裂", "逼问妖魔下落",
    "袭人妖怪", "少女不愿意嫁人", "少女不愿匮嫔人", "利刃相迎",
    "蛊惑失效", "龙王之怒", "偷习秘法", "搅海弄云", "搅海舜云",
    "同门相争", "回门相争", "清者自清", "金蝉之力", "金蝉2力", "心性试炼",
    "火烧明珠", "天庭来拿", "天庭来r", "天庭来享", "天庭来辜",
    "击败恼人的猢狲们", "击败水帘洞灵", "六耳与石猴大打出手", "打败鬼格",
    "与六耳切磋", "六耳大脑方寸山", "从菩提祖师手中救下六",
    "挣脱梦赝", "挣脱梦魇", "攘除贼寇", "渔港境",
    "地府相会", "击败恶龙", "天命如何",
    "琉璃生性羞怯",

]

# 点击完后去点击 '确定'
next_is_certain = [
    "押送普通镖银",
    "押送高级镖银(有难度",
]

certain_coordinate_windows = {
    "百晓仙子": [[560, 517], [646, 530]],
    "郑镖头": [[326, 579], [384, 588]],

    "店小二": [[962, 517], [1020, 534]],
    "钟馗": [[476, 564], [517, 579]],

    "侠士副本": [[513, 190], [686, 229]],
    "侠士1": [[411, 773], [573, 822]],
    "侠士2": [[767, 776], [933, 822]],
    "普通副本": [[300, 188], [472, 224]],
    "普通1": [[411, 773], [573, 822]],
    "普通2": [[767, 776], [933, 822]],
    "普通3": [[1124, 773], [1289, 821]],
    "选择副本": [[1195, 443], [1528, 488]],

    "活动": [[417, 77], [478, 129]],

    # 小地图
    "打开小地图": [[130, 69], [270, 142]],

    "队伍": [[1468, 201], [1591, 253]],
    "任务": [[1345, 201], [1465, 253]],
    "队伍头像": [[1307, 285], [1365, 346]],
    "离开队伍": [[1104, 387], [1244, 452]],
    "世界地图": [[17, 69], [92, 147]],
    "长安城": [[703, 538], [839, 602]],
    "东海湾": [[1206, 551], [1292, 614]],

    "押送普通镖银": [[1197, 527], [1534, 572]],
    "押送高级镖银(有难度": [[1190, 609], [1531, 656]],
    "云乐游": [[652, 542], [719, 559]],
    "云乐游秘境降妖": [[1197, 360], [1526, 405]],
    "瑶池仙镇进入": [[373, 826], [592, 867]],
    "继续挑战": [[1268, 795], [1339, 870]],
    "确定": [[855, 571], [1019, 618]],
    # 快捷点击
    "快速应战": [[1232, 608], [1484, 657]],
    "师门任务完成确认": [[683, 763], [923, 805]],
    "退出师门任务界面": [[1392, 228], [1412, 242]],
    "确认捉鬼": [[865, 554], [1016, 599]],

    # not remark

    "购买": [[625, 488], [725, 510]],

}


def get_certain_coordinate(text):
    return text, certain_coordinate_windows.get(text)


certain_coordinate_up = {
    # 小地图
    "侠士副本": [[265, 136], [362, 151]],
    "侠士1": [[209, 442], [300, 469]],
    "侠士2": [[405, 445], [500, 473]],
    "普通副本": [[265, 282], [297, 332]],
    "普通1": [[209, 442], [300, 469]],
    "普通2": [[405, 445], [500, 473]],
    "普通3": [[595, 446], [685, 473]],
    "选择副本": [[632, 300], [810, 325]],
    "确定": [[457, 341], [534, 362]],
    "活动": [[220, 45], [246, 82]],
    "购买": [[625, 488], [725, 510]],
    "师门任务完成确认": [[363, 441], [487, 466]],
    "退出师门任务界面": [[736, 155], [746, 164]],

    # 小地图

    "打开小地图": [[61, 56], [139, 80]],
    "切换小地图": [[84, 95], [108, 123]],
    "钟馗": [[250, 320], [271, 326]],
    "百晓仙子": [[294, 295], [335, 297]],
    "郑镖头": [[170, 326], [198, 335]],

    # 快捷点击
    "快速应战": [[631, 385], [813, 415]],
    "确认捉鬼": [[455, 332], [539, 355]],

    "队伍": [[774, 111], [836, 144]],
    "队伍头像": [[692, 161], [724, 195]],
    "离开队伍": [[576, 212], [659, 253]],
    "世界地图": [[1, 48], [39, 88]],
    "长安城": [[364, 310], [437, 354]],
    "东海湾": [[633, 331], [682, 362]],

    "押送普通镖银": [[656, 353], [809, 369]],
    "押送高级镖银(有难度": [[627, 384], [811, 415]],
    "云乐游": [[342, 330], [375, 333]],
    "云乐游秘境降妖": [[636, 254], [809, 281]],
    "继续挑战": [[674, 465], [708, 499]],

    "点击禁区": [[1, 369], [318, 554]],
}

# certain_coordinate = [
#     # 小地图
#     ("侠士副本", [[265, 136], [362, 151]]),
#     ("侠士1", [[209, 442], [300, 469]]),
#     ("侠士2", [[405, 445], [500, 473]]),
#     ("普通副本", [[265, 282], [297, 332]]),
#     ("普通1", [[209, 442], [300, 469]]),
#     ("普通2", [[405, 445], [500, 473]]),
#     ("普通3", [[595, 446], [685, 473]]),
#     ("选择副本", [[632, 300], [810, 325]]),
#     ("确定", [[457, 341], [534, 362]]),
#     ("活动", [[220, 45], [246, 82]]),
#     ("购买", [[625, 488], [725, 510]]),
#
#     # 小地图
#     ("打开小地图", [[61, 56], [139, 80]]),
#     # ("切换小地图", [[84, 95],  [108, 123]]),
#     ("钟馗", [[250, 320], [271, 326]]),
#     ("百晓仙子", [[294, 295], [335, 297]]),
#     ("郑镖头", [[170, 326], [198, 335]]),
#     ("店小二", [[506, 298], [536, 302]]),
#
#     # 快捷点击
#     ("快速应战", [[631, 385], [813, 415]]),
#     ("确认捉鬼", [[455, 332], [539, 355]]),
#
#     ("队伍", [[774, 111], [836, 144]]),
#     ("任务", [[712, 111], [774, 144]]),
#     ("队伍头像", [[692, 161], [724, 195]]),
#     ("离开队伍", [[576, 212], [659, 253]]),
#     ("世界地图", [[1, 48], [39, 88]]),
#     ("长安城", [[364, 310], [437, 354]]),
#     ("东海湾", [[633, 331], [682, 362]]),
#
#     ("押送普通镖银", [[656, 353], [809, 369]]),
#     ("押送高级镖银(有难度", [[627, 384], [811, 415]]),
#     ("云乐游", [[342, 330], [375, 333]]),
#     ("云乐游秘境降妖", [[636, 254], [809, 281]]),
#     ("继续挑战", [[674, 465], [708, 499]]),
#
#     ("点击禁区", [[1, 369], [318, 554]]),
# ]

model_type_instance = 5
# app_name = "MuMu模拟器12-1"
app_name = "MuMu模拟器12"

model_type = {
    1: ["跑镖","秘境降妖"],
    2: ["开始副本", "开始捉鬼"],
    3 : ["开始副本", "开始捉鬼","退出队伍","跑镖任务"],
    4: ["退出队伍","师门任务","跑镖"],
    5: ["开始捉鬼"],

}

click_sorted_update = {

    "师门任务":
        [
            "..."
        ]
    ,
    "秘境降妖":
        [
            "世界地图", "东海湾", "打开小地图", "云乐游", 10, "云乐游秘境降妖", "继续挑战",
            "..."
        ]
    ,

    # 侠士2确认,侠士1确认,然后开启
    # ... 后面的是结束出发条件
    "开始副本":
     [
         "...",
         "打开小地图", "百晓仙子", "选择副本", "侠士副本", "侠士2",
         "...",
         "打开小地图", "百晓仙子", "选择副本", "普通1",
         "...",
         "打开小地图", "百晓仙子", "选择副本", "普通2",  #
         "...", "打开小地图", "百晓仙子", "选择副本", "普通3",  #
         "...",
     ],
    "开始捉鬼":
        [
            # "打开小地图", "钟馗", 10,
            "...",
            "少侠已经捉完1轮鬼。是否继续捉鬼?",
            "...",
        ]
    ,
    "退出队伍":
        [
            "队伍", "队伍头像", "离开队伍", "确定"
        ]
    ,
    "去长安":
        [
            "世界地图", "长安城"
        ]
    ,

    "跑镖":
        [
            "世界地图", "长安城",
            "打开小地图", "郑镖头", 10,
            "押送普通镖银", 140,
            "押送普通镖银", 140,
            "押送普通镖银", 140,
            "打开小地图", "郑镖头", 1,
            "押送高级镖银(有难度", 140,
            "打开小地图", "郑镖头", 1,
            "押送高级镖银(有难度", 140,
            "打开小地图", "郑镖头", 1,
            "押送高级镖银(有难度", 140,
        ]
    ,
    "宝图任务":
        [
            "世界地图", "长安城", "打开小地图", "店小二", 15,
            "...",
        ]

    }

click_sorted = [

    (
        "师门任务",
        [
            # "..."
        ]
    ),
    (
        "秘境降妖",
        [
            # "世界地图", "东海湾", "打开小地图", "云乐游", 10, "云乐游秘境降妖", "继续挑战",
            # "..."
        ]
    ),

    # 侠士2确认,侠士1确认,然后开启
    # ... 后面的是结束出发条件
    ("开始副本",
     [
         "...",
         "打开小地图", "百晓仙子", "选择副本", "侠士副本", "侠士2",
         "...",
         "打开小地图", "百晓仙子", "选择副本", "普通1",
         "...",
         "打开小地图", "百晓仙子", "选择副本", "普通2",  #
         "...", "打开小地图", "百晓仙子", "选择副本", "普通3",  #
         "...",
     ]),
    (
        "开始捉鬼",
        [
            "打开小地图", "钟馗", 10,
            "...",
            "少侠已经捉完1轮鬼。是否继续捉鬼?",
            "...",
        ]
    ),
    (
        "退出队伍",
        [
            # "队伍", "队伍头像", "离开队伍", "确定"
        ]
    ),
    (
        "去长安",
        [
            # "世界地图", "长安城"
        ]
    ),

    (
        "跑镖",
        [
            "世界地图", "长安城",
            "打开小地图", "郑镖头", 15,
            "押送普通镖银", 140,
            "押送普通镖银", 140,
            "押送普通镖银", 140,
            "打开小地图", "郑镖头", 1,
            "押送高级镖银(有难度", 140,
            "打开小地图", "郑镖头", 1,
            "押送高级镖银(有难度", 140,
            "打开小地图", "郑镖头", 1,
            "押送高级镖银(有难度", 140,
        ]
    ),
    (
        "宝图任务",
        [
            # "世界地图", "长安城", "打开小地图", "店小二", 15,
            # "...",
        ]
    ),
]

extended_area = [
    ("得罪了", [5, 5, 50, 50]),  # 上下左右的可拓展像素
    ("快把悟空叫出来 !", [5, 5, 20, 20]),
    ("六耳大脑方寸山", [20, 8, 1, 50]),
    ("不 ! 我不要 !", [5, 5, 35, 35]),
    ("从菩提祖师手中救下六", [20, 10, 1, 5]),
    ("跳过剧情动画", [2, 2, 15, 15]),
    ("那就看你本事了", [5, 5, 25, 25]),
    ("再战阎罗王", [20, 10, 1, 80]),
    ("那又如何?", [5, 5, 40, 40]),
    ("老龙王的愤怒?", [20, 10, 2, 65]),
    ("有本事你就试试?", [20, 10, 2, 50]),

]


def get_all_odds():
    values_array = [value for _, sublist in anchors for value in sublist]
    return values_array


if __name__ == '__main__':
    get_all_odds()
