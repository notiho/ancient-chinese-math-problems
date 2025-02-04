"""
今有丁八千九百五十八人，凡三丁出一兵。問：出兵㡬何？
術曰：列八千九百五十八人，以三除之即得。
答曰： a人 。
"""

"""
To solve this problem, we are given that there are 8,958 people (丁), and for every 3 people, 1 soldier (兵) is recruited. The task is to calculate how many soldiers (兵) can be recruited.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Total number of people
total_people = 8958

# Number of people required to recruit one soldier
people_per_soldier = 3

# Calculate the number of soldiers
a = total_people // people_per_soldier  # Use integer division since we need whole soldiers
#----- content ends here -----


"""


The value of `a` will be the number of soldiers recruited.
"""


"""
"""
