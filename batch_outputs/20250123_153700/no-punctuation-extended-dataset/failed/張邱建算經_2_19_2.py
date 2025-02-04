"""
今有田方一百二十一步欲以為圓問周幾何
術曰方自相乗又以十二乗之為實開方除之即得
答曰 a步
"""

"""
Suppose there is a square field with a side length of 121 bu. It is desired to make it into a circular field.
Question: what is the circumference of the circular field?

The procedure says: Square the side length of the square field. 
Then multiply it by 12, obtaining the dividend.
Extract the square root, and divide it by the divisor (π approximation), obtaining the circumference.

Answer: *a* bu.
"""

# 田方一百二十一步
方 = 121

# 方自相乘
方積 = 方 * 方

# 又以十二乘之，為實
實 = 12 * 方積

# 開方 (square root)
# Since we cannot use external libraries, we approximate the square root manually.
def 開方(x):
    guess = x / 2
    for _ in range(20):  # Perform 20 iterations for approximation
        guess = (guess + x / guess) / 2
    return guess

實開方 = 開方(實)

# 除之 (π approximation: 3.141592653589793)
π = 3.141592653589793
a = Fraction(實開方, π)

# Note: The result is expressed as a fraction for exactness.
"""
Code error: both arguments should be Rational instances"""
