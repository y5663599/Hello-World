# 定义一个函数，完成两数相加功能
def add(a,b):
    num = a + b
    # 通过返回值，将相加的结果返回给调用者
    return num
# 函数的返回值，可以通过变量去接收
cnm = add(1,9) # cnm接收了num的值
print(cnm)
# 注：函数体在遇到return后就结束了，写在return后的代码不会执行

# 好奇心测试
def ab(a,b):
    return a*b
FQ = ab(11,45)
print(FQ)