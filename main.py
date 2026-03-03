# main.py - 使用计算器
from calculator import Calculator, validate_number, format_result

def main():
    # 创建计算器实例
    calc = Calculator()

    # 基本运算
    print(format_result(calc.add(10, 5)))      # 结果: 15
    print(format_result(calc.subtract(10, 3))) # 结果: 7
    print(format_result(calc.multiply(4, 6)))  # 结果: 24
    print(format_result(calc.divide(20, 4)))   # 结果: 5.0

    # 查看历史记录
    print("计算历史:")
    for record in calc.get_history():
        print(f"  {record}")

    # 错误处理
    try:
        calc.divide(10, 0)
    except ValueError as error:
        print(f"错误: {error}")

    # 验证数字
    print(validate_number(42))     # True
    print(validate_number("42"))   # False
    print(validate_number(3.14))   # True

if __name__ == "__main__":
    main()