# Python 全局变量修改
counter = 0


def increment():
    global counter  # 声明使用全局变量
    counter += 1
    print("计数器:", counter)


def increment_local():
    counter = 0  # 创建局部变量
    counter += 1
    print("局部计数器:", counter)


increment()
increment()
increment_local()

print("全局计数器:", counter)
