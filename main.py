# 函数定义
def greet(name):
    return f"你好，{name}！"


# 默认参数
def greet2(name="世界"):
    return f"你好，{name}！"


# 类型注解（Python 3.5+）
def greet3(name: str) -> str:
    return f"你好，{name}！"


# 多参数
def greet4(name, age):
    return f"你好，{name}！你今年{age}岁。"


# 关键字参数
def greet5(name, age=None):
    if age:
        return f"你好，{name}！你今年{age}岁。"
    return f"你好，{name}！"


# 解构参数（使用字典）
def greet6(person):
    name = person["name"]
    age = person["age"]
    return f"你好，{name}！你今年{age}岁。"


print(greet("张三"))
print(greet2())
print(greet6({"name": "李四", "age": 25}))
