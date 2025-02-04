"""
今有田廣一步半、三分步之一、四分步之一、五分步之一、六分步之一。求田一畝，問︰從幾何？
術曰：下有六分，以一為一百二十，半為六十，三分之一為四十，四分之一為三十，五分之一為二十四，六分之一為二十，并之得二百九十四以為法。置田二百四十步，亦以一為一百二十乘之，為實。實如法得從步。
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a field with a width of 1 bu, 1/2 bu, 1/3 bu, 1/4 bu, 1/5 bu, and 1/6 bu. A field of 1 mu is sought.
Question: how large is the length?

The procedure says: Below, there are sixths. Take 1 as 120, 1/2 as 60, 1/3 as 40, 1/4 as 30, 1/5 as 24, and 1/6 as 20.
Add these, obtaining 294 as the divisor.
Place the field of 240 bu, and also multiply it by taking 1 as 120, giving the dividend.
Do the division, obtaining the number of steps of the length.

The answer says: *a* bu.
"""

from fractions import Fraction

# Field width components
廣 = [
    1,  # 1 bu
    Fraction(1, 2),  # 1/2 bu
    Fraction(1, 3),  # 1/3 bu
    Fraction(1, 4),  # 1/4 bu
    Fraction(1, 5),  # 1/5 bu
    Fraction(1, 6),  # 1/6 bu
]

# Convert each component to a common denominator (1 as 120, etc.)
廣轉換 = [
    120,  # 1 bu = 120
    60,  # 1/2 bu = 60
    40,  # 1/3 bu = 40
    30,  # 1/4 bu = 30
    24,  # 1/5 bu = 24
    20,  # 1/6 bu = 20
]

# Add these to get the divisor (法)
法 = sum(廣轉換)

# Field area (240 bu)
田 = 240

# Multiply by 120 to get the dividend (實)
實 = 120 * 田

# Perform the division to get the length (從步)
a = Fraction(實, 法)

# Output the result
a#----- content ends here -----

"""
"""
