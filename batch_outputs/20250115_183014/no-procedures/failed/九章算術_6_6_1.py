"""
今有取傭負鹽二斛，行一百里，與錢四十。今負鹽一斛七斗三升、少半升，行八十里。問︰與錢幾何？
荅曰： a錢 。
"""

"""
Suppose a laborer carries 2 hu of salt for 100 li and is paid 40 qian.
Now, the laborer carries 1 hu, 7 dou, 3 sheng, and half a sheng of salt for 80 li.
Question: how much money should the laborer be paid?

Answer: *a* qian.
"""

from fractions import Fraction

# Original payment details
original_salt = 2  # in hu
original_distance = 100  # in li
original_payment = 40  # in qian

# New carrying details
new_salt = 1 + Fraction(7, 10) + Fraction(3, 100) + Fraction(1, 200)  # Convert 1 hu, 7 dou, 3 sheng, and half a sheng to hu
new_distance = 80  # in li

# Payment is proportional to the product of the amount of salt and the distance
# Calculate the proportional payment
a = Fraction(new_salt * new_distance * original_payment, original_salt * original_distance)

a  # Result in qian
"""
Variable 'a' has wrong value. Expected: 416/15, Actual: 694/25"""
