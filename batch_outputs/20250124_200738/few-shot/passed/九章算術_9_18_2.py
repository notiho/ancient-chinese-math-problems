"""
今有邑方不知大小，各中開門。出北門三十步有木，出西門七百五十步見木。問︰邑方幾何？
術曰：令兩出門步數相乘，因而四之，為實。開方除之，即得邑方。
荅曰： a里 。
"""

#----- content starts here -----
"""
Suppose there is a square city whose size is unknown. Each side has a gate in the middle.
Walking 30 bu north from the north gate, there is a tree.
Walking 750 bu west from the west gate, there is another tree.
Question: what is the side length of the square city?

The procedure says: Multiply the number of steps from the two gates, then multiply the result by 4, obtaining the dividend.
Take the square root of the dividend, obtaining the side length of the square city.

Answer: *a* li.
"""

from fractions import Fraction

# 出北門三十步有木
北門步數 = 30

# 出西門七百五十步見木
西門步數 = 750

# 令兩出門步數相乘
實 = 北門步數 * 西門步數

# 因而四之
實 = 4 * 實

# 開方除之，即得邑方
# Since we cannot directly compute square roots with the Fraction class, we approximate:
# Convert 实 to a float for square root calculation, then convert back to Fraction
邑方 = Fraction(int(實**0.5))

# Convert from bu to li (1 li = 300 bu)
a = Fraction(邑方, 300)#----- content ends here -----

"""
"""
