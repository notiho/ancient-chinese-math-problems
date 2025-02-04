"""
今有金二斤，令九十六人分之。問：人得㡬何？
答曰： a銖 。
"""

#----- content starts here -----
"""
Suppose there are 2 jin of gold, and it is to be divided among 96 people.
Question: how much does each person get?

Answer: each person gets *a* zhu.
"""

# 金二斤 (1 jin = 16 liang, 1 liang = 24 zhu)
金 = 2 * 16 * 24  # Convert jin to zhu

# 分給九十六人
人數 = 96

# 每人所得
a = Fraction(金, 人數)  # Each person gets this many zhu

a  # Output the result#----- content ends here -----

"""
"""
