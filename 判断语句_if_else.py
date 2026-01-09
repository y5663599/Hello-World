# 演示if else的组合判断语句
print("欢迎来到游乐场，儿童免费，成人收费")
age = int(input("您的年龄是："))
if age >= 18:
    print("您已成年，需购票10元")
else:
    print("您未成年，可以免费游玩")
print("祝您游玩愉快")


# 小练习
print("欢迎来到动物园，身高120cm以下免费，以上收费")
height = int(input("请输入身高(cm):"))
if height > 120:
    print("需要买票")
else:
    print("不需要买票")