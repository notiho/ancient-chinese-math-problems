"""
今有弦五尺句三尺問為股幾何
句股術曰句股各自乘并而開方除之即弦又股自乘以減弦自乘其餘開方除之即句又句自乘以減弦自乘其餘開方除之即股
荅曰 a尺 
"""

#----- content starts here -----
"""
Suppose there is a hypotenuse (弦) of 5 chi and one leg (句) of 3 chi.
Question: how long is the other leg (股)?

The procedure for the legs and hypotenuse says: Multiply each of the legs (句 and 股) by itself, add them together, and take the square root to obtain the hypotenuse (弦).
Alternatively:
- Multiply the other leg (股) by itself, subtract it from the square of the hypotenuse (弦), and take the square root to obtain the first leg (句).
- Multiply the first leg (句) by itself, subtract it from the square of the hypotenuse (弦), and take the square root to obtain the other leg (股).

The answer says: *a* chi.
"""

# 弦五尺
弦 = 5

# 句三尺
句 = 3

# 句自乘以減弦自乘其餘開方除之即股
弦自乘 = 弦 ** 2
句自乘 = 句 ** 2
股自乘 = 弦自乘 - 句自乘

# 開方
a = 股自乘 ** 0.5#----- content ends here -----

"""
"""
