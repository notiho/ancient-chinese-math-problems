"""
今有句三尺，股四尺，問︰為弦幾何？
句股術曰：句股各自乘，并，而開方除之，即弦。又股自乘，以減弦自乘，其餘開方除之，即句。又句自乘，以減弦自乘，其餘開方除之，即股。
荅曰： a(=5)尺 。
"""

#----- content starts here -----
"""
Suppose there is a right triangle with a base (leg) of 3 chi and a height (leg) of 4 chi.
Question: how long is the hypotenuse?

The procedure says: Multiply each of the base and height by itself, add them together, and take the square root of the result to obtain the hypotenuse.
Additionally, if the square of the height is subtracted from the square of the hypotenuse, the square root of the remainder gives the base.
Similarly, if the square of the base is subtracted from the square of the hypotenuse, the square root of the remainder gives the height.

Answer: *a*(=5) chi.
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
a = 和**(1/2) # 5#----- content ends here -----

"""
"""
