"""
今有句三尺，股四尺，問︰為弦幾何？
句股術曰：句股各自乘，并，而開方除之，即弦。又股自乘，以減弦自乘，其餘開方除之，即句。又句自乘，以減弦自乘，其餘開方除之，即股。
荅曰： a尺 。
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
# 開方即為平方根，弦 = sqrt(和)
# Since we are not using external libraries, we will represent the square root as a Fraction approximation.
弦平方 = 和
a = Fraction(弦平方).limit_denominator() ** Fraction(1, 2)  # Approximation for square root
"""
"""
