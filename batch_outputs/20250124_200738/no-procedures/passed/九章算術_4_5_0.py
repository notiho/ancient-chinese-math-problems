"""
今有田廣一步半、三分步之一、四分步之一、五分步之一、六分步之一、七分步之一。求田一畝，問︰從幾何？
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a field with a width of 1 bu and a half, plus 1/3 bu, plus 1/4 bu, plus 1/5 bu, plus 1/6 bu, plus 1/7 bu.
A field of 1 mu is sought.
Question: how large is the length?

The answer says: *a* bu.
"""

from fractions import Fraction

# 廣一步半、三分步之一、四分步之一、五分步之一、六分步之一、七分步之一
廣 = 1 + Fraction(1, 2) + Fraction(1, 3) + Fraction(1, 4) + Fraction(1, 5) + Fraction(1, 6) + Fraction(1, 7)

# 田一畝 (1 mu = 240 square bu)
田 = 240

# 求從 (length = area / width)
a = Fraction(田, 廣)

a  # Output the result in bu#----- content ends here -----

"""
"""
