"""
今有股四尺，弦五尺，問︰為句幾何？
句股術曰：句股各自乘，并，而開方除之，即弦。又股自乘，以減弦自乘，其餘開方除之，即句。又句自乘，以減弦自乘，其餘開方除之，即股。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a leg (gu) of 4 chi and a hypotenuse (xian) of 5 chi.
Question: how long is the other leg (ju)?

The procedure for right triangles says:
1. Each of the legs (ju and gu) is multiplied by itself, then added together, and the square root is taken, giving the hypotenuse (xian).
2. The leg (gu) is multiplied by itself, and this is subtracted from the hypotenuse (xian) multiplied by itself. The remainder is square-rooted, giving the other leg (ju).
3. The other leg (ju) is multiplied by itself, and this is subtracted from the hypotenuse (xian) multiplied by itself. The remainder is square-rooted, giving the first leg (gu).

Answer: *a* chi.
"""

# 股四尺
股 = 4

# 弦五尺
弦 = 5

# 股自乘
股自乘 = 股 * 股

# 弦自乘
弦自乘 = 弦 * 弦

# 以減弦自乘，其餘開方除之，即句
句自乘 = 弦自乘 - 股自乘
a = 句自乘 ** Fraction(1, 2)  # 開方 (square root)#----- content ends here -----

"""
"""
