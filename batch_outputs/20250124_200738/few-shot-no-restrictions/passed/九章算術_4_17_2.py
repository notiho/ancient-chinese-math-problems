"""
今有積三百步。問︰為圓周幾何？
開圓術曰：置積步數，以十二乘之，以開方除之，即得周。
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is an area of 300 bu. 
Question: what is the circumference of the circle?

The procedure for circles says: Place the area in bu, multiply it by 12, and take the square root of the result. 
This gives the circumference.

Answer: *a* bu.
"""

import math

# 積三百步
積步數 = 300

# 以十二乘之
積乘十二 = 12 * 積步數

# 以開方除之，即得周
a = math.sqrt(積乘十二)

a  # The circumference in bu#----- content ends here -----

"""
"""
