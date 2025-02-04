"""
今有積六萬三千四百一尺、五百一十二分尺之四百四十七。問︰為立方幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a volume of 63,401 chi and 447/512 fractional chi.
Question: how many cubic chi does it represent?

Answer: it represents *a* cubic chi.
"""

from fractions import Fraction

# Given volume in chi
積 = 63401 + Fraction(447, 512)

# Since the volume is already in cubic chi, the answer is simply:
a = 積

# Output
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 319/8, Actual: 32461759/512"""
