"""
今有菽一斗，欲為熟菽。問︰得幾何？
荅曰：為熟菽 a斗 。
"""

"""
Suppose there is 1 dou of raw beans (菽). It is desired to cook them into cooked beans (熟菽).
Question: how much cooked beans does it yield?

Answer: it yields *a* dou of cooked beans.
"""

from fractions import Fraction

# 菽一斗
raw_beans = 1  # in dou

# Cooking beans increases their volume by 3/2
a = Fraction(3, 2) * raw_beans

# Output the result
a  # This is the amount of cooked beans in dou.
"""
Variable 'a' has wrong value. Expected: 23/10, Actual: 3/2"""
