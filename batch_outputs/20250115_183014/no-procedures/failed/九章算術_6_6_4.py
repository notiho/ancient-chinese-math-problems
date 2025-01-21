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

# First, represent the given values
# 2 hu = 20 dou (1 hu = 10 dou)
total_salt_1 = 20  # in dou
distance_1 = 100  # in li
payment_1 = 40  # in qian

# The second case
# 1 hu = 10 dou, 7 dou, 3 sheng, and half a sheng
# 1 dou = 10 sheng
total_salt_2 = 10 + 7 + Fraction(3, 10) + Fraction(1, 20)  # in dou
distance_2 = 80  # in li

# Calculate the payment rate per dou-li
rate_per_dou_li = Fraction(payment_1, total_salt_1 * distance_1)

# Calculate the payment for the second case
a = rate_per_dou_li * total_salt_2 * distance_2

# Result
a
"""
Variable 'a' has wrong value. Expected: 416/15, Actual: 694/25"""
