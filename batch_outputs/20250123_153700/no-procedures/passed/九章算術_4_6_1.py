"""
今有田廣一步半、三分步之一、四分步之一、五分步之一、六分步之一、七分步之一、八分步之一。求田一畝，問︰從幾何？
荅曰： a步 。
"""

"""
Suppose there is a field with a width of:
1 bu + 1/2 bu + 1/3 bu + 1/4 bu + 1/5 bu + 1/6 bu + 1/7 bu + 1/8 bu.
A field of 1 mu is sought.
Question: how large is the length?

Answer: *a* bu.
"""

from fractions import Fraction

# Width of the field (廣)
廣 = (
    1
    + Fraction(1, 2)
    + Fraction(1, 3)
    + Fraction(1, 4)
    + Fraction(1, 5)
    + Fraction(1, 6)
    + Fraction(1, 7)
    + Fraction(1, 8)
)

# Area of the field (田) is 1 mu
田 = 240  # 1 mu = 240 square bu

# Length of the field (從) is calculated as area divided by width
a = Fraction(田, 廣)

a  # Output the length in bu
"""
"""
