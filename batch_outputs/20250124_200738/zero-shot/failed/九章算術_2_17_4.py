"""
今有粟四斗，欲為熟菽。問︰得幾何？
術曰：以粟求熟菽，二百七之，百而一。
荅曰：為熟菽 a斗 。
"""

"""
To solve this problem, we need to compute the amount of 熟菽 (cooked beans) that can be obtained from 4 斗 of 粟 (grain). The rule states: "以粟求熟菽，二百七之，百而一," which means for every 207 parts of 粟, 1 part of 熟菽 is obtained.

Here is the Python code to compute the value of `a`:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
粟 = 4  # 粟 in 斗

# Conversion rule: 207 粟 -> 1 熟菽
a = Fraction(粟, 207)

# Output the result
a  # a is the amount of 熟菽 in 斗
#----- content ends here -----


"""


The variable `a` will contain the amount of 熟菽 in 斗.
"""


"""
Variable 'a' has wrong value. Expected: 207/25, Actual: 4/207"""
