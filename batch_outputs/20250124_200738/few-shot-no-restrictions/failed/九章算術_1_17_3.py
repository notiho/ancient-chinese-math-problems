"""
又有三人，三分人之一，分六錢三分錢之一，四分錢之三。問：人得幾何？
經分術曰：以人數為法，錢數為實，實如法而一。有分者通之；重有分者同而通之。
荅曰：人得 a錢 。
"""

#----- content starts here -----
"""
Suppose there are three people, each receiving one-third of the total.
The total amount to be divided is 6 qian, plus one-third of a qian, plus three-fourths of a qian.
Question: how much does each person receive?

The procedure for proportional division says: Take the number of people as the divisor, and the total amount of qian as the dividend.
Perform the division, obtaining the amount per person.
If there are fractions, unify them; if there are repeated fractions, unify them again.

Answer: Each person receives *a* qian.
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
a = Fraction(實, 法)

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 17/8, Actual: 85/36"""
