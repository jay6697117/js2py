# ============================================================
# 🎯 Python 函数定义大赏 - 从青铜到王者的进化之路
# ============================================================


# 🥉 青铜段位：最朴素的函数，一个萝卜一个坑
def greet(name):
    return f"你好，{name}！"  # f-string：Python界的字符串缝合怪，好用到哭


# 🥈 白银段位：默认参数登场！没人叫你？那就自己打招呼
def greet2(name="世界"):
    return f"你好，{name}！"  # 调用时不传参？没关系，默认跟世界say hi


# 🥇 黄金段位：类型注解，让代码自己解释自己（IDE也会感谢你）
def greet3(name: str) -> str:
    return f"你好，{name}！"  # str -> str：进去是字符串，出来还是字符串，童叟无欺


# 💎 铂金段位：多参数，信息量up up！
def greet4(name, age):
    return f"你好，{name}！你今年{age}岁。"  # 一次性问候+猜年龄，社交达人必备


# 👑 钻石段位：可选参数，进可攻退可守的智慧
def greet5(name, age=None):
    if age:  # 有年龄就多聊两句，没有就保持神秘
        return f"你好，{name}！你今年{age}岁。"
    return f"你好，{name}！"  # 不问年龄才是真正的社交礼仪


# 🏆 王者段位：字典解构，数据打包一把梭
def greet6(person):
    name = person["name"]  # 从字典里掏名字
    age = person["age"]  # 再掏年龄，像开盲盒一样
    return f"你好，{name}！你今年{age}岁。"


# 🚀 发射台：让我们看看这些函数的实际表演
print(greet("张三"))  # 基础款问候
print(greet2())  # 懒人专用（不传参也能跑）
print(greet6({"name": "李四", "age": 25}))  # 豪华打包版
