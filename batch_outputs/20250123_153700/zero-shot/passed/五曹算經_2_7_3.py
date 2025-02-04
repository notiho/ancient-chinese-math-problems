"""
今有城周四十八里，欲令禦賊，每三步置一兵。問：用兵㡬何？
術曰：列城周四十八里，以三百步乘之，得一萬四千四百步，以三步除之即得。
答曰： a人 。
"""

"""
To solve this problem, we need to calculate the number of soldiers required to guard a city with a circumference of 48 li, where one soldier is placed every 3 steps. The problem states that 1 li equals 300 steps. Here's the Python code:


"""


from fractions import Fraction

# Given data
circumference_li = 48  # 城周四十八里
steps_per_li = 300  # 一里等于三百步
steps_per_soldier = 3  # 每三步置一兵

# Total steps around the city
total_steps = circumference_li * steps_per_li

# Number of soldiers required
a = Fraction(total_steps, steps_per_soldier)

# Result
a  # Answer in terms of the number of soldiers


"""


The variable `a` represents the number of soldiers required.
"""


"""
"""
