# 通过注释对函数解释说明

def num(x,y):
    """
    函数的说明
    :param x:形参x的说明
    :param y:形参y的说明
    :return:返回值的说明
    """
    result = x + y # 函数体
    return result  # 返回值

def add(x,y):
    """
    add函数可以接受2个参数，进行两数相加的功能
    :param x:形参x表示相加的其中一个数字
    :param y:同上
    :return:返回2个参数相加的结果
    """
    result2 = x + y
    return result2

add(5,6)