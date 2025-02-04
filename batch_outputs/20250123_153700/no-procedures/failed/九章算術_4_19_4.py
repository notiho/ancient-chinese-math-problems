"""
今有積一千九百五十三尺、八分尺之一。問︰為立方幾何？
荅曰： a尺 。
"""

"""
Suppose there is a volume of 1953 and 1/8 cubic chi.
Question: how many cubic chi does it make?

Answer: it makes *a* cubic chi.
"""

from fractions import Fraction

# Given volume
積 = 1953 + Fraction(1, 8)

# Since the volume is already in cubic chi, the answer is simply:
a = 積

# Output the result
a
"""
Variable 'a' has wrong value. Expected: 25/2, Actual: 15625/8"""
