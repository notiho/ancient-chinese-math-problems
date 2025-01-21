"""
今有邑方不知大小，各中開門。出北門三十步有木，出西門七百五十步見木。問︰邑方幾何？
術曰：令兩出門步數相乘，因而四之，為實。開方除之，即得邑方。
荅曰： a里 。
"""

"""
Suppose there is a square city whose size is unknown. Each side of the city has a gate in the middle.
Walking 30 bu north from the north gate, one encounters a tree.
Walking 750 bu west from the west gate, one encounters another tree.
Question: what is the side length of the square city?

The procedure says: Multiply the distances walked from the two gates.
Then multiply the result by 4, obtaining the dividend.
Take the square root of the dividend, obtaining the side length of the square city.

Answer: *a* li.
"""

# 出北門三十步有木
北門步數 = 30

# 出西門七百五十步見木
西門步數 = 750

# 令兩出門步數相乘
實 = 北門步數 * 西門步數

# 因而四之，為實
實 = 4 * 實

# 開方除之，即得邑方
# Since Python does not have a built-in square root function without external libraries, we use exponentiation.
邑方 = 實 ** Fraction(1, 2)

# Convert from bu to li (1 li = 300 bu)
a = Fraction(邑方, 300)
"""
Code error: both arguments should be Rational instances"""
