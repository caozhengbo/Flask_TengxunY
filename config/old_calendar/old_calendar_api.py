import random
import time, datetime
import sys


def get_old():
    activities = [
        {"name": "写单元测试", "good": "写单元测试将减少出错", "bad": "写单元测试会降低你的开发效率"},
        {"name": "洗澡", "good": "你几天没洗澡了？", "bad": "会把设计方面的灵感洗掉"},
        {"name": "锻炼一下身体", "good": "瘦10斤", "bad": "能量没消耗多少，吃得却更多"},
        {"name": "抽烟", "good": "抽烟有利于提神，增加思维敏捷", "bad": "除非你活够了，死得早点没关系"},
        {"name": "白天上线", "good": "今天白天上线是安全的", "bad": "可能导致灾难性后果"},
        {"name": "重构", "good": "代码质量得到提高", "bad": "你很有可能会陷入泥潭"},
        {"name": "使用%t", "good": "你看起来更有品位", "bad": "别人会觉得你在装逼"},
        {"name": "跳槽", "good": "该放手时就放手", "bad": "鉴于当前的经济形势，你的下一份工作未必比现在强"},
        {"name": "招人", "good": "你遇到千里马的可能性大大增加", "bad": "你只会招到一两个混饭吃的外行"},
        {"name": "面试", "good": "面试官今天心情很好", "bad": "面试官不爽，会拿你出气"},
        {"name": "提交辞职申请", "good": "公司找到了一个比你更能干更便宜的家伙，巴不得你赶快滚蛋", "bad": "鉴于当前的经济形势，你的下一份工作未必比现在强"},
        {"name": "申请加薪", "good": "老板今天心情很好", "bad": "公司正在考虑裁员"},
        {"name": "晚上加班", "good": "晚上是程序员精神最好的时候", "bad": "身心憔悴，早点休息"},
        {"name": "在妹子面前吹牛", "good": "改善你矮穷挫的形象", "bad": "会被识破"},
        {"name": "撸管", "good": "避免缓冲区溢出", "bad": "小撸怡情，大撸伤身，强撸灰飞烟灭"},
        {"name": "浏览成人网站", "good": "重拾对生活的信心", "bad": "你会心神不宁"},
        {"name": "命名变量", "good": "变量名萌萌哒", "bad": "这个变量永远引用不到"},
        {"name": "写超过%l行的方法", "good": "你的代码组织的很好，长一点没关系", "bad": "你的代码将混乱不堪，你自己都看不懂"},
        {"name": "提交代码", "good": "遇到冲突的几率是最低的", "bad": "你遇到的一大堆冲突会让你觉得自己是不是时间穿越了"},
        {"name": "代码复审", "good": "发现重要问题的几率大大增加", "bad": "你什么问题都发现不了，白白浪费时间"},
        {"name": "开会", "good": "写代码之余放松一下打个盹，有益健康", "bad": "你会被扣屎盆子背黑锅"},
        {"name": "打DOTA", "good": "你将有如神助", "bad": "你会被虐的很惨"},
        {"name": "晚上上线", "good": "晚上是程序员精神最好的时候", "bad": "你白天已经筋疲力尽了"},
        {"name": "修复BUG", "good": "你今天对BUG的嗅觉大大提高", "bad": "新产生的BUG将比修复的更多"},
        {"name": "设计评审", "good": "设计评审会议将变成头脑风暴", "bad": "人人筋疲力尽，评审就这么过了"},
        {"name": "需求评审", "good": "这个需求很简单", "bad": "公司需要一个能根据手机外壳变化APP皮肤的功能"},
        {"name": "上微博", "good": "今天发生的事不能错过", "bad": "会被老板看到"},
        {"name": "上AB站", "good": "还需要理由吗？", "bad": "会被老板看到"},
        {"name": "玩冒险岛Online", "good": "砸出二十五星神装", "bad": "除非你想把电脑砸了"},
        {"name": "打守望先锋", "good": "你将有如神助", "bad": "你会被虐的很惨"},
        {"name": "在维基萌抽卡", "good": "大概率抽到了自己心仪的卡", "bad": "垃圾卡片满天飞"},
        {"name": "写技术文章", "good": "新的水文即将诞生", "bad": "你的博文会被抄袭"},
    ]
    return activities[random.randint(0, len(activities) - 1)]


def get_time():
    t = time.strftime("今天是%Y年 %m月%d号", time.localtime())
    data = {
        "time_day": t
    }
    return data


# 座位朝向：面向东北方写程序，BUG 最少。
def directions():
    direc = ["北方", "东北方", "东方", "东南方", "南方", "西南方", "西方", "西北方"]
    data = {"direction": direc[random.randint(0, len(direc) - 1)]}
    # return direc[random.randint(0, len(direc) - 1)]
    return data


