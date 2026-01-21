# 全局作用域
global_var = "我是全局变量"


def test_scope():
    # 函数作用域
    function_var = "我是函数内变量"

    if True:
        # Python 没有块级作用域！
        block_var = "我是块级变量"
        print("块内访问:", block_var)
        print("块内访问函数变量:", function_var)
        print("块内访问全局变量:", global_var)

    # 块外仍然可以访问块级变量
    print("函数内访问块级变量:", block_var)
    print("函数内访问函数变量:", function_var)
    print("函数内访问全局变量:", global_var)


test_scope()
print("全局访问全局变量:", global_var)
# print(function_var)  # 错误！
