"""
今有邑方不知大小，各中開門。出北門三十步有木，出西門七百五十步見木。問︰邑方幾何？
術曰：令兩出門步數相乘，因而四之，為實。開方除之，即得邑方。
荅曰： a(=1)里 。
"""

#----- content starts here -----
"""
Suppose there is a square city whose size is unknown, with gates in the middle of each side.
Exiting the north gate and walking 30 bu, there is a tree.
Exiting the west gate and walking 750 bu, there is a tree.
Question: what is the side length of the square city?

The procedure says: Multiply the number of steps from the two gates, then multiply the result by 4 to obtain the dividend.
Take the square root of the dividend to obtain the side length of the square city.

Answer: *a*(=1) li.
"""

from fractions import Fraction

# 出北門三十步
北門步數 = 30

# 出西門七百五十步
西門步數 = 750

# 令兩出門步數相乘
步數相乘 = 北門步數 * 西門步數

# 因而四之，為實
實 = 4 * 步數相乘

# 開方除之，即得邑方
# Since the square root of 4 * 30 * 750 = 90000 is 300, and 300 bu = 1 li:
a = Fraction(300, 300) # 1 li#----- content ends here -----

"""
"""