# 今日宜饮：
def get_drinks():
    # drinks = ["水", "茶", "红茶", "绿茶", "咖啡", "奶茶", "可乐", "牛奶", "豆奶", "果汁", "果味汽水", "苏打水", "运动饮料", "酸奶", "酒"]
    drinks = ["黑狗血", "黑驴血", "燕京", "崂山", "雪花", "大乌苏", "二锅头", "五粮液", "茅台", '剑南春', "青岛", "大黑啤", "哈尔滨啤酒", "喜力啤酒", "威士忌🥃"]
    return drinks[random.randint(0, len(drinks) - 1)]


# 女神亲近指数：2.5
def get_week_day():
    week_day_dict = {
        0: '星期一',
        1: '星期二',
        2: '星期三',
        3: '星期四',
        4: '星期五',
        5: '星期六',
        6: '星期天',
    }
    day = datetime.datetime.now().weekday()
    return {"week": week_day_dict[day]}
    # print(week_day_dict[day])


# 动画片
def Anime():
    cartoon = ['喜洋洋', '名侦探柯南', '洛克人', '海贼王', '漫画同人会', '青涩宝贝', '圣斗士星失', '仙境传说', '银河少女传说', '半龙少女', '超人特攻队', '怪物史莱克',
               '小飞象', '睡美人', '小猪佩奇', '花园宝宝', '葫芦娃', '钢铁战士']
    cartoon_1 = random.choice(cartoon)
    cartoon_2 = random.choice(cartoon)
    if cartoon_1 is cartoon_2:
        Anime()
    return cartoon_1 + "," + cartoon_2


# 奥特曼
def Ultraman():
    ultraman = [
        "佐菲奥特曼",
        "赛文奥特曼",
        "杰克奥特曼",
        "艾斯奥特曼",
        "奥特之父（叫肯）",
        "泰罗奥特曼",
        "奥特之母（叫玛丽）",
        "雷欧在哦特曼",
        "阿斯特拉奥特曼",
        "爱迪奥特曼",
        "尤丽安奥特曼（女）",
        "乔尼亚斯奥特曼",
        "艾米娅",
        "史考特奥特曼",
        "贝斯奥特曼",
        "察克奥特曼",
        "哉阿斯奥特曼",
        "迪迦奥特曼",
        "戴拿奥特曼",
        '盖亚奥特曼',
        "阿古茹奥特曼",
        "纳依斯奥特曼",
        "奈欧斯奥特曼",
        '赛文21奥特曼',
        "高斯奥特曼",
        "杰斯提斯奥特曼",
        "雷杰多奥特曼",
        "奈科斯特奥特曼",
        "奈克瑟斯奥特曼",
        "诺亚奥特曼",
        "麦克斯奥特曼",
        "杰诺奥特曼",
        "梦比优斯奥特曼",
        "希卡利奥特曼",
        '赛文X奥特曼',
        '赛罗奥特曼',
    ]
    ultraman_1 = random.choice(ultraman)
    ultraman_2 = random.choice(ultraman)
    if ultraman_1 is ultraman_2:
        Ultraman()
    return ultraman_1 + "," + ultraman_2


# 香烟
def smoke():
    Smoke = [
        "利群",
        "砖石",
        "白沙",
        "中南海",
        "新石家庄",
        "万宝路",
        "紫云",
        "玉溪",
        "一根华子",
    ]
    Smoke_1 = random.choice(Smoke)
    Smoke_2 = random.choice(Smoke)
    if Smoke_1 is Smoke_2:
        smoke()
    return Smoke_1 + "," + Smoke_2


def get_old_calendar():
    activities = get_old()
    activities1 = get_old()
    activities2 = get_old()
    activities3 = get_old()
    sys.setrecursionlimit(5000)
    if activities1 != activities and activities != activities2 and activities != activities3 and activities1 != activities2 and activities1 != activities3 and activities2 != activities3:
        # print(
        #     f"{get_time()}  {get_week_day()}\n\n 宜：\n{activities['name']}\t{activities['good']}  \n{activities1['name']}\t{activities1['good']}")
        # print(f"\n 忌：\n{activities2['name']}\t{activities2['bad']}  \n{activities3['name']}\t{activities3['bad']}")
        # print("\n座位朝向：面向{}写程序，BUG 最少。".format(directions()))
        # print("\n今日宜饮：{},{}".format(get_drinks(), get_drinks()))
        calendar = [get_time(), get_week_day(), activities, activities1, activities2, activities3, directions(),
                    get_drinks(), get_drinks(), Anime(), Ultraman(), smoke()]
        data = {
            "status_code": 0,
            "massage": "success",
            "data": {
                "results": calendar,
            }
        }
        return data
    else:
        get_old_calendar()

# if __name__ == '__main__':
#     print(get_old_calendar())
