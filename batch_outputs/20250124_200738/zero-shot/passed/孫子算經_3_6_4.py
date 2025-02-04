"""
今有丁九萬八千七百六十六，凡二十五丁出一兵。問：兵幾何？
術曰：置丁九萬八千七百六十六為實，以二十五為法。實如法，即得。
答曰： a人 奇 b 丁。
"""

"""
To solve this problem, we need to determine how many soldiers ("兵") can be formed from a total of 98,766 people ("丁") where 25 people form one soldier. The remainder will be the leftover people ("奇丁"). Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Total number of people (丁)
total_people = 98766

# Number of people required to form one soldier
people_per_soldier = 25

# Calculate the number of soldiers (a) and the leftover people (b)
a = total_people // people_per_soldier  # Integer division to find the number of soldiers
b = total_people % people_per_soldier   # Remainder to find the leftover people

# Results:
# a: number of soldiers
# b: leftover people
#----- content ends here -----


"""


After running the code:
- `a` will contain the number of soldiers.
- `b` will contain the leftover people.
"""


"""
"""
