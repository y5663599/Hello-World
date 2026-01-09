# 演示判断语句的嵌套使用

print("动物园，身高120cm一下免费、vip等级>3免费")
if int(input("请输入您的身高（cm）：")) > 120:
    print("您的身高不满足免费条件")
    print("vip等级等级>3也可以免费")
    if int(input("请输入您的vip等级（1~5）：")) <= 3:
        print("vip不满足免费条件，您需买票")
    else:
        print("vip满足免费条件")
else:
    print("身高满足免费条件")


# 小练习
print("公司发礼物，条件为大于等于18岁小于30岁的成年人，同时工作时间大于两年，或者级别大于3")

age = int(input("请输入您的年龄："))
if 30 > age >= 18:
    print("年龄符合标准")
    if int(input("请输入您的工作时间")) > 2:
            print("条件足够您可以领取礼物")
    elif int(input("请输入您的级别：")) > 3:
            print("级别足够您可以领取礼物")
    else:
            print("不满足条件，不行")
else:
    print("年龄不符合标准")