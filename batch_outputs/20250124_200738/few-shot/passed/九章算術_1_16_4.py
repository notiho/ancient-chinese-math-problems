"""
今有七人，分八錢三分錢之一。問：人得幾何？
經分術曰：以人數為法，錢數為實，實如法而一。有分者通之；重有分者同而通之。
荅曰：人得 a錢 。
"""

#----- content starts here -----
"""
Suppose there are 7 people, and they are to divide 8 qian and 1/3 of a qian.
Question: how much does each person get?

The procedure for division says: Take the number of people as the divisor, and the amount of qian as the dividend.
Divide the dividend by the divisor to get the result. 
If there are fractional parts, convert them to a common unit; if there are repeated fractional parts, combine them and convert them to a common unit.

Answer: each person gets *a* qian.
"""

from fractions import Fraction

# 七人
人數 = 7

# 八錢三分錢之一
錢數 = 8 + Fraction(1, 3)

# 以人數為法
法 = 人數

# 錢數為實
實 = 錢數

# 實如法而一
a = Fraction(實, 法)  # 每人所得錢數#----- content ends here -----

"""
"""
