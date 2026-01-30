# math_utils.py - Python 模块
# 提示：这就是传说中比 JavaScript 模块简单 100 倍的 Python 模块 😎


def add(a, b):
    """加法函数 - 小学数学，但程序员每天都在用"""
    return a + b  # 就这么简单，连 if 判断都不需要


def multiply(a, b):
    """乘法函数 - 比加法高级一点点，但也就那样"""
    return a * b  # 注意：Python 的 * 是乘法，不是指针（C++ 程序员请注意）


# 模块级变量（类似 JavaScript 的常量）
PI = 3.14159  # 圆周率：数学界最著名的网红，背后有无限位小数

# Python 没有默认导出的概念，但可以定义 __all__ 来控制 from module import * 的行为
# 翻译：这是 Python 的"出口管制清单"，只有这里列出的才能被 * 一键带走
__all__ = ["add", "multiply", "PI"]  # 想导入别的？门都没有！
