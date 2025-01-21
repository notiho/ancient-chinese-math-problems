"""
今有城周四十八里，欲令禦賊，每三步置一兵。問：用兵㡬何？
術曰：列城周四十八里，以三百步乘之，得一萬四千四百步，以三步除之即得。
答曰： a人 。
"""

"""
To solve this problem, we will calculate the number of soldiers ("a") required to guard a city with a circumference of 48 li, placing one soldier every 3 steps. Each li is equivalent to 300 steps.

Here is the Python code:


"""


from fractions import Fraction

# Given values
circumference_li = 48  # 城周四十八里
steps_per_li = 300  # 每里三百步
steps_per_soldier = 3  # 每三步置一兵

# Total steps around the city
total_steps = circumference_li * steps_per_li

# Number of soldiers required
a = Fraction(total_steps, steps_per_soldier)

# Result
a  # a人


"""


The variable `a` will contain the number of soldiers required.
"""


"""
"""
