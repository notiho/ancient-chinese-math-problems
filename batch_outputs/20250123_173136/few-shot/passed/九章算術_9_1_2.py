"""
今有弦五尺，句三尺，問︰為股幾何？
句股術曰：句股各自乘，并，而開方除之，即弦。又股自乘，以減弦自乘，其餘開方除之，即句。又句自乘，以減弦自乘，其餘開方除之，即股。
荅曰： a尺 。
"""

"""
Suppose there is a hypotenuse (弦) of 5 chi and one leg (句) of 3 chi.
Question: how long is the other leg (股)?

The procedure for the right triangle says:
Each leg (句 and 股) is multiplied by itself, and their sums are square-rooted to give the hypotenuse (弦).
Alternatively:
The other leg (股) is multiplied by itself, and subtracted from the square of the hypotenuse (弦). The remainder is square-rooted to give the first leg (句).
Or:
The first leg (句) is multiplied by itself, and subtracted from the square of the hypotenuse (弦). The remainder is square-rooted to give the other leg (股).

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

# 開方除之，即股
a = 股自乘 ** Fraction(1, 2)  # Square root of 股自乘
"""
"""
