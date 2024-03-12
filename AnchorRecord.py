from LargeRecord import anchors, certain_coordinate_windows

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
    "同意入队"
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


def get_certain_coordinate(text):
    return text, certain_coordinate_windows.get(text)


model_type_instance = 5
# app_name = "MuMu模拟器12-1"
app_name = "MuMu模拟器12"

model_type = {
    1: ["跑镖", "秘境降妖"],
    2: ["开始副本", "开始捉鬼"],
    3: ["开始副本", "开始捉鬼", "退出队伍", "跑镖任务"],
    4: ["退出队伍", "师门任务", "跑镖"],
    5: ["开始捉鬼"],

}


def get_final_values(target):
    # Initialize a list to store the final values that are not keys
    final_values = []

    # Function to recursively explore the values
    def explore_value(key):
        # If the value is also a key in the data, recursively explore its values
        if key in click_sorted_update:
            for next_value in certain_coordinate_windows[key]:
                explore_value(next_value)
        else:
            # If the value is not a key, add it to the final values list
            final_values.append(certain_coordinate_windows)

    # Start exploring the initial key
    explore_value(target)

    return final_values


# certain_coordinate_windows 分为俩种类型
# -------- 坐标点击
# "创建队伍": [[364, 310], [437, 354]],
# "关闭队伍": [[364, 310], [437, 354]],
# "消息": [[364, 310], [437, 354]],
# "世界频道": [[364, 310], [437, 354]],
# "gangsChannel": [[364, 310], [437, 354]],
# "输入框": [[364, 310], [437, 354]],
# "sendMessage": [[364, 310], [437, 354]],
# "closeMessage": [[364, 310], [437, 354]],
# "同意入队": [[364, 310], [437, 354]],
# --------- 逻辑代码
# "确定已经进入副本了吗": [[364, 310], [437, 354]],
# "同意入队": [[364, 310], [437, 354]],
# "输入 520": [[364, 310], [437, 354]],

is_running_logic_code = {
    "确定已经进入副本了吗": "AreYouSureYouAreInCopy",
    "同意入队": "AccessTeammate",
    "输入 520": "Input520",
}

click_sorted_update = {
    "组队520":
        [
            "创建队伍", "worldAndGangCriesOut", "addTeammate", "confirmedAccessChivalrousCopy"
        ]
    ,

    "创建队伍":
        [
            "队伍", "创建队伍", "关闭队伍"
        ]
    ,

    "confirmedAccessChivalrousCopy":
        [
            "寻找白晓仙子", "选择副本", "侠士副本", "侠士2", "确定已经进入副本了吗",
            "去长安", "寻找白晓仙子", "选择副本", "侠士副本", "侠士1", "确定已经进入副本了吗",
        ]
    ,

    "寻找白晓仙子":
        [
            "打开小地图", "百晓仙子",
        ]
    ,

    "addTeammate":
        [
            "队伍", "applyTeam", "同意入队"
        ]
    ,

    "worldAndGangCriesOut":
        [
            "消息", "世界频道", "输入框", "输入 520", "sendMessage",
            "gangsChannel", "输入框", "输入 520", "sendMessage",
            "closeMessage"
        ]
    ,

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
