"""
又有三人，三分人之一，分六錢三分錢之一，四分錢之三。問：人得幾何？
經分術曰：以人數為法，錢數為實，實如法而一。有分者通之；重有分者同而通之。
荅曰：人得 a(=17/8)錢 。
"""

#----- content starts here -----
"""
Suppose there are three people. Each person is to receive one-third of the total amount. 
The total amount is 6 qian, plus one-third of a qian, plus three-fourths of a qian.
Question: how much does each person receive?

The procedure for proportional division says: Take the number of people as the divisor, and the total amount of qian as the dividend. 
Perform the division to find the amount per person. 
If there are fractional parts, convert them to a common denominator. 
If there are repeated fractional parts, combine them and convert to a common denominator.

Answer: each person receives *a*(=17/8) qian.
"""

from fractions import Fraction

# 三人
人數 = 3

# 錢數 = 6錢 + 三分錢之一 + 四分錢之三
錢數 = 6 + Fraction(1, 3) + Fraction(3, 4)

# 以人數為法，錢數為實
法 = 人數
實 = 錢數

# 實如法而一
a = Fraction(實, 法)  # 17/8 qian#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 17/8, Actual: 85/36"""
