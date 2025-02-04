"""
又有三人三分人之一分六錢三分錢之一四分錢之三問人得幾何
經分術曰以人數為法錢數為實實如法而一有分者通之重有分者同而通之
荅曰人得 a錢 
"""

"""
Suppose there are three people. One-third of a person gets 6 qian, one-third of a qian gets 1, and three-fourths of a qian gets 3.
Question: how much does each person get?

The procedure for proportional division says: Take the number of people as the divisor, and the total qian as the dividend.
Perform the division to obtain the amount for one person.
If there are fractions, unify them. If there are repeated fractions, combine and unify them.

Answer: each person gets *a* qian.
"""

# 三人
人數 = 3

# 三分人之一分六錢
第一部分 = Fraction(1, 3) * 6

# 三分錢之一
第二部分 = Fraction(1, 3) * 1

# 四分錢之三
第三部分 = Fraction(3, 4)

# 合計錢數
總錢數 = 第一部分 + 第二部分 + 第三部分

# 以人數為法，錢數為實
a = Fraction(總錢數, 人數)
"""
Variable 'a' has wrong value. Expected: 17/8, Actual: 37/36"""
