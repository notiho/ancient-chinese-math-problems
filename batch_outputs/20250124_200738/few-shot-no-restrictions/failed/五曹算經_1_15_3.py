"""
今有田形如牛角從五十步口廣二十步。問：為田㡬何？
術曰：列口廣二十步半之得十步以從五十步乘之得五百步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a field shaped like a cow's horn (a trapezoid) with a length of 50 bu and a width at the mouth of 20 bu.
Question: how large is the field?

The procedure says: Take the width at the mouth (20 bu), halve it to get 10 bu.
Multiply this by the length (50 bu), obtaining 500 bu².
Divide this by the mu divisor (240 bu² per mu), and the result is the area in mu and remaining bu.

Answer: *a* mu and *b* bu.
"""

from fractions import Fraction

# Given values
口廣 = 20  # Width at the mouth in bu
從 = 50    # Length in bu
畝法 = 240  # 1 mu = 240 bu²

# Halve the width
半口廣 = 口廣 / 2

# Multiply by the length to get the total area in bu²
積步 = 半口廣 * 從

# Divide by the mu divisor to get the area in mu
畝數 = Fraction(積步, 畝法)

# Separate the result into whole mu and remaining bu
a = 畝數.numerator // 畝數.denominator  # Whole mu
b = 畝數.numerator % 畝數.denominator  # Remaining bu

a, b  # Output the result as (a mu, b bu)#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
