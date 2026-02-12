# 1. 准备一盘饺子 (列表)
# 这就是一个普通的列表，里面有 3 个饺子
pan_zi = ["饺子1", "饺子2", "饺子3"]

# 2. 只有把饺子装进 "自动喂食器" (迭代器/Iterator)，next 函数才能工作
# iter() 就是把盘子里的东西装进喂食器
wei_shi_qi = iter(pan_zi)

print("--- 开始吃饺子 ---")

print(f"这就是喂食器(迭代器)的真面目: {wei_shi_qi}")

# 👆 注意：直接打印它，只能看到通过 "内存地址" (类似于它的身份证号)
# 要吃到里面的东西，必须用 next()！
# 3. 使用 next() 函数
# next(喂食器) = 从喂食器里拿这就出来吃掉一个
# 这里的 "next" 就是 "下一个" 的意思

first_one = next(wei_shi_qi)
print(f"也就是: {first_one}")  # 输出: 饺子1

second_one = next(wei_shi_qi)
print(f"接着吃: {second_one}")  # 输出: 饺子2

third_one = next(wei_shi_qi)
print(f"最后吃: {third_one}")  # 输出: 饺子3

print("\n--- 盘子空了，如果再硬要吃... ---")

# 4. 如果没有饺子了，还硬要 next()，就会报错 (StopIteration)
# 下面这行如果不注释掉，程序就会崩溃报错
error_one = next(wei_shi_qi, "没有啦")
print("嘿嘿不报错:", error_one)

# # 5. 为了不报错，我们可以给 next 一个 "安慰奖" (默认值)
# # 如果拿不到了，就返回这个默认值，而不是报错
# empty_result = next(wei_shi_qi, "没有饺子啦！")
# print(f"再次尝试仅仅结果是: {empty_result}")
