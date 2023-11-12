import random
while True:
    num = random.randint(0,21)
    a = int(input("请输入一个整数:"))
    if a == num:
        print("猜对了★",a)
    elif a>num:
        print("猜大了",a)
    elif a<num:
        print("猜小了",a)