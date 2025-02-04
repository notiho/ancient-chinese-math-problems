"""
今有粟八斗六升，欲為鑿飯。問︰得幾何？
荅曰：為鑿飯 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 8 dou and 6 sheng of millet. It is desired to turn it into cooked rice.
Question: how much cooked rice does it make?

Answer: it makes *a* dou of cooked rice.
"""

from fractions import Fraction

# 粟八斗六升
粟 = 8 + Fraction(6, 10)  # 1 dou = 10 sheng, so 6 sheng = 6/10 dou

# To convert millet to cooked rice, multiply by 2/3
a = 粟 * Fraction(2, 3)

# Result: a is the amount of cooked rice in dou
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1032/125, Actual: 86/15"""
