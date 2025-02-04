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
粟 = 9 + Fraction(8, 10)  # Convert 8 sheng to dou (1 dou = 10 sheng)

# 御飯 conversion: multiply by 2 and divide by 3
a = Fraction(2 * 粟, 3)  # Result in dou#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1029/125, Actual: 98/15"""
