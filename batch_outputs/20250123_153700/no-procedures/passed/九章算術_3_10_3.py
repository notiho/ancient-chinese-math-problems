"""
今有絲一斤價直三百四十五。今有絲七兩一十二銖，問︰得錢幾何？
荅曰： a錢 。
"""

"""
Suppose there is 1 jin of silk worth 345 qian. Now, there is 7 liang and 12 zhu of silk.
Question: how much money is it worth?

Answer: it is worth *a* qian.
"""

# 1 jin = 16 liang
# 1 liang = 24 zhu

# Total value of 1 jin of silk
value_per_jin = 345

# Convert 7 liang and 12 zhu into a fraction of a jin
silk_weight = Fraction(7, 16) + Fraction(12, 16 * 24)

# Calculate the value of the given silk
a = silk_weight * value_per_jin
"""
"""
