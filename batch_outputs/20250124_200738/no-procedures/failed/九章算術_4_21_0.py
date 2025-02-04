"""
又有積一百九十三萬七千五百四十一尺、二十七分尺之一十七。問︰為立方幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a volume of 1,937,541 chi and 17/27 of a chi.
Question: how many cubic chi does it make?

Answer: it makes *a* cubic chi.
"""

from fractions import Fraction

# Given volume in chi
積 = 1937541 + Fraction(17, 27)

# Since the volume is already in cubic chi, the answer is simply:
a = 積

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 374/3, Actual: 52313624/27"""
