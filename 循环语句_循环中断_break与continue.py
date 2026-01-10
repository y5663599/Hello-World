# 演示循环中断语句 continue
# for i in range(5):
#     print(f"第{i}")
#     continue # 停止本次循环重新开始循环
#     print(f"第{i}")

# 演示 continue 的嵌套应用
# for x in range(1,6):
#     print(f"一号第{x}次触发")
#     for y in range(1,6):
#         print(f"二号第{y+(x-1)*5}次触发")
#         continue
#         print("孩子们我是三号，whatCanISay")
#     print(f"四号第{x}次触发")

# 演示 break
for u in range(1,6):
    for n in range(1,6):
        print("输出1")
        break
    print("输出2")