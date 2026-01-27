# 创建集合
set_data = {1, 2, 3, 3, 4}  # 自动去重

# 添加元素
set_data.add(5)

# 删除元素
set_data.remove(3)  # 如果不存在会报错
set_data.discard(3)  # 推荐使用，元素不存在时不会报错

# 检查元素
print(2 in set_data)

# 集合操作
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# 并集
union = set1 | set2
union = set1.union(set2)

# 交集
intersection = set1 & set2
intersection = set1.intersection(set2)

# 差集
difference = set1 - set2
difference = set1.difference(set2)

print("并集:", union)
print("交集:", intersection)
print("差集:", difference)
