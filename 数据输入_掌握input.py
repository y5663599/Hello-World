# 演示input语句
# 获取键盘输入
print("请告诉我你是谁：")
name = input()
print(f"你是{name}")

name = input("请告诉我你是谁：")
print(f"你是{name}")

# 数字类型
num = input("请告诉我你的密码：")
print(f"你的密码类型是{type(num)}")
# 获取到键盘输入的类型永远为字符串

# 数据类型转换
num = input("请告诉我你的密码：")
num = int(num)
print(f"你的密码类型是{type(num)}")

# 小练习
userName = input("请输入您的名字：")
userType = input("请输入您的类型：")
print(f"您好：{userName},您是尊贵的{userType}用户，欢迎您的光临")