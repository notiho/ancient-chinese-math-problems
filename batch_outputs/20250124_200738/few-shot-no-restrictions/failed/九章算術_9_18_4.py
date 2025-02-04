"""
今有邑方不知大小，各中開門。出北門三十步有木，出西門七百五十步見木。問︰邑方幾何？
術曰：令兩出門步數相乘，因而四之，為實。開方除之，即得邑方。
荅曰： a里 。
"""

#----- content starts here -----
"""
Suppose there is a square city, the size of which is unknown, with gates at the center of each side.
Exiting the north gate and walking 30 bu, one encounters a tree.
Exiting the west gate and walking 750 bu, one encounters another tree.
Question: what is the side length of the square city?

The procedure says: Multiply the distances walked from the two gates, then multiply the result by 4, obtaining the dividend.
Take the square root of the dividend, and this is the side length of the square city.

Answer: *a* li.
"""

from fractions import Fraction
import math

# 出北門三十步有木
北門步數 = 30

# 出西門七百五十步見木
西門步數 = 750

# 令兩出門步數相乘
步數積 = 北門步數 * 西門步數

# 因而四之，為實
實 = 4 * 步數積

# 開方除之，即得邑方
邑方步 = math.sqrt(實)

# Convert bu to li (1 li = 300 bu)
a = Fraction(邑方步, 300)

a#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
