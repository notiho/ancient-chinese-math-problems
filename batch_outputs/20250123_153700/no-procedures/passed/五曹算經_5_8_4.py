"""
今有金二斤，令九十六人分之。問：人得㡬何？
答曰： a銖 。
"""

"""
Suppose there are 2 jin of gold, and it is to be divided among 96 people.
Question: how much does each person get?

Answer: each person gets *a* zhu.
"""

# 金二斤 (2 jin)
金 = 2

# 1 jin = 16 liang, and 1 liang = 24 zhu
金_in_銖 = 金 * 16 * 24

# 分給九十六人 (96 people)
人數 = 96

# Each person gets:
a = Fraction(金_in_銖, 人數)  # Result in zhu

a  # Output the result
"""
"""
