"""
今有句三尺股四尺問為弦幾何
句股術曰句股各自乘并而開方除之即弦又股自乘以減弦自乘其餘開方除之即句又句自乘以減弦自乘其餘開方除之即股
荅曰 a尺 
"""

#----- content starts here -----
"""
Suppose there is a right triangle with one leg (ju) of 3 chi and the other leg (gu) of 4 chi.
Question: how long is the hypotenuse (xian)?

The procedure for right triangles says: Multiply each of the legs (ju and gu) by itself, add them together, and take the square root. This gives the hypotenuse.
Additionally:
- Multiply the other leg (gu) by itself, subtract the square of the hypotenuse, and take the square root. This gives the first leg (ju).
- Multiply the first leg (ju) by itself, subtract the square of the hypotenuse, and take the square root. This gives the other leg (gu).

The answer says: *a* chi.
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
a = Fraction(弦平方).sqrt()  # Taking the square root of the sum#----- content ends here -----

"""
Code error: 'Fraction' object has no attribute 'sqrt'"""
