"""
今有城周四十八里，欲令禦賊，每三步置一兵。問：用兵㡬何？
術曰：列城周四十八里，以三百步乘之，得一萬四千四百步，以三步除之即得。
答曰： a人 。
"""

"""
To solve this problem, we need to calculate how many soldiers ("a") are required if one soldier is placed every 3 steps along the perimeter of a city with a circumference of 48 li. Each li is equivalent to 300 steps.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
circumference_li = 48  # 城周四十八里
steps_per_li = 300  # 每里三百步
steps_per_soldier = 3  # 每三步置一兵

# Calculate total steps around the city
total_steps = circumference_li * steps_per_li

# Calculate the number of soldiers required
a = Fraction(total_steps, steps_per_soldier)

# Result
a  # a人
#----- content ends here -----


"""


The variable `a` will contain the number of soldiers required.
"""


"""
"""
