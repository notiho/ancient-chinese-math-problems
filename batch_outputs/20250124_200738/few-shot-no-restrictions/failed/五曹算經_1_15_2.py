"""
今有田形如牛角從五十步口廣二十步。問：為田㡬何？
術曰：列口廣二十步半之得十步以從五十步乘之得五百步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a field shaped like a cow's horn, with a length of 50 bu and a mouth width of 20 bu.
Question: how large is the field?

The procedure says: Take the mouth width of 20 bu, halve it to get 10 bu.
Multiply this by the length of 50 bu to get 500 bu².
Divide this by the mu-divisor (240 bu² per mu) to obtain the result.

Answer: *a* mu and *b* bu².
"""

from fractions import Fraction

# Given values
口廣 = 20  # bu
從 = 50  # bu
畝法 = 240  # bu² per mu

# Halve the mouth width
半口廣 = 口廣 / 2

# Multiply by the length
積步 = 半口廣 * 從

# Divide by the mu-divisor to get the area in mu
畝數 = Fraction(積步, 畝法)

# Separate into whole mu and remaining bu²
a = 畝數.numerator // 畝數.denominator  # Whole mu
b = 畝數.numerator % 畝數.denominator  # Remaining bu²

# Final result
a, b#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
