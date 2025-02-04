"""
今有粟九百斛，斛别加二斗五升。問：加㡬何？
術曰：列九百斛以二斗五升乘之即得。
答曰： a斛 。
"""

"""
To solve this problem, we need to calculate the total amount added when 2斗 (dou) and 5升 (sheng) are added to each of the 900斛 (hu). 

In ancient Chinese measurements:
- 1斛 = 10斗
- 1斗 = 10升

So, 2斗5升 = 2.5斗 = 0.25斛.

The total addition is calculated as \( 900 \times 0.25 \).

Here is the Python code to compute the solution:


"""


from fractions import Fraction

# Given values
total_hu = 900  # 900斛
additional_per_hu = Fraction(2, 10) + Fraction(5, 100)  # 2斗5升 converted to 斛

# Calculate the total addition
a = total_hu * additional_per_hu

# Result
a  # Total added in 斛


"""


The value of `a` will be the total amount added in 斛.
"""


"""
"""
