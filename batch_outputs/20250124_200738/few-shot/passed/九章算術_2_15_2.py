"""
今有粟七斗八升，欲為豉。問︰得幾何？
術曰：以粟求豉，六十三之，五十而一。
荅曰：為豉 a斗 。
"""

#----- content starts here -----
"""
Suppose there is 7 dou and 8 sheng of millet. It is desired to turn it into fermented soybeans (chi).
Question: how much does one obtain?

The procedure says: when seeking fermented soybeans using millet, multiply by 63 and divide by 50.

The answer says: it makes *a* dou of fermented soybeans.
"""

# 粟七斗八升
粟斗 = 7
粟升 = 8

# Convert everything to 升 (1 斗 = 10 升)
粟 = 10 * 粟斗 + 粟升

# 以粟求豉，六十三之
豉 = 63 * 粟

# 五十而一
豉斗 = Fraction(豉, 50)

# Convert back to 斗
a = Fraction(豉斗, 10)  # Result in dou#----- content ends here -----

"""
"""
