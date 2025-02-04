"""
今有丁八千九百五十八人，凡三丁出一兵。問：出兵㡬何？
術曰：列八千九百五十八人，以三除之即得。
答曰： a人 。
"""

"""
To solve this problem, we need to divide the total number of people (8,958) by 3 to determine how many soldiers ("兵") can be formed. The solution will be stored in the variable `a`.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Total number of people
total_people = 8958

# Number of people required to form one soldier
people_per_soldier = 3

# Calculate the number of soldiers
a = total_people // people_per_soldier  # Integer division since we need whole soldiers
#----- content ends here -----


"""


The value of `a` will represent the number of soldiers.
"""


"""
"""
