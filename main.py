# 基本调用
def greet(name, age):
    return f"你好，{name}！你今年{age}岁。"


print(greet("张三", 25))

# 关键字参数调用
print(greet(name="李四", age=25))
print(greet(age=25, name="李四"))  # 参数顺序可以调换

# 字典解包
person = {"name": "王五", "age": 30}
print(greet(**person))


# 方法调用
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"你好，{self.name}！"


person = Person("赵六")
print(person.greet())
