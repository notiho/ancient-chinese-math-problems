"""
今有七人，分八錢三分錢之一。問：人得幾何？
經分術曰：以人數為法，錢數為實，實如法而一。有分者通之；重有分者同而通之。
荅曰：人得 a(=25/21)錢 。
"""

"""
Suppose there are 7 people, and they are to divide 8 qian and 1/3 of a qian.
Question: how much does each person get?

The procedure for division says: Take the number of people as the divisor, and the amount of qian as the dividend. 
Divide the dividend by the divisor to obtain the result. 
If there are fractional parts, unify them; if there are repeated fractional parts, combine and unify them.

Answer: each person gets *a*(=25/21) qian.
"""

# 七人
人數 = 7

# 八錢三分錢之一
錢數 = 8 + Fraction(1, 3)

# 以人數為法
法 = 人數

# 錢數為實
實 = 錢數

# 實如法而一
a = Fraction(實, 法) # 25/21
"""
"""
