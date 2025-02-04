"""
今有取傭負鹽二斛，行一百里，與錢四十。今負鹽一斛七斗三升、少半升，行八十里。問︰與錢幾何？
荅曰： a錢 。
"""

#----- content starts here -----
"""
Suppose a laborer is hired to carry 2 hu of salt for 100 li and is paid 40 qian.
Now, the laborer carries 1 hu, 7 dou, 3 sheng, and half a sheng of salt for 80 li.
Question: how much money should be paid?

Answer: *a* qian.
"""

# Constants for the first case
first_salt = 2  # in hu
first_distance = 100  # in li
first_payment = 40  # in qian

# Constants for the second case
second_salt = 1 + Fraction(7, 10) + Fraction(3, 100) + Fraction(1, 200)  # Convert 1 hu, 7 dou, 3 sheng, and half a sheng to hu
second_distance = 80  # in li

# Payment is proportional to the product of the amount of salt and the distance traveled
# Calculate the proportional payment for the second case
a = Fraction(second_salt * second_distance, first_salt * first_distance) * first_payment

# Result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 416/15, Actual: 694/25"""
