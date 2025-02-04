"""
又有三人，三分人之一，分六錢三分錢之一，四分錢之三。問：人得幾何？
經分術曰：以人數為法，錢數為實，實如法而一。有分者通之；重有分者同而通之。
荅曰：人得 a錢 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given data
people = 3  # 三人
money = Fraction(6) + Fraction(3, 10) + Fraction(3, 4)  # 六錢三分錢之一，四分錢之三

# Calculate money per person
a = money / people  # 人得幾何？

# Result
a  # 人得 a錢


"""


The variable `a` will hold the amount of money each person gets in terms of fractions.
"""


"""
Variable 'a' has wrong value. Expected: 17/8, Actual: 47/20"""
