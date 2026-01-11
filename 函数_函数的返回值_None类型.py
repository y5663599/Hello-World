# 函数没有使用return语句返回数据，那么函数有返回值吗？  有的兄弟有的
def say():
    print("hello")
# 使用变量n接收say()的返回值
n = say()
# 打印返回值
print(f"无返回值函数，返回的内容是：{n}") # 输出：None（无意味）
# 打印返回值类型
print(f"无返回值函数，返回的内容类型是：{type(n)}") # 输出：<class 'NoneType'>


# None可以主动使用return返回，效果等同于不写return语句：
def say1():
    print("hello")
    return None
# 使用变量n接收say()的返回值
u = say1()
# 打印返回值
print(u) # 输出：None
# 打印返回值类型
print(type(u)) # 输出：<class 'NoneType'>

"""
None的应用场景
- 用在函数无返回值上

- 用在if判断上
- - 在if判断中，None等同于False
- - 一般用于在函数中主动返回None，配合if判断做相关处理

- 用于声明无内容的变量上
- - 定义变量，但暂时不需要变量有具体值，可以用None来代替

- 暂不赋予变量具体值
- - name = None
"""

# None用于if
def age(x):
    if x > 18:
        return "有意味"
    else:
        return None # 无意味
yw = age(int(input("何意味：")))
if not yw: # 若返回值为None，在if中等同于False，即：if None等同于if False。 使用not反转：if not None等同于if not False等同于if True
    print("意味你令人着迷")
else:
    print(yw)

# None用于声明无初始内容的变量
name = None