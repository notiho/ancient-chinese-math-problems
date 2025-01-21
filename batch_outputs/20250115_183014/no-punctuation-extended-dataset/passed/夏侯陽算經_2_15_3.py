"""
今有兵四萬八千六百二十五人人凡五日給鹽二升問一月幾何
術曰置兵數以二因之退二等得五日鹽數九百七十二斛五斗求一月數以六因之
答曰 a月 b斛
"""

"""
Suppose there are 48,625 soldiers. Every 5 days, they are given 2 sheng of salt each.
Question: how much salt is needed for one month?

The procedure says: Place the number of soldiers. Multiply it by 2. Divide by 2 dou per hu, obtaining the amount of salt for 5 days, which is 972 hu and 5 dou.
To find the amount for one month, multiply by 6.

Answer: *a* months and *b* hu.
"""

# 兵四萬八千六百二十五人
兵數 = 48625

# 凡五日給鹽二升
五日鹽每人 = 2  # 升

# 置兵數，以二因之
五日總鹽升 = 兵數 * 五日鹽每人

# 退二等（1斛 = 10斗, 1斗 = 10升, so 1斛 = 100升）
五日總鹽斛 = Fraction(五日總鹽升, 100)

# 得五日鹽數
五日鹽數 = 五日總鹽斛

# 求一月數，以六因之
一月鹽數 = 五日鹽數 * 6

# 分解成月和斛
a = 1  # 一月
b = 一月鹽數  # 斛

a, b
"""
"""
