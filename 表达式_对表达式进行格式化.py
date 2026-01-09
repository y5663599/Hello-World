"""
表达式是什么？
- 表达式就是一个具有明确结果的代码语句，如1 + 1、type("字符串")、3 * 5等
- 在变量定义的时候，如age = 11 + 11，等号右侧的就是表达式，也就是有具体的结果，
  将结果赋值给了等号左侧的变量
如何格式化表达式？
- f"{表达式}"
- "%s,%d,%f" % (表达式,表达式,表达式)
"""
print("1 * 1 = %d" % (1 * 1))
print(f"1 * 2 = {1 * 2}")
print("字符串在python中的类型是%s" % type("字符串"))

# 小练习
name = "护理"
stockPrice = 19.99
stockCode = "003032"
stockPriceDailyGrowthFactor = 1.2
growthDays = 7

print(f"公司:{name},股票代码:{stockCode},当前股价:{stockPrice}")
print("每日增长系数是：%.1f,经过%d天的增]长后，股票达到了%.2f" % (stockPriceDailyGrowthFactor,growthDays,(stockPrice * stockPriceDailyGrowthFactor ** growthDays)))