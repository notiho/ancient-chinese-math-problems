"""
今有絲一千五百二十五斤毎兩一百七十文問錢幾何
術曰先置絲數以二八因之以兩價乗之即得
答曰 a貫
"""

"""
Suppose there is 1525 jin of silk, with each liang priced at 170 wen.
Question: how much money is it in total?

The procedure says: First, place the amount of silk. Multiply it by 28 (since 1 jin = 16 liang, and 1 jin = 16 * 10 = 160 liang, thus 28 is used for conversion). Then multiply it by the price per liang. The result is obtained.

Answer: *a* guan.
"""

# 絲一千五百二十五斤
絲數 = 1525

# 每兩一百七十文
每兩價 = 170

# 以二八因之 (1斤 = 16兩, 16兩 = 16 * 10 = 160文, thus 28 is used for conversion)
絲數_兩 = 絲數 * 16

# 以兩價乘之即得
總文數 = 絲數_兩 * 每兩價

# Convert to 貫 (1貫 = 1000文)
a = Fraction(總文數, 1000)
"""
"""
