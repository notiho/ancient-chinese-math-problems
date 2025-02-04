"""
今有粟九百斛，斛别加二斗五升。問：加㡬何？
術曰：列九百斛以二斗五升乘之即得。
答曰： a斛 。
"""

"""
To solve this problem, we need to calculate the total amount added when each of the 900斛 is increased by 2斗5升. First, we convert 2斗5升 into a single unit (斛), then multiply it by 900 to find the total addition.

1斛 = 10斗, and 1斗 = 10升. Therefore, 2斗5升 = \( 2 + \frac{5}{10} \) 斛 = \( \frac{20}{10} + \frac{5}{10} \) 斛 = \( \frac{25}{10} \) 斛 = \( \frac{5}{2} \) 斛.

Now, multiply \( \frac{5}{2} \) 斛 by 900 to get the total addition.

Here is the Python code:


"""


from fractions import Fraction

# Given values
total_corn = 900  # in 斛
increase_per_hu = Fraction(5, 2)  # 2斗5升 converted to 斛

# Calculate the total addition
a = total_corn * increase_per_hu

# The result is stored in variable 'a'
a


"""


The value of `a` will represent the total amount added in 斛.
"""


"""
Variable 'a' has wrong value. Expected: 225, Actual: 2250"""
