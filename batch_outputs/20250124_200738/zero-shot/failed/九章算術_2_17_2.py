"""
今有粟四斗，欲為熟菽。問︰得幾何？
術曰：以粟求熟菽，二百七之，百而一。
荅曰：為熟菽 a斗 。
"""

"""
To solve this problem, let's translate the ancient Chinese math problem into Python code.

The problem states that we have 4斗 of 粟 (grain), and we want to calculate how much 熟菽 (cooked beans) we can get. The rule is: multiply the amount of 粟 by 200/7, then divide by 100 to get the amount of 熟菽.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
粟 = 4  # in 斗

# Calculation
a = 粟 * Fraction(200, 7) / 100  # in 斗

# Result
a  # This is the amount of 熟菽 in 斗
#----- content ends here -----


"""


The variable `a` will contain the result in 斗.
"""


"""
Variable 'a' has wrong value. Expected: 207/25, Actual: 8/7"""
