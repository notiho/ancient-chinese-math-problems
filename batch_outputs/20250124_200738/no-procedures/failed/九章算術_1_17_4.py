"""
又有三人，三分人之一，分六錢三分錢之一，四分錢之三。問：人得幾何？
荅曰：人得 a錢 。
"""

#----- content starts here -----
"""
Suppose there are three people. Each person gets one-third of the total. The total amount of money is 6 qian, plus one-third of a qian, plus three-fourths of a qian.
Question: how much does each person get?

Answer: each person gets *a* qian.
"""

from fractions import Fraction

# Total money: 6 qian + 1/3 qian + 3/4 qian
total_money = 6 + Fraction(1, 3) + Fraction(3, 4)

# Divide the total money equally among 3 people
a = total_money / 3

# Result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 17/8, Actual: 85/36"""
