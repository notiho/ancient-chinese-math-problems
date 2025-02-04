"""
今有句三尺，股四尺，問︰為弦幾何？
句股術曰：句股各自乘，并，而開方除之，即弦。又股自乘，以減弦自乘，其餘開方除之，即句。又句自乘，以減弦自乘，其餘開方除之，即股。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a right triangle with one leg (ju) of 3 chi and the other leg (gu) of 4 chi.
Question: how long is the hypotenuse (xian)?

The procedure for right triangles says: Multiply each of the legs (ju and gu) by itself, add the results, and take the square root to find the hypotenuse.
Additionally:
- Multiply the other leg (gu) by itself, subtract the square of the hypotenuse, and take the square root to find the first leg (ju).
- Multiply the first leg (ju) by itself, subtract the square of the hypotenuse, and take the square root to find the other leg (gu).

Answer: the hypotenuse is *a* chi.
"""

import math

# Given values
句 = 3  # ju (one leg)
股 = 4  # gu (other leg)

# Procedure: 弦 = sqrt(句^2 + 股^2)
弦平方 = 句**2 + 股**2
弦 = math.sqrt(弦平方)

# Answer
a = 弦
a  # Hypotenuse in chi#----- content ends here -----

"""
"""
