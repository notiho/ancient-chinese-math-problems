"""
又有積一百九十三萬七千五百四十一尺、二十七分尺之一十七。問︰為立方幾何？
荅曰： a尺 。
"""

"""
Suppose there is a volume of 1,937,541 chi and 27/17 chi (fractional part).
Question: how many cubic chi does it make?

Answer: it makes *a* cubic chi.
"""

from fractions import Fraction

# Total volume in chi
積 = 1937541 + Fraction(27, 17)

# Convert to cubic chi (since the unit is already in cubic chi, no further calculation is needed)
a = 積

# Result
a
"""
Variable 'a' has wrong value. Expected: 374/3, Actual: 32938224/17"""
