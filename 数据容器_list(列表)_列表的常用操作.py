#方法概念：
# 在python中，如果将函数定义为class(类)的成员，那么函数会被称之为：方法
"""
函数
def add(x,y):
    return x+y

方法
class Student():
    def add(self,x,y):
        return x+y

函数的使用
num = add(1,2)
方法的使用
student = Student() #先获得方法所在的class类对象
num = student.add(3,4) # . 后接函数名就可以正常使用
"""
#list(列表)中提供了一系列方法
# list.方法


# list列表的常用操作
myList = ["字符串0","字符串1","字符串2"]

# 查找某元素在列表中的下标索引的功能
# 列表.index(元素)
# index就是列表对象(变量)内置的方法
index = myList.index("字符串1")
print(index)
# 没有会报错
# index = myList.index("何意味")
# print(index)


# 修改特定位置(索引)的元素值
# 语法：列表[下标] = 值
# 使用如上语法，直接对指定下标（正向、反向下标均可）的值进行：重新赋值（修改）
# 正向下标
my_list = [1,2,3]
my_list[0] = 6
print(my_list)
# 反向下标
myList[-1] = "何意味2"
print(myList)


# 插入元素
# 语法：列表.insert(下标,元素)，在指定的下标位置，插入指定的元素。      insert方法
myList.insert(0,'何意味0')
print(myList)


# 追加元素
# 语法：列表.append(元素),将指定元素，追加到列表的尾部
myList.append("意意味味")
print(myList)

# 想要追加多个元素？
# 追加元素2
# 语法：列表.extend(其他数据容器),将其他数据容器的内容取出，依次追加到列表尾部
myList.extend(['意味意味','味意味意',114514])
print(myList)


# 删除元素
# 语法1：del列表[下标]        关键字del
del myList[0]
print(myList)
# 语法2：列表.pop(下标)      pop方法：返回并移除元素
pop = myList.pop(0)
print(pop)
print(myList)

# 删除某元素在列表中的第一个匹配项
# 列表.remove(元素)
mylist = [1,6,5,6]
mylist.remove(6)
print(mylist) # 删除第一个匹配项，输出为1,5,6
myList.remove("意意味味")
print(myList)


# 清空列表
# 语法：列表.clear()
myList.clear()
print(myList)   #输出棍母


#统计某个元素在列表中的数量
# 语法：列表.count(元素)
my_list = [1,2,3,3,3,3,3]
print(my_list.count(3))


# 统计列表内有多少元素
# 语法：len(列表)
print(len(my_list))






"""
列表
- 可以容纳多个元素(上限为2**63-1、9223372036854775807个)
- 可以容纳不同类型的元素(混装)
- 数据是有序存储的(有下标序号)
- 允许重复数据存在
- 可以修改(增加或删除元素等)
"""