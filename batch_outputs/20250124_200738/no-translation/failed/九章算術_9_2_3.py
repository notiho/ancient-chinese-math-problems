"""
今有股四尺，弦五尺，問︰為句幾何？
句股術曰：句股各自乘，并，而開方除之，即弦。又股自乘，以減弦自乘，其餘開方除之，即句。又句自乘，以減弦自乘，其餘開方除之，即股。
荅曰： a尺 。
"""

#----- content starts here -----

# 股四尺
股 = 4

# 弦五尺
弦 = 5

# 股自乘
股平方 = 股 * 股

# 弦自乘
弦平方 = 弦 * 弦

# 以減弦自乘，其餘開方除之，即句
句平方 = 弦平方 - 股平方
句 = Fraction(句平方).sqrt()

a = 句#----- content ends here -----

"""
Code error: 'Fraction' object has no attribute 'sqrt'"""
