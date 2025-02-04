"""
今有粟五斗五升，欲為飧。問︰得幾何？
荅曰：為飧 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 5 dou and 5 sheng of millet. It is desired to turn it into cooked millet (food).
Question: how much cooked millet does it make?

The answer says: it makes *a* dou of cooked millet.
"""

from fractions import Fraction

# 粟五斗五升
粟_斗 = 5
粟_升 = 5

# Convert everything to sheng (1 dou = 10 sheng)
粟_總升 = 粟_斗 * 10 + 粟_升

# Cooked millet is 2/3 of the raw millet
飧_總升 = Fraction(2, 3) * 粟_總升

# Convert back to dou and sheng
a_斗 = 飧_總升 // 10  # Whole dou
a_升 = 飧_總升 % 10   # Remaining sheng

# Final result
a = Fraction(a_斗) + Fraction(a_升, 10)  # Represent as dou with fractional part

a  # Output the result in dou#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 99/10, Actual: 11/3"""
