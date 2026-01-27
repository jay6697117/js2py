# if-elif-else 语句
age = 18
if age >= 18:
    print("成年人")
elif age >= 12:
    print("青少年")
else:
    print("儿童")

# 三元运算符（条件表达式）
status = "成年人" if age >= 18 else "未成年人"  # 语法顺序为： 值 if 条件 else 否则的值
print(status)

# match 语句（Python 3.10+）
day = "Monday"
match day:
    case "Monday":
        print("星期一")
    case "Tuesday":
        print("星期二")
    case _:
        print("其他日子")
