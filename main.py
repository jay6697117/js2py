# 2.3.2 全局变量修改
# 1. 定义一个“公共记分牌”（全局变量），所有人在任何地方都能看到它
counter = 0  # 2


def increment():
    # 2. 【关键】我想修改外面的“公共记分牌”，必须先拿钥匙（声明 global）才能改
    global counter
    counter += 1
    print("计数器:", counter)  # 1 2


def increment_local():
    # 3. 这里定义的是“私有记分牌”（局部变量），虽然名字一样，但只在函数内部有效，跟外面无关
    counter = 0
    counter += 1
    print("局部计数器:", counter)  # 1


# 4. 调用两次函数：修改的是外面的“公共记分牌”
increment()
increment()

# 5. 调用一次局部函数：它关起门来改自己的“私有记分牌”，不会影响外面
increment_local()

# 6. 验证结果：外面的“公共记分牌”确实被修改了（应该是 2）
print("全局计数器:", counter)  # 2
