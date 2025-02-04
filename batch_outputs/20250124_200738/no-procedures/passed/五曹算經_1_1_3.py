"""
今有方田廣從各六十八步。問：為田㡬何？
答曰： a畝 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a square field with both the width and the length being 68 bu.
Question: how large is the field?

Answer: it is *a* mu and *b* bu.
"""

from fractions import Fraction

# 方田廣從各六十八步
廣 = 68
從 = 68

# Calculate the total area in bu²
total_area_bu2 = 廣 * 從

# Convert bu² to mu (1 mu = 240 bu²)
a = total_area_bu2 // 240  # Whole mu
b = total_area_bu2 % 240   # Remaining bu²

a, b  # Output the result as (a mu, b bu²)#----- content ends here -----

"""
"""
