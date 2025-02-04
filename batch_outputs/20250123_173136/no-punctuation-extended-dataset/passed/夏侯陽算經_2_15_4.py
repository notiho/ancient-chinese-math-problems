"""
今有兵四萬八千六百二十五人人凡五日給鹽二升問一月幾何
術曰置兵數以二因之退二等得五日鹽數九百七十二斛五斗求一月數以六因之
答曰一月 a斛
"""

"""
Suppose there are 48,625 soldiers, and every 5 days, they are given 2 sheng of salt.
Question: how much salt is needed for one month?

The procedure says: Place the number of soldiers. Multiply it by 2. Divide it by 2 dou (1 dou = 10 sheng), obtaining the amount of salt for 5 days, which is 972 hu and 5 dou.
To find the amount for one month, multiply it by 6.

Answer: for one month, it is *a* hu.
"""

# 兵四萬八千六百二十五人
兵數 = 48625

# 凡五日給鹽二升
五日鹽升 = 2

# 置兵數，以二因之
五日鹽總升 = 兵數 * 五日鹽升

# 退二等 (1斗 = 10升, 1斛 = 10斗)
五日鹽總斗 = Fraction(五日鹽總升, 10)
五日鹽總斛 = Fraction(五日鹽總斗, 10)

# 求一月數，以六因之 (1月 = 30日, 30日 = 6個5日)
一月鹽總斛 = 6 * 五日鹽總斛

a = 一月鹽總斛
"""
"""
