"""
今有積六萬三千四百一尺、五百一十二分尺之四百四十七。問︰為立方幾何？
荅曰： a尺 。
"""

"""
Suppose there is a volume of 63,401 chi and 447/512 fractional chi.
Question: how many cubic chi does it make?

Answer: it makes *a* cubic chi.
"""

from fractions import Fraction

# Given volume in chi
積整數 = 63401  # Whole part in chi
積分數 = Fraction(447, 512)  # Fractional part in chi

# Total volume in chi
總積 = 積整數 + 積分數

# Since the volume is already in cubic chi, the result is simply the total volume
a = 總積

# Output the result
a
"""
Variable 'a' has wrong value. Expected: 319/8, Actual: 32461759/512"""
