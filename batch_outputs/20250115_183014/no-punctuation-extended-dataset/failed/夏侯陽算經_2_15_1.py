"""
今有兵四萬八千六百二十五人人凡五日給鹽二升問一月幾何
術曰置兵數以二因之退二等得五日鹽數九百七十二斛五斗求一月數以六因之
答曰 a月 b斛
"""

"""
Suppose there are 48,625 soldiers. Every 5 days, they are given 2 sheng of salt each.
Question: how much salt is needed for one month?

The procedure says: Place the number of soldiers. Multiply it by 2, then divide by 2 dou (10 sheng per dou), obtaining the amount of salt for 5 days in hu and dou. 
To find the amount for one month, multiply it by 6.

Answer: *a* months and *b* hu.
"""

from fractions import Fraction

# 兵四萬八千六百二十五人
兵數 = 48625

# 五日給鹽二升
五日鹽每人 = 2  # 升

# 置兵數，以二因之
總鹽升 = 兵數 * 五日鹽每人

# 退二等 (1斗 = 10升, 1斛 = 10斗)
總鹽斗 = Fraction(總鹽升, 10)  # 轉為斗
總鹽斛 = Fraction(總鹽斗, 10)  # 轉為斛

# 得五日鹽數
五日鹽數 = 總鹽斛

# 求一月數，以六因之
一月鹽數 = 五日鹽數 * 6

# 分解為整數月和剩餘斛
a = 0  # 月數 (since the problem only asks for one month)
b = 一月鹽數  # 斛數
"""
Variable 'a' has wrong value. Expected: 1, Actual: 0"""
