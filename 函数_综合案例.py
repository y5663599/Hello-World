"""
银行
- 启动时输入姓名
- 输入1查余额，输入2存款，输入3取款，输入4退出
- 定义1，2，3，4四个函数
- 存款取款后显示余额
- 查询余额后会返回主菜单
- 选择退出或输入错误程序会结束，否则一直运行
"""
# 课前
# money = 10000
# name= input("请输入您的姓名:")
# def func1():
#     print(f"您的余额为：{money}")
# def func2():
#     global money
#     num1 = int(input("您打算存入："))
#     money += num1
#     print(f"存入{num1}，余额剩余{money}")
# def func3():
#     global money
#     num2 = int(input("您打算取出："))
#     money -= num2
#     print(f"取出{num2}，余额剩余{money}")
# def func4():
#     print(f"你好，{name}，欢迎来到银行，请选择操作：\n查询余额\t[输入1]\n存款   \t[输入2]\n取款   \t[输入3]\n退出   \t[输入4]")
#     op = int(input("请输入您的操作："))
#     if op == 1:
#         func1()
#         func4()
#     elif op == 2:
#         func2()
#         func4()
#     elif op == 3:
#         func3()
#         func4()
#     elif op == 4:
#         print("程序结束")
#     else:
#         print("检测到错误数字，程序结束")
# func4()
# 我的天哪，满足要求这一块，屎山的第一坨屎


# 课后
# 先设置全局变量
money = 10000
name = input("请输入您的姓名:")
# 定义查询函数
def func1(x):
    if x: # 当形参x为False时，执行完其他函数再执行func1就不会运行此if
        print("查询余额功能")
    print(f"{name},您的余额为：{money}")
# 定义存款函数
def func2(y):
    global money
    money += y
    print("存款功能")
    print(f"存入{y}")
    func1(False)
# 取款函数
def func3(g):
    global money
    money -= g
    print("取款功能")
    print(f"取出{g}")
    func1(False)
# 主菜单函数
def func4():
    print("主菜单功能")
    print(f"你好，{name}，欢迎来到银行，请选择操作：\n查询余额\t[输入1]\n存款\t\t[输入2]\n取款\t\t[输入3]\n退出\t\t[输入4]")
    return input("请输入您的操作：")
# 设置无限循环
while True:
    op = func4() # 每次循环都会触发一次主菜单函数重新获取输入值返回给op
    if op == "1":
        func1(True)
        continue
    elif op == "2":
        num = int(input("请输入您的存款金额："))
        func2(num)
        continue
    elif op == "3":
        num = int(input("请输入您的取款余额:"))
        func3(num)
        continue
    else:
        print("程序结束")
        break
# 传入参数，返回值
# 反思，进步