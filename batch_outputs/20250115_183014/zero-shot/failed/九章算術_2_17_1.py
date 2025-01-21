"""
今有粟四斗，欲為熟菽。問︰得幾何？
術曰：以粟求熟菽，二百七之，百而一。
荅曰：為熟菽 a斗 。
"""

"""
To solve this problem, we translate the ancient Chinese math problem into Python code. The problem states that for every 100 units of 粟 (grain), you get 1 unit of 熟菽 (cooked beans). The given amount of 粟 is 4 斗 (a unit of volume). Using the formula provided, we calculate the amount of 熟菽.

Here is the Python code:


"""


from fractions import Fraction

# Given data
粟 = Fraction(4)  # 4 斗 of 粟

# Formula: 熟菽 = 粟 * (1 / 100)
a = 粟 * Fraction(1, 100)

# Result
a  # 熟菽 in 斗


"""


The variable `a` will contain the amount of 熟菽 in 斗.
"""


"""
Variable 'a' has wrong value. Expected: 207/25, Actual: 1/25"""
