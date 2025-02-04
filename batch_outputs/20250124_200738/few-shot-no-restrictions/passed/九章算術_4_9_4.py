"""
今有田廣一步半、三分步之一、四分步之一、五分步之一、六分步之一、七分步之一、八分步之一、九分步之一、十分步之一、十一分步之一。求田一畝，問︰從幾何？
術曰：下有一十一分，以一為二萬七千七百二十，半為一萬三千八百六十，三分之一為九千二百四十，四分之一為六千九百三十，五分之一為五千五百四十四，六分之一為四千六百二十，七分之一為三千九百六十，八分之一為三千四百六十五，九分之一為三千八十，一十分之一為二千七百七十二，一十一分之一為二千五百二十，并之得八萬三千七百一十一，以為法。置田二百四十步，亦以一為二萬七千七百二十乘之，為實。實如法得從步。
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a field with a width of 1 bu, plus 1/2 bu, plus 1/3 bu, plus 1/4 bu, plus 1/5 bu, plus 1/6 bu, plus 1/7 bu, plus 1/8 bu, plus 1/9 bu, plus 1/10 bu, plus 1/11 bu.
A field of 1 mu is sought.
Question: how large is the length?

The procedure says: Below, there is 1/11. Take 1 as 27720, 1/2 as 13860, 1/3 as 9240, 1/4 as 6930, 1/5 as 5544, 1/6 as 4620, 1/7 as 3960, 1/8 as 3465, 1/9 as 3080, 1/10 as 2772, and 1/11 as 2520.
Add these, obtaining 83711 as the divisor.
Place the field of 240 bu, and also multiply it by taking 1 as 27720, giving the dividend.
Do the division, obtaining the number of steps of the length.

The answer says: *a* bu.
"""

from fractions import Fraction

# Define the widths of the field
widths = [
    1,  # 1 bu
    Fraction(1, 2),  # 1/2 bu
    Fraction(1, 3),  # 1/3 bu
    Fraction(1, 4),  # 1/4 bu
    Fraction(1, 5),  # 1/5 bu
    Fraction(1, 6),  # 1/6 bu
    Fraction(1, 7),  # 1/7 bu
    Fraction(1, 8),  # 1/8 bu
    Fraction(1, 9),  # 1/9 bu
    Fraction(1, 10),  # 1/10 bu
    Fraction(1, 11),  # 1/11 bu
]

# Convert each width to the least common denominator (LCD) of 27720
lcd = 27720
converted_widths = [int(width * lcd) for width in widths]

# Add the converted widths to calculate the divisor (法)
法 = sum(converted_widths)

# Define the field area (田) in bu
田 = 240

# Multiply the field area by the LCD to calculate the dividend (實)
實 = 田 * lcd

# Calculate the length (從) by dividing the dividend by the divisor
a = Fraction(實, 法)

# Output the result
a#----- content ends here -----

"""
"""
