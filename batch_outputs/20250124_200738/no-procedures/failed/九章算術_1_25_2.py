"""
又有圭田廣五步、二分步之一，從八步、三分步之二。問：為田幾何？
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a rectangular field (圭田) with a width of 5 bu and 1/2 bu, and a length of 8 bu and 2/3 bu.
Question: how large is the area of the field?

Answer: it makes *a* bu².
"""

from fractions import Fraction

# 廣五步、二分步之一 (width = 5 + 1/2 bu)
廣 = 5 + Fraction(1, 2)

# 從八步、三分步之二 (length = 8 + 2/3 bu)
從 = 8 + Fraction(2, 3)

# Calculate the area of the field (area = width * length)
a = 廣 * 從

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 143/6, Actual: 143/3"""
