"""
今有田廣一步半、三分步之一、四分步之一、五分步之一、六分步之一、七分步之一、八分步之一、九分步之一。求田一畝，問︰從幾何？
術曰：下有九分，以一為二千五百二十，半為一千二百六十，三分之一為八百四十，四分之一為六百三十，五分之一為五百四，六分之一為四百二十，七分之一為三百六十，八分之一為三百一十五，九分之一為二百八十，并之得七千一百二十九，以為法。置田二百四十步，亦以一為二千五百二十乘之，為實。實如法得從步。
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a field with a width of 1.5 bu, plus 1/3 bu, plus 1/4 bu, plus 1/5 bu, plus 1/6 bu, plus 1/7 bu, plus 1/8 bu, plus 1/9 bu.
A field of 1 mu is sought.
Question: how large is the length?

The procedure says: Below, there are denominators up to 9.
Take 1 as 2520, 1/2 as 1260, 1/3 as 840, 1/4 as 630, 1/5 as 504, 1/6 as 420, 1/7 as 360, 1/8 as 315, and 1/9 as 280.
Add these together, obtaining 7129 as the divisor.
Place the field of 240 bu, and also multiply it by taking 1 as 2520, giving the dividend.
Do the division, obtaining the number of steps of the length.

The answer says: *a* bu.
"""

from fractions import Fraction

# Define the width of the field
廣 = Fraction(1, 1) + Fraction(1, 2) + Fraction(1, 3) + Fraction(1, 4) + Fraction(1, 5) + Fraction(1, 6) + Fraction(1, 7) + Fraction(1, 8) + Fraction(1, 9)

# Convert each fraction to the equivalent "scaled" value
scaled_values = {
    Fraction(1, 1): 2520,
    Fraction(1, 2): 1260,
    Fraction(1, 3): 840,
    Fraction(1, 4): 630,
    Fraction(1, 5): 504,
    Fraction(1, 6): 420,
    Fraction(1, 7): 360,
    Fraction(1, 8): 315,
    Fraction(1, 9): 280,
}

# Calculate the divisor (法)
法 = sum(scaled_values.values())

# Define the area of 1 mu in bu
田 = 240

# Multiply the area by the scaled value of 1 (2520)
實 = 田 * 2520

# Calculate the length (從步)
a = Fraction(實, 法)

a#----- content ends here -----

"""
"""
