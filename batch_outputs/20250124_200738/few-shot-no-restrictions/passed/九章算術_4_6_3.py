"""
今有田廣一步半、三分步之一、四分步之一、五分步之一、六分步之一、七分步之一、八分步之一。求田一畝，問︰從幾何？
術曰：下有八分，以一為八百四十，半為四百二十，三分之一為二百八十，四分之一為二百一十，五分之一為一百六十八，六分之一為一百四十，七分之一為一百二十，八分之一為一百五，并之得二千二百八十三，以為法。置田二百四十步，亦以一為八百四十乘之，為實。實如法得從步。
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a field with a width of 1 bu, 1/2 bu, 1/3 bu, 1/4 bu, 1/5 bu, 1/6 bu, 1/7 bu, and 1/8 bu.
A field of 1 mu is sought.
Question: how large is the length?

The procedure says: Below, there are eighths. Take 1 as 840, 1/2 as 420, 1/3 as 280, 1/4 as 210, 1/5 as 168, 1/6 as 140, 1/7 as 120, and 1/8 as 105.
Add these, obtaining 2283 as the divisor.
Place the field of 240 bu, and also multiply it by taking 1 as 840, giving the dividend.
Do the division, obtaining the number of steps of the length.

The answer says: *a* bu.
"""

from fractions import Fraction

# Define the widths in terms of fractions of a bu
widths = [
    1,  # 1 bu
    Fraction(1, 2),  # 1/2 bu
    Fraction(1, 3),  # 1/3 bu
    Fraction(1, 4),  # 1/4 bu
    Fraction(1, 5),  # 1/5 bu
    Fraction(1, 6),  # 1/6 bu
    Fraction(1, 7),  # 1/7 bu
    Fraction(1, 8),  # 1/8 bu
]

# Convert each width to a common base (1 as 840)
base = 840
converted_widths = [int(base * width) for width in widths]

# Add them to get the divisor (法)
法 = sum(converted_widths)

# Place the field of 240 bu
田 = 240

# Multiply the field by the base to get the dividend (實)
實 = 田 * base

# Perform the division to get the length (從步)
a = Fraction(實, 法)

# Output the result
a#----- content ends here -----

"""
"""
