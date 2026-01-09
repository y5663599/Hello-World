"""
- 单引号定义法
- 双音号定义法
- 三引号定义法
"""

# 使用单引号进行包围
name = '单引号'
print(name)
print(type(name))

# 使用双引号包围
name = "双引号"
print(name)
print(type(name))

# 使用三引号包围，写法与多行注释相同，支持换行操作
name = """
三
引
号
"""
print(name)
print(type(name))


# 如果我想要定义的字符串是包含引号自身呢？
# 1.单引号定义法，可以内含双引号
name = '"名字"'
print(name)
# 2.双引号定义法，可以内涵单引号
name = "'名字'"
print(name)
# 3.使用转移字符(\)将引号解除效用，变为普通字符串
name = "\"名\""
print(name)
name = '\'名\''
print(name)

# 好奇心测试
oblique = "\\"
print(oblique)