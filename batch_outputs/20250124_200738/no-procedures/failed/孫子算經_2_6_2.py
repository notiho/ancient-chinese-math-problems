"""
今有粟四斗五升。問：為糳米幾何？
答曰： a斗 。
"""

#----- content starts here -----
"""
Suppose there are 4 dou and 5 sheng of unhusked millet. It is desired to turn it into roughly husked millet.
Question: how much husked millet does it make?

Answer: it makes *a* dou.
"""

from fractions import Fraction

# 粟四斗五升
粟_斗 = 4
粟_升 = 5

# Convert everything to sheng (1 dou = 10 sheng)
總粟_升 = 粟_斗 * 10 + 粟_升

# Husked millet is 3/5 of the original unhusked millet
糳米_升 = Fraction(3, 5) * 總粟_升

# Convert back to dou and sheng
a_斗 = 糳米_升 // 10  # Whole dou
a_升 = 糳米_升 % 10   # Remaining sheng

# Final result
a = Fraction(a_斗) + Fraction(a_升, 10)

a  # Answer in dou#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 54/25, Actual: 27/10"""
