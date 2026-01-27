# ========== 字典：Python的"万能收纳盒" ==========

# 创建字典 —— 用花括号{}，键值对用冒号:连接
person = {"name": "张三", "age": 25}  # 恭喜，你有了一个虚拟人类

# ---------- 读取数据 ----------

print(person["name"])  # 硬核取值：没有就报错，适合自信的你
print(person.get("name"))  # 温柔取值：没有返回None，不会炸
print(person.get("city", "未知"))  # 贴心取值：没有就用默认值，人美心善

# ---------- 增改数据 ----------

person["city"] = "北京"  # 新key=添加，老key=覆盖，一招鲜吃遍天
person["job"] = "程序员"  # 又多了个属性，张三越来越立体了

# ---------- 删除数据 ----------

del person["age"]  # 暴力删除：key不存在直接报错（慎用！）
person.pop("age", None)  # 优雅删除：不存在也不慌，返回None

# ---------- 遍历三连 ----------

# 方式1：items() 同时拿key和value，最常用
for key, value in person.items():
    print(f"{key}: {value}")

# 方式2：keys() 只要key，value自己取
for key in person.keys():
    print(f"{key}: {person[key]}")

# 方式3：values() 只要value，key是谁我不care
for value in person.values():
    print(value)
