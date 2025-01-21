"""
今有邑方不知大小各中開門出北門三十步有木出西門七百五十步見木問邑方幾何
術曰令兩出門步數相乘因而四之為實開方除之即得邑方
荅曰 a里 
"""

"""
Suppose there is a square city whose size is unknown. 
From the center of the city, exiting the north gate and walking 30 bu, there is a tree.
Exiting the west gate and walking 750 bu, the tree is visible.
Question: what is the side length of the square city?

The procedure says: Multiply the number of steps exiting the two gates with each other.
Then multiply the result by 4, obtaining the dividend.
Take the square root of the dividend, and divide it, obtaining the side length of the city.

The answer says: *a* li.
"""

# 出北門三十步
北門步數 = 30

# 出西門七百五十步
西門步數 = 750

# 令兩出門步數相乘
實 = 北門步數 * 西門步數

# 因而四之，為實
實 = 4 * 實

# 開方除之，即得邑方
# Note: Square root is equivalent to raising to the power of 1/2
邑方 = 實 ** Fraction(1, 2)

# Convert from bu to li (1 li = 300 bu)
a = Fraction(邑方, 300)
"""
Code error: both arguments should be Rational instances"""
