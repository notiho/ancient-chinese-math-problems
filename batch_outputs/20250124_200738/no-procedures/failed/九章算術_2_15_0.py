"""
今有粟七斗八升，欲為豉。問︰得幾何？
荅曰：為豉 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 7 dou and 8 sheng of millet. It is desired to turn it into fermented soybeans (chi).
Question: how much fermented soybeans does it make?

The answer says: it makes *a* dou.
"""

# 粟七斗八升
# Convert everything to sheng (1 dou = 10 sheng)
粟 = 7 * 10 + 8  # 7 dou and 8 sheng = 78 sheng

# To make fermented soybeans, millet reduces to 2/3 of its original volume
豉 = Fraction(2, 3) * 粟

# Convert back to dou (1 dou = 10 sheng)
a = Fraction(豉, 10)

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2457/250, Actual: 26/5"""
