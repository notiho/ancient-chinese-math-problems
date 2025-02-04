"""
今有句三尺，股四尺，問︰為弦幾何？
句股術曰：句股各自乘，并，而開方除之，即弦。又股自乘，以減弦自乘，其餘開方除之，即句。又句自乘，以減弦自乘，其餘開方除之，即股。
荅曰： a尺 。
"""

"""
Suppose there is a right triangle with a base (leg) of 3 chi and a height (leg) of 4 chi.
Question: how long is the hypotenuse?

The procedure for right triangles says: Multiply each of the base and height by itself, add them together, and extract the square root, obtaining the hypotenuse.
Additionally, multiply the height by itself, subtract the square of the hypotenuse, and extract the square root, obtaining the base.
Similarly, multiply the base by itself, subtract the square of the hypotenuse, and extract the square root, obtaining the height.

Answer: the hypotenuse is *a* chi.
"""

# 句三尺
句 = 3

# 股四尺
股 = 4

# 句股各自乘
句平方 = 句 * 句
股平方 = 股 * 股

# 并
和 = 句平方 + 股平方

# 而開方除之，即弦
a = Fraction(和).sqrt()  # Square root of the sum
"""
Code error: 'Fraction' object has no attribute 'sqrt'"""
