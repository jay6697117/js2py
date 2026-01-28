from math_utils import add, subtract, Calculator

calc = Calculator()

print(add(5, 3))  # 8
print(subtract(10, 3))  # 7

print("----------------")

print(calc.add(10).add(4).result)  # 14
print(calc.subtract(10).subtract(2).result)  # 6

print(calc.result)  # 2
