"""
今有粟一十斗八升、五分升之二，欲為麥。問︰得幾何？
荅曰：為麥 a斗 。
"""

#----- content starts here -----
"""
Suppose there is 10 dou, 8 sheng, and 2/5 of a sheng of millet. It is desired to convert it into wheat.
Question: how much wheat does it make?

Answer: it makes *a* dou of wheat.
"""

from fractions import Fraction

# 粟一十斗八升、五分升之二
粟 = 10 + Fraction(8, 10) + Fraction(2, 50)  # Convert everything to dou (1 dou = 10 sheng)

# Conversion ratio from millet to wheat: 2 millet = 1 wheat
a = 粟 / 2  # Divide by 2 to get the equivalent amount of wheat in dou

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2439/250, Actual: 271/50"""
