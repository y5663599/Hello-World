# 函数：是组织好的，可重复使用的，用来实现特定功能的代码段

# 统计字符串的长度，不使用内置函数len()
n1 = "qwerasdf"
n2 = "qwerasd"
n3 = "qweras"

y = 0
for x in n1:
    y += 1
print(f"{n1}的长度是{y}")

y = 0
for x in n2:
    y += 1
print(f"{n2}的长度是{y}") # 重复的代码


# 使用函数优化
def myLen(num):
    count = 0
    for n in num:
        count += 1
    print(f"字符串{num}的长度是{count}")  # 已组织好的
myLen(n1)                              # 可重复使用
myLen(n2)                              # 针对特定功能
myLen(n3)

# - 将功能封装在函数内，可供随时随地重复利用
# - 提高代码复用性，减少重复代码，提高开发效率