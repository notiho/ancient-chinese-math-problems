"""
今有圭田廣十二步，正從二十一步。問：為田幾何？
術曰：半廣以乘正從。
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a wedge-shaped field with a width of 12 bu and a length of 21 bu.
Question: how large is the area of the field?

The procedure says: Take half of the width and multiply it by the full length.

The answer says: *a* bu².
"""

from fractions import Fraction

# 廣十二步
廣 = 12

# 正從二十一步
正從 = 21

# 半廣以乘正從
半廣 = Fraction(廣, 2)
a = 半廣 * 正從

# Output the result
a#----- content ends here -----

"""
"""
