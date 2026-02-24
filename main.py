# math_utils.py - Python 模块
def add(a, b):
    """加法函数"""
    return a + b


def multiply(a, b):
    """乘法函数"""
    return a * b


# 模块级变量（类似 JavaScript 的常量）
PI = 3.14159


# Python 没有默认导出的概念，但可以定义 __all__ 来控制 from module import * 的行为
__all__ = ["add", "multiply", "PI"]
