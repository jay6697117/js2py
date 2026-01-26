# 2.3.2 全局变量修改

counter = 0  # 全局变量


def increment():
    global counter  # 声明使用全局变量（不声明则无法修改）
    counter += 1
    print("计数器:", counter)


def increment_local():
    counter = 0  # 同名局部变量，与全局变量无关
    counter += 1
    print("局部计数器:", counter)


increment()  # 输出: 1
increment()  # 输出: 2
increment_local()  # 输出: 1（局部变量，不影响全局）
print("全局计数器:", counter)  # 输出: 2
