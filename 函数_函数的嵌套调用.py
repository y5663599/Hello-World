# 演示嵌套调用函数

# 定义函数func1
def func1():
    print("--2--")

# 定义函数func2
def func2():
    print("--1--")

    # 嵌套调用func1
    func1()

    print("--3--")

# 调用函数fun1测试
func2()