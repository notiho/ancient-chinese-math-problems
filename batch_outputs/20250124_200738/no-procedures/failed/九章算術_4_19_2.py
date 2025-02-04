"""
今有積一千九百五十三尺、八分尺之一。問︰為立方幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a volume of 1953 1/8 cubic chi.
Question: how many cubic chi does it make?

Answer: it makes *a* cubic chi.
"""

from fractions import Fraction

# Given volume in cubic chi
積 = 1953 + Fraction(1, 8)

# Since the volume is already in cubic chi, the result is the same
a = 積

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 25/2, Actual: 15625/8"""
