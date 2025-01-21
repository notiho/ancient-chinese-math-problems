"""
今有句三尺股四尺問為弦幾何
句股術曰句股各自乘并而開方除之即弦又股自乘以減弦自乘其餘開方除之即句又句自乘以減弦自乘其餘開方除之即股
荅曰 a尺 
"""

"""
Suppose there is a right triangle with a base (ju) of 3 chi and a height (gu) of 4 chi.
Question: how long is the hypotenuse (xian)?

The procedure says: Multiply the base and the height by themselves, add them together, and take the square root. This gives the hypotenuse.
Also, multiply the height by itself, subtract the square of the hypotenuse, and take the square root. This gives the base.
Also, multiply the base by itself, subtract the square of the hypotenuse, and take the square root. This gives the height.

Answer: the hypotenuse is *a* chi.
"""

# 句三尺
句 = 3

# 股四尺
股 = 4

# 句股各自乘
句平方 = 句 * 句
股平方 = 股 * 股

# 并而開方除之，即弦
弦平方 = 句平方 + 股平方
a = Fraction(弦平方).sqrt()  # Square root of the hypotenuse squared
"""
Code error: 'Fraction' object has no attribute 'sqrt'"""
