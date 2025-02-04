"""
今有句三尺，股四尺，問︰為弦幾何？
句股術曰：句股各自乘，并，而開方除之，即弦。又股自乘，以減弦自乘，其餘開方除之，即句。又句自乘，以減弦自乘，其餘開方除之，即股。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a right triangle with a base (leg) of 3 chi and a height (leg) of 4 chi.
Question: how long is the hypotenuse?

The procedure says: Multiply each of the base and height by itself (square them), add the results, and take the square root, obtaining the hypotenuse.
Additionally, if the square of the hypotenuse is reduced by the square of the height, the square root of the remainder gives the base.
Similarly, if the square of the hypotenuse is reduced by the square of the base, the square root of the remainder gives the height.

Answer: the hypotenuse is *a* chi.
"""

import math

# 句三尺
句 = 3

# 股四尺
股 = 4

# 句股各自乘
句平方 = 句 ** 2
股平方 = 股 ** 2

# 并，而開方除之，即弦
弦平方 = 句平方 + 股平方
a = math.sqrt(弦平方)  # Hypotenuse length

# Answer
a#----- content ends here -----

"""
"""
