"""
今有七人分八錢三分錢之一問人得幾何
經分術曰以人數為法錢數為實實如法而一有分者通之重有分者同而通之
荅曰人得 a錢 
"""

"""
Suppose there are 7 people dividing 8 qian and 1/3 of a qian.
Question: how much does each person get?

The procedure for division says: Take the number of people as the divisor and the number of qian as the dividend.
Divide the dividend by the divisor to get the result.
If there is a remainder, convert it into smaller units (fractions) and distribute it equally.
If there are repeated remainders, continue converting and distributing until resolved.

Answer: each person gets *a* qian.
"""

from fractions import Fraction

# 人數
人數 = 7

# 錢數
錢數 = 8 + Fraction(1, 3)

# 以人數為法，錢數為實
法 = 人數
實 = 錢數

# 實如法而一
a = Fraction(實, 法)  # Each person gets this amount of qian

a
"""
"""
