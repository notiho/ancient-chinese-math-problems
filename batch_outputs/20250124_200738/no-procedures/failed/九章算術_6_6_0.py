"""
今有取傭負鹽二斛，行一百里，與錢四十。今負鹽一斛七斗三升、少半升，行八十里。問︰與錢幾何？
荅曰： a錢 。
"""

#----- content starts here -----
"""
Suppose a laborer is hired to carry 2 hu of salt for 100 li and is paid 40 qian.
Now, the laborer carries 1 hu, 7 dou, 3 sheng, and half a sheng of salt for 80 li.
Question: how much money should the laborer be paid?

Answer: *a* qian.
"""

from fractions import Fraction

# First scenario: 2 hu for 100 li = 40 qian
# Convert 2 hu to dou (1 hu = 10 dou)
first_salt = 2 * 10  # in dou
first_distance = 100  # in li
first_payment = 40  # in qian

# Second scenario: 1 hu, 7 dou, 3 sheng, and half a sheng for 80 li
# Convert to dou (1 hu = 10 dou, 1 dou = 10 sheng)
second_salt = 1 * 10 + 7 + Fraction(3, 10) + Fraction(1, 20)  # in dou
second_distance = 80  # in li

# Payment is proportional to the product of salt and distance
# Payment ratio = (second_salt * second_distance) / (first_salt * first_distance)
payment_ratio = (second_salt * second_distance) / (first_salt * first_distance)

# Calculate the payment for the second scenario
a = payment_ratio * first_payment

# Result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 416/15, Actual: 694/25"""
