"""
又有三人三分人之一分六錢三分錢之一四分錢之三問人得幾何
經分術曰以人數為法錢數為實實如法而一有分者通之重有分者同而通之
荅曰人得 a錢 
"""

"""
Suppose there are three people. One-third of a person gets 6 qian, one-third of a qian gets 1/4 of a qian, and three-fourths of a qian are distributed.
Question: how much does each person get?

The procedure for proportional division says: Take the number of people as the divisor. Take the total amount of qian as the dividend. Divide the dividend by the divisor to find the amount each person gets. If there are fractions, combine them. If there are repeated fractions, combine them as well.

Answer: each person gets *a* qian.
"""

from fractions import Fraction

# 三人
人數 = 3

# 一分人之一分六錢
第一部分 = Fraction(1, 3) * 6

# 三分錢之一四分錢之三
第二部分 = Fraction(1, 3) * Fraction(1, 4) * 3

# 總錢數
總錢數 = 第一部分 + 第二部分

# 以人數為法，錢數為實
a = 總錢數 / 人數
"""
Variable 'a' has wrong value. Expected: 17/8, Actual: 3/4"""
