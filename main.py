# 点名道姓地导入，清晰明了，编辑器绝对不会报错！
from math_utils import add, multiply, PI

# 因为你在 __all__ 里规定了可以导出这三个，所以可以直接用
print(add(10, 20))
print(multiply(2, 3))
print(PI)
