"""
今有城周四十八里，欲令禦賊，每三步置一兵。問：用兵㡬何？
術曰：列城周四十八里，以三百步乘之，得一萬四千四百步，以三步除之即得。
答曰： a人 。
"""

"""
To solve this problem, we need to calculate the number of soldiers required to guard a city with a perimeter of 48 li (ancient Chinese unit of length). Soldiers are placed every 3 steps, and 1 li equals 300 steps.

Here is the Python code to compute the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
city_perimeter_li = 48  # in li
steps_per_li = 300  # steps in one li
steps_per_soldier = 3  # steps between each soldier

# Calculations
total_steps = city_perimeter_li * steps_per_li
a = total_steps // steps_per_soldier  # number of soldiers

# Result
a  # This is the number of soldiers required
#----- content ends here -----


"""


The variable `a` will contain the number of soldiers required.
"""


"""
"""
