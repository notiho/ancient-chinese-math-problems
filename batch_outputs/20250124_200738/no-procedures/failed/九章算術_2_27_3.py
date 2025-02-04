"""
今有菽一斗，欲為熟菽。問︰得幾何？
荅曰：為熟菽 a斗 。
"""

#----- content starts here -----
"""
Suppose there is one dou of raw beans (菽). It is desired to turn it into cooked beans (熟菽).
Question: how much cooked beans does one obtain?

The answer says: *a* dou of cooked beans.
"""

from fractions import Fraction

# 菽一斗
raw_beans = 1  # in dou

# Cooked beans are 3/5 of the raw beans
a = Fraction(3, 5) * raw_beans

# Result
a  # This is the amount of cooked beans in dou.#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 23/10, Actual: 3/5"""
