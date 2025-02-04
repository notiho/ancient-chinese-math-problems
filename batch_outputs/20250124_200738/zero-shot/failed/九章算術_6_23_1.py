"""
今有假田，初假之歲三畝一錢，明年四畝一錢，後年五畝一錢。凡三歲得一百，問︰田幾何？
術曰：置畝數及錢數，令畝數互乘錢數，并以為法。畝數相乘，又以百錢乘之，為實。實如法得一畝。
荅曰： a頃 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
money = 100  # Total money in three years
years = 3  # Total years
rate_year1 = Fraction(1, 3)  # 3 畝 1 錢
rate_year2 = Fraction(1, 4)  # 4 畝 1 錢
rate_year3 = Fraction(1, 5)  # 5 畝 1 錢

# Calculate the total area of the field (田)
a = Fraction(money, rate_year1 + rate_year2 + rate_year3)

# Output the result
a  # The total area of the field in 畝
#----- content ends here -----


"""


This code calculates the total area of the field (田) in 畝 using the given rates for each year and the total money earned over three years. The result is stored in the variable `a`.
"""


"""
Variable 'a' has wrong value. Expected: 60/47, Actual: 6000/47"""
