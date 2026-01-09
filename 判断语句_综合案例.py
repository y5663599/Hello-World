# 定义一个数字（1~10，随机产生），通过3次判断猜出来数字
# -数字随机产生，范围1~10
# -有3次机会猜测数字，通过3层嵌套实现
# -每次猜不中，会提示大了或小了
import random
num = random.randint(1,10)

print("猜猜数字吧（1~10）,三次机会")
# 课前
# num1 = int(input("第一次机会："))
# if num1 == num:
#     print("第一次就猜对，666开了")
#
# elif num1 > num:
#     print("大了")
#     num2 = int(input("第二次机会:"))
#     if num2 == num:
#         print("第二次就猜对，运气")
#     elif num2 > num:
#         print("大了")
#         num3 = int(input("第三次机会:"))
#         if num3 == num:
#             print("第三次才猜对，拉完了")
#         else:
#             print(f"三次机会都没有猜对，fvv，数字是{num}")
#     elif num2 < num:
#         print("小了")
#         num3 = int(input("第三次机会:"))
#         if num3 == num:
#             print("第三次才猜对，拉完了")
#         else:
#             print(f"三次机会都没有猜对，fvv，数字是{num}")
#
# elif num1 < num:
#     print("小了")
#     num2 = int(input("第二次机会:"))
#     if num2 == num:
#         print("第二次就猜对，运气")
#     elif num2 > num:
#         print("大了")
#         num3 = int(input("第三次机会:"))
#         if num3 == num:
#             print("第三次才猜对，拉完了")
#         else:
#             print(f"三次机会都没有猜对，fvv，数字是{num}")
#     elif num2 < num:
#         print("小了")
#         num3 = int(input("第三次机会:"))
#         if num3 == num:
#             print("第三次才猜对，拉完了")
#         else:
#             print(f"三次机会都没有猜对，fvv，数字是{num}")
# 若猜测次数增加代码量成倍增长，

# 课后
num1 = int(input("第一次猜数字："))
if num1 == num:
    print("第一次就猜中了")
else:
    if num1 > num:
        print("大了")
    else:
        print("小了")
    num2 = int(input("第二次猜数字："))
    if num2 == num:
        print("第二次机会猜中了")
    else:
        if num2 > num:
            print("大了")
        else:
            print("小了")
        num3 = int(input("第三次猜数字："))
        if num3 == num:
            print("第三次机会猜中了")
        else:
            print(f"三次机会都没有猜中，数字是{num}")