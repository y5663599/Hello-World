"""
某公司，账户余额1W元，给20名员工发工资
- 员工编号1~20，从编号1开始，依次领取工资，每人可领取1000元
- 领工资时，财务判断员工绩效分(1~10)(随机生成)，低于5，不发工资，下一位
- 工资发完，结束
"""
# 课前
import random
# money = 10000
# for n in range(1,21):
#     num = random.randint(1,10)
#     while money > 0:
#         if num < 5:
#             print(f"员工{n}，绩效分{num}，低于5，不发工资")
#             break
#         else:
#             money -= 1000
#             print(f"向员工{n}发放工资1000，账户余额还剩余{money}")
#             break
# print("工资发完了")

# 课后
money = 10000
for n in range(1,21):
    num = random.randint(1,10)
    if num < 5:
        print(f"员工{n}，绩效分{num}，低于5，不发工资")
        continue
    if money > 0:
        money -= 1000
        print(f"向员工{n}发放工资1000，账户余额还剩余{money}")
    else:
        print("工资发完了")
        break
