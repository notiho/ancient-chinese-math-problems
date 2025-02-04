"""
今有假田，初假之歲三畝一錢，明年四畝一錢，後年五畝一錢。凡三歲得一百，問︰田幾何？
術曰：置畝數及錢數，令畝數互乘錢數，并以為法。畝數相乘，又以百錢乘之，為實。實如法得一畝。
荅曰： a頃 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves determining the area of the field (田) in "頃" (a unit of area). Here's the Python code:


"""


from fractions import Fraction

# Given data
money = 100  # Total money in three years
rate1 = Fraction(1, 3)  # 3 畝 per 1 錢 in the first year
rate2 = Fraction(1, 4)  # 4 畝 per 1 錢 in the second year
rate3 = Fraction(1, 5)  # 5 畝 per 1 錢 in the third year

# Calculate the "法" (denominator)
denominator = (rate1 * rate2) + (rate2 * rate3) + (rate3 * rate1)

# Calculate the "實" (numerator)
numerator = rate1 * rate2 * rate3 * money

# Solve for the area of the field in 畝
a = numerator / denominator

# Convert 畝 to 頃 (1 頃 = 100 畝)
a = a / 100

# The result is stored in variable "a"


"""


The variable `a` will contain the solution in "頃".
"""


"""
Variable 'a' has wrong value. Expected: 60/47, Actual: 1/12"""
