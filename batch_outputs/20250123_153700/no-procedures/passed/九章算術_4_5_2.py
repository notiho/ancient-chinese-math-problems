"""
今有田廣一步半、三分步之一、四分步之一、五分步之一、六分步之一、七分步之一。求田一畝，問︰從幾何？
荅曰： a步 。
"""

"""
Suppose there is a field with a width of 1.5 bu, plus 1/3 bu, plus 1/4 bu, plus 1/5 bu, plus 1/6 bu, plus 1/7 bu.
A field of 1 mu is sought.
Question: how large is the length?

The answer says: *a* bu.
"""

from fractions import Fraction

# Width of the field (廣)
廣 = Fraction(3, 2) + Fraction(1, 3) + Fraction(1, 4) + Fraction(1, 5) + Fraction(1, 6) + Fraction(1, 7)

# Area of 1 mu (田)
田 = 240  # 1 mu = 240 square bu

# Length of the field (從) is calculated as area divided by width
a = Fraction(田, 廣)

# Result
a
"""
"""
