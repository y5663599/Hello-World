# print("hello\tworld")
# print("hellooo\tworld") ( \t )制表符号

# 使用while循环打印九九乘法表

# - 1.控制行的循环
# - 2.控制每一行输出的循环

# 课前
# n = 1
# while n <= 9:
#     u = 1
#     while u <= n:
#         print(f"{u}*{n}=",n*u," ",end='')
#         u += 1
#     print("\t")
#     n += 1

# 课后
n = 1
while n <= 9:
    u = 1
    while u <= n:
        print(f"{u}*{n}={n*u}\t",end='')
        u += 1
    n += 1
    print() #空白内容为输出换行