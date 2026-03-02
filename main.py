# # 点名道姓地导入，清晰明了，编辑器绝对不会报错！
# from math_utils import add, multiply, PI

# # 因为你在 __all__ 里规定了可以导出这三个，所以可以直接用
# print(add(10, 20))
# print(multiply(2, 3))
# print(PI)

# Python 导入方式
# # 1. 导入整个模块
# import math_utils

# # 2. 从模块导入特定函数/变量
# from math_utils import add, multiply, PI

# 3. 导入所有内容（不推荐）
# from math_utils import *

# # 4. 重命名导入
# from math_utils import add as add_function
# print(add_function(1, 2))

# 5. 重命名模块
# import math_utils as math
# print(math.add(1, 2))

# # 6. 从模块导入并重命名
# from math_utils import add as add_func, multiply as mul
# print(add(5, 3)) // 8
# print(multiply(4, 2)) // 8
# print(PI) // 3.14159
# print(math_utils.add(10, 5)) // 15
# print(add_func(1, 2)) // 3
# print(mul(4, 2)) // 8

# # Python 模块特殊变量

# # __file__ - 当前文件路径
# print("__file__:", __file__)

# # __name__ - 模块名称
# print("__name__:", __name__)

# # __doc__ - 模块文档字符串
# print("__doc__:", __doc__)

# # __all__ - 控制 from module import * 的行为
# # ⚠️ 注意：__all__ 不会自动生成，必须手动定义，否则直接使用会报错！
# __all__ = []  # 我们先手动定义一个空列表试试看
# print("__all__:", __all__)

# # 判断是否为直接运行的文件
# if __name__ == "__main__":
#     print("这个文件被直接运行")
# else:
#     print("这个文件被作为模块导入")

# Python 包结构示例
# my_package/
# ├── __init__.py          # 包初始化文件
# ├── math_utils.py        # 数学工具模块
# ├── string_utils.py      # 字符串工具模块
# └── tests/
#     ├── __init__.py
#     └── test_math.py

# __init__.py - 包初始化文件
from .math_utils import add, multiply
from .string_utils import capitalize, reverse

__all__ = ["add", "multiply", "capitalize", "reverse"]
