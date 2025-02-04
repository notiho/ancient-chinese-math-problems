"""
又有席，一領坐客二十三人，有席一千五百領。問：客㡬何？
術曰：列席數一千五百領，以二十三人乘之即得。
答曰： a人 。
"""

"""
To solve this problem, we calculate the total number of guests by multiplying the number of seats per mat (23 people) by the total number of mats (1500 mats). Here's the Python code:


"""


from fractions import Fraction

# Given data
seats_per_mat = 23  # people per mat
total_mats = 1500   # total mats

# Calculation
a = seats_per_mat * total_mats  # total guests

# Result
a  # a is the total number of guests


"""


The value of `a` will be `34500` people.
"""


"""
"""
