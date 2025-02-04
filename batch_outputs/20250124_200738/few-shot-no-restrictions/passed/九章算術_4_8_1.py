"""
今有田廣一步半、三分步之一、四分步之一、五分步之一、六分步之一、七分步之一、八分步之一、九分步之一、十分步之一。求田一畝，問︰從幾何？
術曰：下有一十分，以一為二千五百二十，半為一千二百六十，三分之一為八百四十，四分之一為六百三十，五分之一為五百四，六分之一為四百二十，七分之一為三百六十，八分之一為三百一十五，九分之一為二百八十，十分之一為二百五十二，并之得七千三百八十一，以為法。置田二百四十步，亦以一為二千五百二十乘之，為實。實如法得從步。
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a field with a width of 1 bu and a half, plus 1/3 bu, 1/4 bu, 1/5 bu, 1/6 bu, 1/7 bu, 1/8 bu, 1/9 bu, and 1/10 bu. A field of 1 mu is sought.
Question: how large is the length?

The procedure says: Below, there is 1/10. Take 1 as 2520, 1/2 as 1260, 1/3 as 840, 1/4 as 630, 1/5 as 504, 1/6 as 420, 1/7 as 360, 1/8 as 315, 1/9 as 280, and 1/10 as 252. Add these, obtaining 7381 as the divisor.
Place the field of 240 bu, and also multiply it by taking 1 as 2520, giving the dividend.
Do the division, obtaining the number of steps of the length.

The answer says: *a* bu.
"""

from fractions import Fraction

# Define the width of the field
廣 = (
    1  # 1 bu
    + Fraction(1, 2)  # 1/2 bu
    + Fraction(1, 3)  # 1/3 bu
    + Fraction(1, 4)  # 1/4 bu
    + Fraction(1, 5)  # 1/5 bu
    + Fraction(1, 6)  # 1/6 bu
    + Fraction(1, 7)  # 1/7 bu
    + Fraction(1, 8)  # 1/8 bu
    + Fraction(1, 9)  # 1/9 bu
    + Fraction(1, 10)  # 1/10 bu
)

# Convert each fraction to its equivalent in terms of the base unit (2520)
base_unit = 2520
廣_in_base_units = (
    1 * base_unit  # 1 bu
    + Fraction(1, 2) * base_unit  # 1/2 bu
    + Fraction(1, 3) * base_unit  # 1/3 bu
    + Fraction(1, 4) * base_unit  # 1/4 bu
    + Fraction(1, 5) * base_unit  # 1/5 bu
    + Fraction(1, 6) * base_unit  # 1/6 bu
    + Fraction(1, 7) * base_unit  # 1/7 bu
    + Fraction(1, 8) * base_unit  # 1/8 bu
    + Fraction(1, 9) * base_unit  # 1/9 bu
    + Fraction(1, 10) * base_unit  # 1/10 bu
)

# 法: The divisor is the sum of all these values
法 = 廣_in_base_units

# 置田二百四十步 (240 bu for 1 mu)
田 = 240

# Multiply田 by the base unit (2520) to get the dividend
實 = 田 * base_unit

# Perform the division to find the length
a = Fraction(實, 法)

# Output the result
a#----- content ends here -----

"""
"""
