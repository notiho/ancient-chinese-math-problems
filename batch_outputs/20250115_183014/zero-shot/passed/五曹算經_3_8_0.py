"""
今有席，一領坐客一十二人，有席一千五百三十八領。問：客㡬何？
術曰：列席一千五百三十八領，以一十二人乘之即得。
答曰： a人 。
"""

"""
To solve this problem, we need to calculate the total number of guests (客) based on the given number of seats (席) and the number of people per seat. Here's the Python code:


"""


from fractions import Fraction

# Given data
seats = 1538  # 席, number of seats
people_per_seat = 12  # 一領坐客一十二人

# Calculation
a = seats * people_per_seat  # Total number of guests

# Answer
a  # a人


"""


The variable `a` will hold the total number of guests.
"""


"""
"""
