"""
Python 数据类型演示
==================
本文件演示了 Python 中的基本数据类型和引用类型。
Python 是动态类型语言，变量不需要声明类型，解释器会自动推断。
"""

# ============================================================
# 一、基本类型（不可变类型 - Immutable Types）
# ============================================================
# 基本类型的值一旦创建就不能被修改，对变量的重新赋值实际上是创建了一个新对象

# 1. 字符串类型 (str)
# - 用于存储文本数据
# - 可以使用单引号 '' 或双引号 "" 定义
# - 字符串是不可变的，任何修改都会创建新的字符串对象
string = "文本"

# 2. 整数类型 (int)
# - 用于存储整数，没有大小限制（Python 会自动处理大整数）
# - 支持二进制(0b)、八进制(0o)、十六进制(0x) 表示法
# - 例如: 0b1010 = 10, 0o12 = 10, 0xA = 10
number = 42

# 3. 布尔类型 (bool)
# - 只有两个值: True 和 False（注意首字母大写！）
# - 在条件判断中，以下值被视为 False:
#   None, 0, 0.0, '', [], {}, set()
# - 其他所有值都被视为 True
boolean = True  # 注意大写，与 JavaScript 的 true 不同

# 4. 空值类型 (NoneType)
# - None 表示"没有值"或"空"
# - 相当于 JavaScript 的 null
# - 常用于函数没有返回值时的默认返回、变量的初始化占位
none_value = None  # 相当于 JavaScript 的 null

# 5. 复数类型 (complex)
# - Python 原生支持复数运算（这是很多语言没有的特性！）
# - 格式: 实部 + 虚部j（注意是 j 不是 i）
# - 常用于科学计算、信号处理、电气工程等领域
# - 可以通过 .real 获取实部，.imag 获取虚部
complex_number = 3 + 4j  # 3 是实部，4 是虚部
print(f"复数: {complex_number}")
print(f"  实部: {complex_number.real}")  # 输出: 3.0
print(f"  虚部: {complex_number.imag}")  # 输出: 4.0

# ============================================================
# 二、引用类型（可变/不可变类型 - Reference Types）
# ============================================================
# 引用类型存储的是对象的引用（内存地址），而不是实际的值

# 1. 列表 (list) - 可变类型
# - 有序的元素集合，可以包含不同类型的元素
# - 使用方括号 [] 定义
# - 支持索引访问、切片、增删改查等操作
# - 相当于 JavaScript 的 Array
array = [1, 2, 3]  # 列表（可变）
# 常用操作:
# array.append(4)     # 末尾添加元素
# array.insert(0, 0)  # 指定位置插入
# array.pop()         # 移除并返回最后一个元素
# array[0] = 10       # 修改指定位置的元素

# 2. 元组 (tuple) - 不可变类型
# - 有序的元素集合，一旦创建就不能修改
# - 使用圆括号 () 定义
# - 比列表更节省内存，访问速度更快
# - 常用于函数返回多个值、作为字典的键
tuple_data = (1, 2, 3)  # 元组（不可变）
# 注意: 单元素元组需要加逗号: (1,)

# 3. 字典 (dict) - 可变类型
# - 键值对的集合，键必须是不可变类型（如字符串、数字、元组）
# - 使用花括号 {} 定义
# - 相当于 JavaScript 的 Object 或 Map
# - Python 3.7+ 保证插入顺序
dictionary = {"key": "value"}  # 字典
# 常用操作:
# dictionary["new_key"] = "new_value"  # 添加/修改
# dictionary.get("key", "默认值")      # 安全获取（键不存在时返回默认值）
# dictionary.keys()                    # 获取所有键
# dictionary.values()                  # 获取所有值
# dictionary.items()                   # 获取所有键值对

# 4. 集合 (set) - 可变类型
# - 无序的、不重复的元素集合
# - 使用花括号 {} 定义（注意：空集合用 set() 而不是 {}）
# - 常用于去重、集合运算（并集、交集、差集）
set_data = {1, 2, 3}  # 集合
# 常用操作:
# set_data.add(4)           # 添加元素
# set_data.remove(1)        # 移除元素（不存在会报错）
# set_data.discard(1)       # 移除元素（不存在不报错）
# set_a | set_b             # 并集
# set_a & set_b             # 交集
# set_a - set_b             # 差集

# ============================================================
# 三、类型检查
# ============================================================
# 使用 type() 函数可以查看变量的类型
# 使用 isinstance() 函数可以检查变量是否是某个类型的实例

print("\n=== 类型检查 ===")
print(f"string 的类型: {type(string)}")  # <class 'str'>
print(f"number 的类型: {type(number)}")  # <class 'int'>
print(f"boolean 的类型: {type(boolean)}")  # <class 'bool'>
print(f"none_value 的类型: {type(none_value)}")  # <class 'NoneType'>
print(f"complex_number 的类型: {type(complex_number)}")  # <class 'complex'>

print("\n=== 引用类型检查 ===")
print(f"array 的类型: {type(array)}")  # <class 'list'>
print(f"tuple_data 的类型: {type(tuple_data)}")  # <class 'tuple'>
print(f"dictionary 的类型: {type(dictionary)}")  # <class 'dict'>
print(f"set_data 的类型: {type(set_data)}")  # <class 'set'>

# ============================================================
# 四、isinstance() 类型检查
# ============================================================
# isinstance() 比 type() 更推荐使用，因为它支持继承检查
# 语法: isinstance(对象, 类型) 或 isinstance(对象, (类型1, 类型2, ...))

print("\n=== isinstance() 类型检查 ===")

# 1. 基本用法 - 检查单个类型
print(f"string 是字符串吗? {isinstance(string, str)}")  # True
print(f"number 是整数吗? {isinstance(number, int)}")  # True
print(f"boolean 是布尔吗? {isinstance(boolean, bool)}")  # True
print(f"array 是列表吗? {isinstance(array, list)}")  # True

# 2. 检查多个类型（元组形式）- 只要是其中之一就返回 True
print(f"\nnumber 是 int 或 float 吗? {isinstance(number, (int, float))}")  # True
print(f"string 是 str 或 list 吗? {isinstance(string, (str, list))}")  # True

# 3. 布尔类型的特殊性 - bool 是 int 的子类！
print("\n布尔值的特殊性:")
print(f"  True 是 bool 吗? {isinstance(True, bool)}")  # True
print(f"  True 是 int 吗? {isinstance(True, int)}")  # True（因为 bool 继承自 int）
print(f"  type(True) == bool: {type(True) == bool}")  # noqa: E721 演示用
print(f"  type(True) == int: {type(True) == int}")  # noqa: E721 演示用

# 4. isinstance() vs type() 的区别
# - isinstance() 会考虑继承关系，推荐使用
# - type() 只检查精确类型，不考虑继承
print("\nisinstance() 和 type() 的区别:")
print(f"  isinstance(True, int): {isinstance(True, int)}")  # True
print(f"  isinstance(True, int): {isinstance(True, bool)}")  # True
print(f"  type(True) == int: {type(True) == int}")  # noqa: E721 False
print(f"  type(True) == int: {type(True) == bool}")  # noqa: E721 True
