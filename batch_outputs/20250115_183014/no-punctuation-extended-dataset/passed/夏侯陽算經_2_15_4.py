"""
今有兵四萬八千六百二十五人人凡五日給鹽二升問一月幾何
術曰置兵數以二因之退二等得五日鹽數九百七十二斛五斗求一月數以六因之
答曰 a月 b斛
"""

"""
Suppose there are 48,625 soldiers, and every 5 days, they are given 2 sheng of salt.
Question: how much salt is needed for one month?

The procedure says: Place the number of soldiers. Multiply it by 2, then divide by 2 dou (1 dou = 10 sheng), obtaining the amount of salt for 5 days in hu and dou. 
To find the amount for one month, multiply it by 6.

Answer: *a* months and *b* hu.
"""

# 置兵數
兵數 = 48625

# 每五日給鹽二升
五日鹽升 = 2

# 以二因之 (乘以 2)
五日鹽總升 = 兵數 * 五日鹽升

# 退二等 (升轉為斛，1 斛 = 100 升)
五日鹽數 = Fraction(五日鹽總升, 100)

# 求一月數，以六因之 (乘以 6)
一月鹽數 = 6 * 五日鹽數

# 答案
a = 1  # 一個月
b = 一月鹽數  # 斛數
"""
"""
