"""
今有席，一領坐客二十三人，有客五十三萬三千六百八十人。問：席㡬何？
術曰：列五十三萬三千六百八十人，以二十三人除之即得。
答曰： a領 奇 b人 。
"""

"""
To solve this problem, we need to calculate how many full seats ("領") can be formed, and how many people ("人") are left over. Here's the Python code:


"""


from fractions import Fraction

# Total number of people
total_people = 533680

# Number of people per seat
people_per_seat = 23

# Calculate the number of full seats
a = total_people // people_per_seat

# Calculate the remaining people
b = total_people % people_per_seat

# Results
a, b


"""


This will compute the values of `a` (number of full seats) and `b` (remaining people).
"""


"""
"""
