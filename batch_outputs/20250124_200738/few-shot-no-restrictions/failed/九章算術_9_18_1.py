"""
今有邑方不知大小，各中開門。出北門三十步有木，出西門七百五十步見木。問︰邑方幾何？
術曰：令兩出門步數相乘，因而四之，為實。開方除之，即得邑方。
荅曰： a里 。
"""

#----- content starts here -----
"""
Suppose there is a square city (yi) of unknown size, with gates at the middle of each side.
From the north gate, walking 30 bu, there is a tree.
From the west gate, walking 750 bu, there is another tree.
Question: what is the side length of the square city?

The procedure says: Multiply the distances walked from the two gates, then multiply the result by 4, obtaining the dividend.
Take the square root of the result, and that is the side length of the square city.

Answer: *a* li.
"""

from fractions import Fraction
import math

# 出北門三十步
北門步數 = 30

# 出西門七百五十步
西門步數 = 750

# 令兩出門步數相乘
步數積 = 北門步數 * 西門步數

# 因而四之，為實
實 = 4 * 步數積

# 開方除之，即得邑方
邑方步 = math.sqrt(實)

# 1 里 = 300 步
a = Fraction(邑方步, 300)  # Convert to li

a#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
