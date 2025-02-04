"""
今有粟九斗八升，欲為御飯。問︰得幾何？
荅曰：為御飯 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 9 dou and 8 sheng of millet. It is desired to turn it into cooked rice.
Question: how much cooked rice does it make?

Answer: it makes *a* dou of cooked rice.
"""

# 粟九斗八升
粟_斗 = 9
粟_升 = 8

# Convert everything to sheng (1 dou = 10 sheng)
total_sheng = 粟_斗 * 10 + 粟_升

# To make cooked rice, millet is multiplied by 2/3
cooked_rice_sheng = Fraction(2, 3) * total_sheng

# Convert cooked rice back to dou and sheng
a_斗 = cooked_rice_sheng // 10  # Whole dou
a_升 = cooked_rice_sheng % 10   # Remaining sheng

# Final answer
a = Fraction(cooked_rice_sheng, 10)  # Represent as dou
#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1029/125, Actual: 98/15"""
