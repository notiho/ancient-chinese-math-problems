"""
又有三人，三分人之一，分六錢三分錢之一，四分錢之三。問：人得幾何？
經分術曰：以人數為法，錢數為實，實如法而一。有分者通之；重有分者同而通之。
荅曰：人得 a錢 。
"""

#----- content starts here -----
"""
Suppose there are three people. Each person is to receive one-third of the total.
The total amount to be divided is 6 qian, 1/3 of a qian, and 3/4 of a qian.
Question: how much does each person get?

The procedure for proportional division says: Take the number of people as the divisor, and the total amount of qian as the dividend.
Perform the division, obtaining the amount for each person.
If there are fractional parts, unify them into a common denominator.
If there are repeated fractional parts, unify them together into a single fraction.

Answer: each person gets *a* qian.
"""

from fractions import Fraction

# 三人
人數 = 3

# 錢數：六錢三分錢之一，四分錢之三
錢數 = 6 + Fraction(1, 3) + Fraction(3, 4)

# 以人數為法，錢數為實
法 = 人數
實 = 錢數

# 實如法而一
每人所得 = Fraction(實, 法)

# 有分者通之 (simplify the fraction)
a = 每人所得
#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 17/8, Actual: 85/36"""
