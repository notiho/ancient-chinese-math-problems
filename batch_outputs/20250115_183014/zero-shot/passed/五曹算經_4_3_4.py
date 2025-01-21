"""
今有粟九百斛，斛别加二斗五升。問：加㡬何？
術曰：列九百斛以二斗五升乘之即得。
答曰： a斛 。
"""

"""
To solve this problem, we need to calculate the total amount added when 900斛 (hú) of grain is increased by 2斗5升 (2 dǒu and 5 shēng) per hú. 

In ancient Chinese measurements:
- 1斗 = 10升.

Thus, 2斗5升 = 2 * 10 + 5 = 25升.

The total increase is calculated by multiplying 900斛 by 25升 per hú.

Here is the Python code to compute the solution:


"""


from fractions import Fraction

# Given values
total_hu = 900  # 900斛
increase_per_hu = 25  # 2斗5升 = 25升

# Total increase in 升
total_increase_sheng = total_hu * increase_per_hu

# Convert the total increase to 斛
# 1斛 = 100升
a = Fraction(total_increase_sheng, 100)

# The answer is stored in variable 'a'


"""


The solution is stored in the variable `a` as a fraction in terms of 斛.
"""


"""
"""
