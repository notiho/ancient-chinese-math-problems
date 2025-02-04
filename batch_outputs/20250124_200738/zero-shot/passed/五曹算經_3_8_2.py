"""
今有席，一領坐客一十二人，有席一千五百三十八領。問：客㡬何？
術曰：列席一千五百三十八領，以一十二人乘之即得。
答曰： a人 。
"""

"""
To solve this problem, we need to calculate the total number of guests (`a`) based on the given number of mats (`1538`) and the number of guests per mat (`12`). Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
seats = 1538  # number of mats
guests_per_seat = 12  # guests per mat

# Calculation
a = seats * guests_per_seat  # total number of guests

# Result
a  # a is the total number of guests
#----- content ends here -----


"""


The solution is stored in the variable `a`, which represents the total number of guests.
"""


"""
"""
