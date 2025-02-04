"""
今有邑方不知大小，各中開門。出北門三十步有木，出西門七百五十步見木。問︰邑方幾何？
術曰：令兩出門步數相乘，因而四之，為實。開方除之，即得邑方。
荅曰： a里 。
"""

"""
Suppose there is a square city whose size is unknown. Each side of the city has a gate in the middle.
Walking 30 bu out of the north gate, there is a tree. Walking 750 bu out of the west gate, there is another tree.
Question: what is the side length of the square city?

The procedure says: Multiply the distances walked out of the two gates, then multiply the result by 4, obtaining the dividend.
Take the square root of the dividend, and this gives the side length of the square city.

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
# Since we cannot use external functions, we manually compute the square root using an iterative method.
# Here, we use the Babylonian method for square root approximation.

def 開方(x):
    guess = x / 2  # Initial guess
    for _ in range(20):  # Perform 20 iterations for approximation
        guess = (guess + x / guess) / 2
    return guess

邑方步 = 開方(實)

# Convert from bu to li (1 li = 300 bu)
a = Fraction(邑方步, 300)
"""
Code error: both arguments should be Rational instances"""
