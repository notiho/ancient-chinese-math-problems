"""
今有田廣一步半、三分步之一、四分步之一、五分步之一、六分步之一、七分步之一。求田一畝，問︰從幾何？
術曰：下有七分，以一為四百二十，半為二百一十，三分之一為一百四十，四分之一為一百五，五分之一為八十四，六分之一為七十，七分之一為六十，并之得一千八十九，以為法。置田二百四十步，亦以一為四百二十乘之，為實。實如法得從步。
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a field with a width of 1 bu, 1/2 bu, 1/3 bu, 1/4 bu, 1/5 bu, 1/6 bu, and 1/7 bu.
A field of 1 mu is sought.
Question: how large is the length?

The procedure says: Below, there are denominators up to 7.
Take 1 as 420, 1/2 as 210, 1/3 as 140, 1/4 as 105, 1/5 as 84, 1/6 as 70, and 1/7 as 60.
Add these, obtaining 1089 as the divisor.
Place the field of 240 bu, and also multiply it by taking 1 as 420, giving the dividend.
Do the division, obtaining the number of steps of the length.

The answer says: *a* bu.
"""

from fractions import Fraction

# Define the width components
width_components = [
    1,                      # 1 bu
    Fraction(1, 2),         # 1/2 bu
    Fraction(1, 3),         # 1/3 bu
    Fraction(1, 4),         # 1/4 bu
    Fraction(1, 5),         # 1/5 bu
    Fraction(1, 6),         # 1/6 bu
    Fraction(1, 7)          # 1/7 bu
]

# Convert each component to the equivalent value in terms of the base unit (1 = 420)
base_unit = 420
converted_widths = [base_unit * component for component in width_components]

# Add all converted widths to get the divisor (法)
法 = sum(converted_widths)

# The total field area in bu (240 bu)
田 = 240

# Multiply the field area by the base unit to get the dividend (實)
實 = 田 * base_unit

# Perform the division to get the length (從步)
a = Fraction(實, 法)

# Output the result
a#----- content ends here -----

"""
"""
