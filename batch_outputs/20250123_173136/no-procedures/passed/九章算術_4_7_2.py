"""
今有田廣一步半、三分步之一、四分步之一、五分步之一、六分步之一、七分步之一、八分步之一、九分步之一。求田一畝，問︰從幾何？
荅曰： a步 。
"""

"""
Suppose there is a field with a width of:
1 bu + 1/2 bu + 1/3 bu + 1/4 bu + 1/5 bu + 1/6 bu + 1/7 bu + 1/8 bu + 1/9 bu.
A field of 1 mu is sought.
Question: how large is the length?

The answer says: *a* bu.
"""

from fractions import Fraction

# Calculate the total width
廣 = (
    1
    + Fraction(1, 2)
    + Fraction(1, 3)
    + Fraction(1, 4)
    + Fraction(1, 5)
    + Fraction(1, 6)
    + Fraction(1, 7)
    + Fraction(1, 8)
    + Fraction(1, 9)
)

# 1 mu is equivalent to 240 square bu
田 = 240

# Calculate the length by dividing the area by the width
a = Fraction(田, 廣)

# Output the result
a
"""
"""
