"""
又有三人，三分人之一，分六錢三分錢之一，四分錢之三。問：人得幾何？
經分術曰：以人數為法，錢數為實，實如法而一。有分者通之；重有分者同而通之。
荅曰：人得 a錢 。
"""

#----- content starts here -----
"""
Suppose there are three people. Each person gets 1/3 of the total people, and the total money to be divided is 6 qian, plus 1/3 of a qian, plus 3/4 of a qian.
Question: how much does each person get?

The procedure for division says: Take the number of people as the divisor, and the total money as the dividend. Divide the dividend by the divisor to get the result. If there are fractions, unify them; if there are repeated fractions, unify them again.

Answer: each person gets *a* qian.
"""

from fractions import Fraction

# 三人
人數 = 3

# 錢數 = 6錢 + 1/3錢 + 3/4錢
錢數 = 6 + Fraction(1, 3) + Fraction(3, 4)

# 以人數為法，錢數為實
法 = 人數
實 = 錢數

# 實如法而一
a = 實 / 法

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 17/8, Actual: 85/36"""
