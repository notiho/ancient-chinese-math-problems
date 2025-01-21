"""
今有兵四萬八千六百二十五人人凡五日給鹽二升問一月幾何
術曰置兵數以二因之退二等得五日鹽數九百七十二斛五斗求一月數以六因之
答曰 a月 b斛
"""

"""
Suppose there are 48,625 soldiers. Every 5 days, they are given 2 sheng of salt each.
Question: how much salt is needed for one month?

The procedure says: Place the number of soldiers. Multiply it by 2, then divide by 2 dou per hu (to convert to hu), obtaining the amount of salt for 5 days: 972 hu and 5 dou.
To find the amount for one month, multiply it by 6.

Answer: *a* months and *b* hu.
"""

# 兵四萬八千六百二十五人
兵數 = 48625

# 凡五日給鹽二升
五日鹽每人 = 2  # 升

# 置兵數，以二因之
五日總鹽升 = 兵數 * 五日鹽每人

# 退二等 (1 斛 = 10 斗, 1 斗 = 10 升, so 1 斛 = 100 升)
五日總鹽斛 = Fraction(五日總鹽升, 100)

# 求一月數，以六因之 (1 月 = 6 個 5 日)
一月總鹽斛 = 6 * 五日總鹽斛

# 分解為整月和剩餘斛
a = 1  # 一個月
b = 一月總鹽斛  # 總斛數
"""
"""
