# 演示for循环的基础语法
"""
语法格式：
for 临时变量 in 待处理的数据集(序列类型):
    循环满足条件时执行的代码

语法中：待处理的数据集，严格来说称之为：序列类型
序列类型指，其内容可以一个个依次取出的一种类型，包括：
- 字符串
- 列表
- 元组
- 等
"""

name = "hello"
# for 变量 in 被处理的数据:
for x in name:
    # 将name的内容挨个取出，赋予x临时变量
    # 就可以在循环体内对x进行处理了
    print(x)
    # for循环是将字符串的内容依次取出。所以for循环也被称为：遍历循环

"""
- 与while循环不同，for循环无法定义循环条件
- 只能从被处理的数据集中，依次取出内容进行处理
- 所以，理论上Python的for循环无法构建无限循环
"""

# 小练习：name中有几个a
name = "wwwawaa wwa a waw wwa"
num = 0
for x in name:
    if x == "a":
        num += 1
        print(f"发现第{num}个a")
print(f"一共{num}个a")