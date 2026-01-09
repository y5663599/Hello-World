# 设置1~100的随机数变量，通过while循环，配合input，语句判断输入的数字是否等于随机数
# - 无限次机会直到猜中
# - 没猜中提示大或者小
# - 猜完提示猜了几次

import random
num = random.randint(1,100)
# 课前
# n = 1
# guess = int(input("输入猜测的数字："))
# while guess != num:
#     if guess > num:
#         print("大了")
#     else:
#         print("小了")
#     print(f"第{n}次猜测，猜错")
#     guess = int(input("输入猜测的数字"))
#     n += 1
# print(f"猜测{n}次，猜对")

# 课后
n = 1
whether = True
while whether:
    guess = int(input("输入猜测的数字："))
    if guess == num:
        print(f"{n}次猜中了")
        whether = False
    else:
        if guess < num:
            print("小了")
        else:
            print("大了")
    n += 1