"""
今有田廣一步半、三分步之一、四分步之一。求田一畝，問︰從幾何？
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a field with a width of 1 bu, 1/2 bu, 1/3 bu, and 1/4 bu combined. A field of 1 mu is sought.
Question: how large is the length?

The answer says: *a* bu.
"""

from fractions import Fraction

# 廣一步半、三分步之一、四分步之一
廣 = 1 + Fraction(1, 2) + Fraction(1, 3) + Fraction(1, 4)

# 田一畝 (1 mu = 240 square bu)
田 = 240

# 求從 (length = area / width)
a = Fraction(田, 廣)

a#----- content ends here -----

"""
"""
