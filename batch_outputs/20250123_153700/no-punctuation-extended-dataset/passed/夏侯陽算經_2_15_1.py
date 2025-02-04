"""
今有兵四萬八千六百二十五人人凡五日給鹽二升問一月幾何
術曰置兵數以二因之退二等得五日鹽數九百七十二斛五斗求一月數以六因之
答曰一月 a斛
"""

"""
Suppose there are 48,625 soldiers. Every 5 days, they are given 2 sheng of salt.
Question: how much salt is needed for one month?

The procedure says: Place the number of soldiers, multiply it by 2, and divide it by 2 dou per hu (retreating two ranks).
This gives the amount of salt for 5 days, which is 972 hu and 5 dou.
To find the amount for one month, multiply it by 6.

Answer: for one month, it is *a* hu.
"""

from fractions import Fraction

# 兵四萬八千六百二十五人
兵數 = 48625

# 凡五日給鹽二升
五日鹽升 = 2

# 置兵數，以二因之
五日鹽總升 = 兵數 * 五日鹽升

# 退二等 (1 hu = 10 dou, 1 dou = 10 sheng, so divide by 100 to convert sheng to hu)
五日鹽數 = Fraction(五日鹽總升, 100)

# 求一月數，以六因之 (1 month = 30 days, so 6 sets of 5 days)
一月鹽數 = 6 * 五日鹽數

a = 一月鹽數

"""
"""
