"""
今有粟七斗八升欲為豉問得幾何
術曰以粟求豉六十三之五十而一
荅曰為豉 a斗 
"""

"""
Suppose there are 7 dou and 8 sheng of millet. It is desired to turn it into fermented soybeans (chi).
Question: how much does one obtain?

The procedure says: when seeking fermented soybeans from millet, multiply by 63 and divide by 50.

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
豉升 = Fraction(豉, 50)

# Convert back to 斗 and 升
豉斗 = 豉升 // 10  # Whole number of 斗
豉剩餘升 = 豉升 % 10  # Remaining 升

a = Fraction(豉斗) + Fraction(豉剩餘升, 10)  # Final answer in 斗

"""
"""
