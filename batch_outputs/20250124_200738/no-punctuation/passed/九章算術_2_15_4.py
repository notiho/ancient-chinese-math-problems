"""
今有粟七斗八升欲為豉問得幾何
術曰以粟求豉六十三之五十而一
荅曰為豉 a斗 
"""

#----- content starts here -----
"""
Suppose there are 7 dou and 8 sheng of millet. It is desired to turn it into fermented soybeans (chi).
Question: how much does one obtain?

The procedure says: when seeking fermented soybeans from millet, multiply by 63 and divide by 50.

The answer says: it makes *a* dou of fermented soybeans.
"""

# 粟七斗八升
粟斗 = 7
粟升 = 8

# Convert to total sheng (1 dou = 10 sheng)
粟總升 = 粟斗 * 10 + 粟升

# 以粟求豉，六十三之
豉 = 63 * 粟總升

# 五十而一
豉總升 = Fraction(豉, 50)

# Convert back to dou and sheng
a斗 = 豉總升 // 10  # Integer part is the number of dou
a升 = 豉總升 % 10   # Remainder is the number of sheng

a = Fraction(a斗) + Fraction(a升, 10)  # Final result in dou
#----- content ends here -----

"""
"""
