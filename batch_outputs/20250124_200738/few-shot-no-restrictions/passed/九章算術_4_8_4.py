"""
今有田廣一步半、三分步之一、四分步之一、五分步之一、六分步之一、七分步之一、八分步之一、九分步之一、十分步之一。求田一畝，問︰從幾何？
術曰：下有一十分，以一為二千五百二十，半為一千二百六十，三分之一為八百四十，四分之一為六百三十，五分之一為五百四，六分之一為四百二十，七分之一為三百六十，八分之一為三百一十五，九分之一為二百八十，十分之一為二百五十二，并之得七千三百八十一，以為法。置田二百四十步，亦以一為二千五百二十乘之，為實。實如法得從步。
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a field with a width of one and a half bu, plus 1/3, 1/4, 1/5, 1/6, 1/7, 1/8, 1/9, and 1/10 bu. A field of 1 mu is sought.
Question: how large is the length?

The procedure says: Below, there is 1/10. Take 1 as 2520, 1/2 as 1260, 1/3 as 840, 1/4 as 630, 1/5 as 504, 1/6 as 420, 1/7 as 360, 1/8 as 315, 1/9 as 280, and 1/10 as 252. Add these, obtaining 7381 as the divisor.
Place the field of 240 bu, and also multiply it by taking 1 as 2520, giving the dividend.
Do the division, obtaining the number of steps of the length.

The answer says: *a* bu.
"""

from fractions import Fraction

# Define the width of the field
廣 = 1 + Fraction(1, 2) + Fraction(1, 3) + Fraction(1, 4) + Fraction(1, 5) + Fraction(1, 6) + Fraction(1, 7) + Fraction(1, 8) + Fraction(1, 9) + Fraction(1, 10)

# Convert each fraction to the equivalent value when 1 is taken as 2520
conversion_factor = 2520
廣_converted = (
    2520 * 1 +  # 1
    1260 +      # 1/2
    840 +       # 1/3
    630 +       # 1/4
    504 +       # 1/5
    420 +       # 1/6
    360 +       # 1/7
    315 +       # 1/8
    280 +       # 1/9
    252         # 1/10
)

# 法 (divisor)
法 = 廣_converted

# 置田二百四十步 (field size in bu)
田 = 240

# Multiply田 by the conversion factor
實 = 田 * conversion_factor

# Calculate the length (從步)
a = Fraction(實, 法)

a#----- content ends here -----

"""
"""
