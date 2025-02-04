"""
今有丁八千九百五十八人，凡三丁出一兵。問：出兵㡬何？
術曰：列八千九百五十八人，以三除之即得。
答曰： a人 。
"""

"""
To solve this problem, we need to divide the total number of people (8,958) by 3, as every 3 people produce 1 soldier. Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Total number of people
total_people = 8958

# Number of people required to produce one soldier
people_per_soldier = 3

# Calculate the number of soldiers
a = Fraction(total_people, people_per_soldier)

# Result
a  # This represents the number of soldiers
#----- content ends here -----


"""


The variable `a` will store the number of soldiers as a fraction or integer, depending on the divisibility.
"""


"""
"""
