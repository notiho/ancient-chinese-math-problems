"""
今有席，一領坐客二十三人，有客五十三萬三千六百八十人。問：席㡬何？
術曰：列五十三萬三千六百八十人，以二十三人除之即得。
答曰： a領 奇 b人 。
"""

"""
To solve this problem, we need to determine how many full seats ("a") and how many remaining people ("b") there are when 533,680 people are seated, with each seat accommodating 23 people.

Here is the Python code to compute the values of "a" and "b":


"""


from fractions import Fraction

# Total number of people
total_people = 533680

# Number of people per seat
people_per_seat = 23

# Calculate the number of full seats (a) and the remaining people (b)
a = total_people // people_per_seat  # Full seats
b = total_people % people_per_seat  # Remaining people

# Results
a, b


"""


After running this code:
- `a` will represent the number of full seats.
- `b` will represent the number of remaining people.
"""


"""
"""
