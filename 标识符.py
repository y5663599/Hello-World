# 规则1：内容限定.字母,数字,下划线(_),各类语言文字(可能会有bug).不能以数字开头.
# 错误示范：1name = "张三"
#         name! = "李四"
_name = "张三"
n_ame = "李四"
nmae_1 = "王五"


# 规则2：大小写敏感
Mingzi = "名字"
mingzi = 666
print(Mingzi)
print(mingzi)


# 规则3：不可使用关键字
# 错误示例：class = 1
#         def = 2
Class = 1 #规则2