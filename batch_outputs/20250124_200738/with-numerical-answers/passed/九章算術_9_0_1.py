"""
今有句三尺，股四尺，問︰為弦幾何？
句股術曰：句股各自乘，并，而開方除之，即弦。又股自乘，以減弦自乘，其餘開方除之，即句。又句自乘，以減弦自乘，其餘開方除之，即股。
荅曰： a(=5)尺 。
"""

#----- content starts here -----
"""
Suppose there is a right triangle with a base (leg) of 3 chi and a height (leg) of 4 chi.
Question: how long is the hypotenuse?

The procedure for right triangles says: Multiply each of the base and height by itself.
Add these, and extract the square root, obtaining the hypotenuse.
Additionally, multiply the height by itself, subtract the square of the hypotenuse, and extract the square root, obtaining the base.
Similarly, multiply the base by itself, subtract the square of the hypotenuse, and extract the square root, obtaining the height.

Answer: *a*(=5) chi.
"""

# 句三尺
句 = 3

# 股四尺
股 = 4

# 句股各自乘
句自乘 = 句 * 句
股自乘 = 股 * 股

# 并
和 = 句自乘 + 股自乘

# 而開方除之，即弦
弦自乘 = 和
a = int(弦自乘**0.5)  # 5 chi#----- content ends here -----

"""
"""
