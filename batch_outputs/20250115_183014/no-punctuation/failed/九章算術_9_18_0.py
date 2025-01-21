"""
今有邑方不知大小各中開門出北門三十步有木出西門七百五十步見木問邑方幾何
術曰令兩出門步數相乘因而四之為實開方除之即得邑方
荅曰 a里 
"""

"""
Suppose there is a square city whose size is unknown. 
From the center of the city, one exits the north gate and walks 30 bu to find a tree. 
Exiting the west gate, one walks 750 bu to see the same tree.
Question: what is the side length of the square city?

The procedure says: Multiply the step counts from the two gates by each other, then multiply the result by 4 to obtain the dividend.
Take the square root of the dividend, and divide it to obtain the side length of the city.

Answer: *a* li.
"""

# 出北門三十步
北門步數 = 30

# 出西門七百五十步
西門步數 = 750

# 令兩出門步數相乘
相乘 = 北門步數 * 西門步數

# 因而四之，為實
實 = 4 * 相乘

# 開方 (square root)
邑方步 = 實**0.5

# 1 里 = 300 步, convert to 里
a = Fraction(邑方步, 300)
"""
Code error: both arguments should be Rational instances"""
