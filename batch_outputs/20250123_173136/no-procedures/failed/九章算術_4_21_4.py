"""
又有積一百九十三萬七千五百四十一尺、二十七分尺之一十七。問︰為立方幾何？
荅曰： a尺 。
"""

"""
Suppose there is a volume of 1,937,541 chi and 27/17 of a chi.
Question: how many cubic chi does it represent?

Answer: it is *a* cubic chi.
"""

from fractions import Fraction

# Total volume in chi
積 = 1937541 + Fraction(27, 17)

# Since the volume is already in cubic chi, the answer is simply the given value
a = 積
"""
Variable 'a' has wrong value. Expected: 374/3, Actual: 32938224/17"""
