# Python 动态导入示例
import importlib

def load_module(module_name):
    """
    动态加载名为 module_name 的模块
    它会在当前目录的 modules 文件夹中寻找对应的模块
    """
    try:
        # 使用 importlib 动态加载模块，字符串 f"modules.{module_name}" 会告诉 python 去找 modules 文件夹下的对应文件
        module = importlib.import_module(f"modules.{module_name}")
        print(f"成功加载模块: {module_name}")
        return module
    except ImportError as error:
        print(f"无法加载模块 {module_name}: {error}")
        return None

# 使用动态导入
def main():
    print("--- 测试动态导入 math_utils ---")
    # 程序运行到这里时，才会去查找和加载 modules/math_utils.py
    math_module = load_module('math_utils')
    if math_module:
        # 成功加载后，就可以像普通导入的模块一样使用它里面的函数了
        result = math_module.add(5, 3)
        print(f"计算 5 + 3 = {result}")
    
    print("\n--- 测试动态导入 string_utils ---")
    # 程序运行到这里时，才会去查找和加载 modules/string_utils.py
    string_module = load_module('string_utils')
    if string_module:
        result = string_module.capitalize('hello dynamic import')
        print(f"转换结果: {result}")
        
    print("\n--- 测试动态导入不存在的模块 ---")
    # 这个模块不存在，会抛出异常并被 except 捕获
    non_exist_module = load_module('non_exist_module')

if __name__ == "__main__":
    main()
