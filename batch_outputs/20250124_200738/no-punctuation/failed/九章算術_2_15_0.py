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

# Convert to 升 (1 斗 = 10 升)
粟 = 10 * 粟斗 + 粟升

# 以粟求豉，六十三之
豉 = 63 * 粟

# 五十而一
a = Fraction(豉, 50)

# Convert back to dou and sheng if needed
a斗 = a // 10  # Whole dou
a升 = a % 10   # Remaining sheng

a = (a斗, a升)  # Represent as (dou, sheng)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2457/250, Actual: (9, Fraction(207, 25))"""
