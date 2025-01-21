"""
又有席，一領坐客二十三人，有席一千五百領。問：客㡬何？
術曰：列席數一千五百領，以二十三人乘之即得。
答曰： a人 。
"""

"""
To solve this problem, we need to calculate the total number of guests ("a") based on the given information. Each席 (席, mat or seat) can accommodate 23 people, and there are 1500 such mats. The total number of guests is the product of the number of mats and the number of people per mat.

Here is the Python code:


"""


from fractions import Fraction

# Given data
seats = 1500  # number of mats
people_per_seat = 23  # number of people per mat

# Calculation
a = seats * people_per_seat  # total number of guests

# Result
a  # a is the total number of guests


"""


The value of `a` will be the total number of guests.
"""


"""
"""
