"""
今有兵四萬八千六百二十五人人凡五日給鹽二升問一月幾何
術曰置兵數以二因之退二等得五日鹽數九百七十二斛五斗求一月數以六因之
答曰 a月 b斛
"""

"""
Suppose there are 48,625 soldiers. Every 5 days, they are given 2 sheng of salt each.
Question: how much salt is needed for one month?

The procedure says: Place the number of soldiers. Multiply it by 2. Divide by 2 dou per hu, obtaining the amount of salt for 5 days as 972 hu and 5 dou.
To find the amount for one month, multiply it by 6.

Answer: *a* months and *b* hu.
"""

# 兵四萬八千六百二十五人
兵數 = 48625

# 凡五日給鹽二升
每日鹽 = 2

# 置兵數，以二因之
五日鹽升 = 兵數 * 每日鹽

# 退二等 (1 hu = 10 dou, 1 dou = 10 sheng)
五日鹽斗 = 五日鹽升 / 10
五日鹽斛 = 五日鹽斗 / 10

# 得五日鹽數
五日鹽 = Fraction(五日鹽升, 100)

# 求一月數，以六因之
一月鹽 = 五日鹽 * 6

# 分解為整數部分和分數部分
a = 1  # 一月 (1 month)
b = 一月鹽  # Total hu needed for one month
"""
"""
