"""
今有席，一領坐客二十三人，有客五十三萬三千六百八十人。問：席㡬何？
術曰：列五十三萬三千六百八十人，以二十三人除之即得。
答曰： a領 奇 b人 。
"""

"""
To solve this problem, we will compute the number of seats ("a") and the remaining people ("b") when 533,680 people are divided into groups of 23. Here's the Python code:


"""


from fractions import Fraction

# Total number of people
total_people = 533680

# Number of people per seat
people_per_seat = 23

# Compute the number of seats (a) and the remaining people (b)
a = total_people // people_per_seat  # Integer division for the number of seats
b = total_people % people_per_seat   # Remainder for the remaining people

# Results
a  # Number of seats
b  # Remaining people


"""


After running this code:
- `a` will hold the number of seats.
- `b` will hold the number of remaining people.
"""


"""
"""
