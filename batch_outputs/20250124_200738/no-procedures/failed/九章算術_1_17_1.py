"""
又有三人，三分人之一，分六錢三分錢之一，四分錢之三。問：人得幾何？
荅曰：人得 a錢 。
"""

#----- content starts here -----
"""
Suppose there are three people. Each person gets one-third of the total amount. The total amount is 6 qian, plus one-third of a qian, plus three-fourths of a qian.
Question: how much does each person get?

Answer: each person gets *a* qian.
"""

from fractions import Fraction

# Total amount of money
total_qian = 6 + Fraction(1, 3) + Fraction(3, 4)

# Divide the total amount equally among 3 people
a = total_qian / 3

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 17/8, Actual: 85/36"""
