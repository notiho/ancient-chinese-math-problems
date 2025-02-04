"""
今有弦五尺，句三尺，問︰為股幾何？
句股術曰：句股各自乘，并，而開方除之，即弦。又股自乘，以減弦自乘，其餘開方除之，即句。又句自乘，以減弦自乘，其餘開方除之，即股。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a hypotenuse (弦) of 5 chi and one leg (句) of 3 chi.
Question: how long is the other leg (股)?

The procedure says:
- Multiply each of the legs (句 and 股) by itself, add them, and take the square root to get the hypotenuse (弦).
- Alternatively, multiply the other leg (股) by itself, subtract it from the square of the hypotenuse (弦), and take the square root to get the known leg (句).
- Finally, multiply the known leg (句) by itself, subtract it from the square of the hypotenuse (弦), and take the square root to get the unknown leg (股).

Answer: *a* chi.
"""

import math

# 弦五尺
弦 = 5

# 句三尺
句 = 3

# 句自乘，以減弦自乘，其餘開方除之，即股
股平方 = 弦**2 - 句**2
股 = math.sqrt(股平方)

a = 股
#----- content ends here -----

"""
"""
