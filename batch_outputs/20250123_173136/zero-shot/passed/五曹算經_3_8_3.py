"""
今有席，一領坐客一十二人，有席一千五百三十八領。問：客㡬何？
術曰：列席一千五百三十八領，以一十二人乘之即得。
答曰： a人 。
"""

"""
To solve this problem, we calculate the total number of guests ("a") by multiplying the number of seats per mat (12) by the total number of mats (1538). Here's the Python code:


"""


from fractions import Fraction

# Given data
seats_per_mat = 12  # people per mat
total_mats = 1538   # total number of mats

# Calculation
a = seats_per_mat * total_mats  # total number of guests

# Result
a  # a is the total number of guests


"""


The value of `a` will be `18456 人`.
"""


"""
"""
