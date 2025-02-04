"""
今有絲一千五百二十五斤毎兩一百七十文問錢幾何
術曰先置絲數以二八因之以兩價乗之即得
答曰 a貫
"""

"""
Suppose there are 1525 jin of silk, with each liang costing 170 wen.
Question: how much money is it in total?

The procedure says: First, place the amount of silk. Multiply it by 28 (since 1 jin = 16 liang, and 16 * 10 = 160 liang per jin, so 1 jin = 28 liang). Then multiply it by the price per liang, obtaining the total amount.

Answer: it is *a* guan.
"""

from fractions import Fraction

# 絲一千五百二十五斤
絲數 = 1525

# 每兩一百七十文
每兩價 = 170

# 以二八因之 (1斤 = 16兩, 1兩 = 10文, so 1斤 = 28兩)
每斤兩數 = 28

# 以兩價乘之，即得
總文數 = 絲數 * 每斤兩數 * 每兩價

# 1貫 = 1000文
a = Fraction(總文數, 1000)
"""
Variable 'a' has wrong value. Expected: 4148, Actual: 7259"""
