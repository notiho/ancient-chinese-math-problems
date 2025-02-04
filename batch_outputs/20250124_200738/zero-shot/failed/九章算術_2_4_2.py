"""
今有粟一斗，欲為小䵂。問︰得幾何？
術曰：以粟求小䵂，二十七之，百而一。
荅曰：為小䵂 a升 。
"""

"""
To solve this problem, we need to compute the amount of "小䵂" (a type of measurement) obtained from 1斗 of 粟 (grain). The method described is to multiply the amount of 粟 by 27 and then divide by 100.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# 粟 (grain) in 斗
粟 = 1  # 1斗

# Calculation for 小䵂
a = Fraction(粟 * 27, 100)  # Multiply by 27 and divide by 100

# Result
a  # a升
#----- content ends here -----


"""


The variable `a` will hold the result in units of 升.
"""


"""
Variable 'a' has wrong value. Expected: 27/10, Actual: 27/100"""
