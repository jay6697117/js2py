# ========== Python 集合(Set) 速成 ==========
# 集合特点: 无序、不重复、可变（像个有洁癖的篮子）

# 创建集合 - 重复的3？不好意思，只留一个
set_data = {1, 2, 3, 3, 4}  # 结果: {1, 2, 3, 4}

# 添加元素 - 来者不拒（除非你已经在里面了）
set_data.add(5)

# 删除元素 - 两种脾气
set_data.remove(3)  # 暴躁型：找不到就报错 KeyError
set_data.discard(3)  # 佛系型：找不到？没事，当无事发生

# 查户口 - 问：2在不在？
print(2 in set_data)  # True/False

# ========== 集合运算（数学课本复活！）==========
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# 并集 - 我全都要！两边元素合体
union = set1 | set2  # 符号版：|
union = set1.union(set2)  # 方法版

# 交集 - 找共同好友
intersection = set1 & set2  # 符号版：&
intersection = set1.intersection(set2)

# 差集 - set1有但set2没有的（单相思）
difference = set1 - set2  # 符号版：-
difference = set1.difference(set2)

print("并集:", union)  # {1, 2, 3, 4, 5}
print("交集:", intersection)  # {3}
print("差集:", difference)  # {1, 2}
