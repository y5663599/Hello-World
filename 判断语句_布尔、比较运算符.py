"""
演示布尔类型的定义
以及比较运算符的应用
"""

# 定义变量存储布尔类型的数据。True为真、False为假(注意搜字母大写)
bool1 = True
bool2 = False
print(f"bool1的内容是：{bool1}，它的类型是{type(bool1)}")
print(f"bool2的内容是：{bool2}，它的类型是{type(bool2)}")
# 比较运算符的使用
# ==判断是否相等,!=判断是否不相等,>判断是否大于,<判断是否小于,>=判断是否大于等于,<=判断是否小于等于

# 演示是否相等的比较运算
num1 = 10
num2 = 10
print(f"10 == 10的结果是：{num1 == num2}")

num1 = 10
num2 = 15
print(f"10 != 15的结果是：{num1 != num2}")

name1 = "小明"
name2 = "小王"
print(f"小明 == 小王的结果是：{name1 == name2}")


#演示大于、小于、大于等于、小于等于的比较运算
num1 = 10
num2 = 5
print(f"10 > 5的结果是：{num1 > num2}")
print(f"10 < 5的结果是：{num1 < num2}")

num1 = 10
num2 = 11
print(f"10 >= 11的结果是：{num1 >= num2}")
print(f"10 <= 11的结果是：{num1 <= num2}")