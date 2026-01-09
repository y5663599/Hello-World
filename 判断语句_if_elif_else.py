# 演示if elif else多条件判断语句的使用

print("欢迎参观动物园，身高120cm以下或vip等级>3可以免费，否则收费，1号免费日")
if int(input("请输入您的身高(cm)：")) < 120:
    print("身高小于120cm，您可以免费游玩")
elif int(input("请输入您的vip等级(1~5)：")) > 3:
    print("vip等级>3，您可以免费游玩")
elif int(input("今天几号(1~30)：")) == 1:
    print("免费日，您可以免费游玩")
else:
    print("您需要收费")


# 小练习
print("猜猜我心里想的数字吧（1~10）")
num = 5
if int(input("请输入您猜想的数字（1~10）：")) == num:
    print("太厉害了一次猜对")
elif int(input("不对，再猜一次吧（1~10）：")) == num:
    print("猜对啦")
elif int(input("不对，最后一次机会了（1~10）：")) == num:
    print("终于猜对啦")
else:
    print("太可惜了都没有猜对，我心里的数字是10")