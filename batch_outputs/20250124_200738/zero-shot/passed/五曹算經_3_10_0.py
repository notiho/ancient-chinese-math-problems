"""
今有席，一領坐客二十三人，有客五十三萬三千六百八十人。問：席㡬何？
術曰：列五十三萬三千六百八十人，以二十三人除之即得。
答曰： a領 奇 b人 。
"""

"""
To solve this problem, we need to calculate how many full seats ("領") can be formed and how many people ("人") are left over when dividing the total number of people (533,680) by the number of people per seat (23). Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Total number of people
total_people = 533680

# Number of people per seat
people_per_seat = 23

# Calculate the number of full seats
a = total_people // people_per_seat

# Calculate the remaining people
b = total_people % people_per_seat

# The results are stored in variables a (seats) and b (remaining people)
#----- content ends here -----


"""


After running this code:
- `a` will contain the number of full seats.
- `b` will contain the number of people left over.
"""


"""
"""
