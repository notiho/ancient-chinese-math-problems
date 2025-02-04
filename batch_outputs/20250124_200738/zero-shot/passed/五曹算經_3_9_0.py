"""
又有席，一領坐客二十三人，有席一千五百領。問：客㡬何？
術曰：列席數一千五百領，以二十三人乘之即得。
答曰： a人 。
"""

"""
To solve this problem, we need to calculate the total number of guests ("客") based on the given information:

- Each "席" (seat or mat) can accommodate 23 people.
- There are 1500 "席" (seats or mats).

The total number of guests is calculated by multiplying the number of seats by the number of people per seat.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
seats = 1500  # Number of seats (席)
people_per_seat = 23  # Number of people per seat

# Calculate the total number of guests
a = seats * people_per_seat

# The result is stored in variable 'a'
#----- content ends here -----


"""


The value of `a` will be the total number of guests.
"""


"""
"""
