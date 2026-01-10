# for循环语句，本质上时遍历：序列类型
"""
range()语句
语法1
range(num)
获取一个从0开始，到num结束的数字序列（不含num本身）
如，range(5)取得的数据是：[0,1,2,3,4]
"""
for x in range(10):
    print(x)


"""
语法2
range(num1,num2)
获得从num1开始到num2结束的数字序列（不含num2本身）
如，range(5,10)取得的数据是[5,6,7,8,9]
"""
for x in range(5,15):
    print(x)


"""
语法3
range(num1,num2,step)
获得一个从num1开始到num2结束的数字序列（不含num2本身）
数字之间的步长，以step为准（step默认为1）
如，range(5,10,2)取得的数据为[5,7,9]
"""
for x in range(10,100,10):
    print(x)
print()
for x in range(1,11):
    print(f"第{x}次")

# 小练习
num = 0
for x in range(1,100):
    if x % 2 == 0:
        num += 1
print(f"共有{num}个偶数")