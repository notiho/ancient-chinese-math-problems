"""
今有粟七斗九升，欲為御米。問︰得幾何？
荅曰：為御米 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 7 dou and 9 sheng of millet. It is desired to turn it into polished rice.
Question: how much polished rice does one obtain?

Answer: it makes *a* dou of polished rice.
"""

# 粟七斗九升
粟斗 = 7
粟升 = 9

# Convert everything to sheng (1 dou = 10 sheng)
粟總升 = 粟斗 * 10 + 粟升

# Polished rice is obtained by multiplying the total millet by 2/3
御米總升 = Fraction(2 * 粟總升, 3)

# Convert back to dou and sheng
a斗 = 御米總升 // 10  # Whole dou
a升 = 御米總升 % 10   # Remaining sheng

# Final result
a = Fraction(a斗) + Fraction(a升, 10)  # Represent as a single fraction in dou units#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1659/500, Actual: 79/15"""
