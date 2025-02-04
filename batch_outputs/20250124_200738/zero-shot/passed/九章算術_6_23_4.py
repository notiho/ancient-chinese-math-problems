"""
今有假田，初假之歲三畝一錢，明年四畝一錢，後年五畝一錢。凡三歲得一百，問︰田幾何？
術曰：置畝數及錢數，令畝數互乘錢數，并以為法。畝數相乘，又以百錢乘之，為實。實如法得一畝。
荅曰： a頃 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves determining the area of the field in "頃" (a traditional Chinese unit of area) based on the given rates of payment over three years.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
rate1 = Fraction(3, 1)  # 3 畝 per 錢 in the first year
rate2 = Fraction(4, 1)  # 4 畝 per 錢 in the second year
rate3 = Fraction(5, 1)  # 5 畝 per 錢 in the third year
total_money = 100  # Total 錢 over three years

# Method (術)
# 畝數互乘錢數，并以為法
denominator = (rate1 * rate2) + (rate2 * rate3) + (rate3 * rate1)

# 畝數相乘，又以百錢乘之，為實
numerator = rate1 * rate2 * rate3 * total_money

# 實如法得一畝
a = numerator / denominator  # Result in 畝

# Convert 畝 to 頃 (1 頃 = 100 畝)
a = a / 100

# The result is stored in variable 'a'
#----- content ends here -----


"""


The variable `a` will contain the solution in "頃".
"""


"""
"""
