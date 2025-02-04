"""
今有弦五尺，句三尺，問︰為股幾何？
句股術曰：句股各自乘，并，而開方除之，即弦。又股自乘，以減弦自乘，其餘開方除之，即句。又句自乘，以減弦自乘，其餘開方除之，即股。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a hypotenuse (弦) of 5 chi and one leg (句) of 3 chi.
Question: how long is the other leg (股)?

The procedure for right triangles says:
1. Each leg (句 and 股) is multiplied by itself, then added together, and the square root is taken to obtain the hypotenuse (弦).
2. Multiply the other leg (股) by itself, subtract it from the square of the hypotenuse (弦), and take the square root to obtain the given leg (句).
3. Multiply the given leg (句) by itself, subtract it from the square of the hypotenuse (弦), and take the square root to obtain the other leg (股).

Answer: *a* chi.
"""

# 弦五尺
弦 = 5

# 句三尺
句 = 3

# 句自乘，以減弦自乘，其餘開方除之，即股
弦自乘 = 弦 ** 2
句自乘 = 句 ** 2
股自乘 = 弦自乘 - 句自乘

# 開方除之
a = 股自乘 ** Fraction(1, 2)  # Equivalent to square root
#----- content ends here -----

"""
"""
