# Python 作用域练习
x = 10


def outer():
    x = 20

    def inner():
        x = 30
        print("inner x:", x)  # 30

    inner()
    print("outer x:", x)  # 20


outer()
print("global x:", x)  # 10
