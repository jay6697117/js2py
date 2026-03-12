# calculator.py - Python 版本
class Calculator:
    """计算器类，支持基本运算和历史记录"""

    def __init__(self):
        self.history = []

    def add(self, a, b):
        """加法运算"""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        """减法运算"""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        """乘法运算"""
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        """除法运算"""
        if b == 0:
            raise ValueError("除数不能为零")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result

    def get_history(self):
        """获取计算历史"""
        return self.history

    def clear_history(self):
        """清空计算历史"""
        self.history = []


# 工具函数
def validate_number(num):
    """验证数字"""
    return isinstance(num, (int, float)) and not isinstance(num, bool)


def format_result(result):
    """格式化结果"""
    return f"结果: {result}"


# 如果直接运行此文件
print("__name__ 2:", __name__)
if __name__ == "__main__":
    calc = Calculator()
    print(calc.add(10, 5))
    print(calc.multiply(4, 3))
    print("计算历史:", calc.get_history())
