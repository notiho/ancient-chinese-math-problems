"""
今有弦五尺句三尺問為股幾何
句股術曰句股各自乘并而開方除之即弦又股自乘以減弦自乘其餘開方除之即句又句自乘以減弦自乘其餘開方除之即股
荅曰 a尺 
"""

#----- content starts here -----
"""
Suppose there is a hypotenuse (弦) of 5 chi and one leg (句) of 3 chi.
Question: how long is the other leg (股)?

The procedure says: For the legs (句 and 股), each is multiplied by itself, then added together, and the square root is taken, yielding the hypotenuse.
Alternatively, for the leg (股), multiply it by itself, subtract it from the square of the hypotenuse, and take the square root, yielding the other leg (句).
Similarly, for the leg (句), multiply it by itself, subtract it from the square of the hypotenuse, and take the square root, yielding the other leg (股).

The answer says: *a* chi.
"""

# 弦五尺
弦 = 5

# 句三尺
句 = 3

# 弦自乘
弦自乘 = 弦 * 弦

# 句自乘
句自乘 = 句 * 句

# 股自乘以減弦自乘，其餘開方除之，即股
股自乘 = 弦自乘 - 句自乘
a = 股自乘**0.5  # 開方 (square root)#----- content ends here -----

"""
"""
