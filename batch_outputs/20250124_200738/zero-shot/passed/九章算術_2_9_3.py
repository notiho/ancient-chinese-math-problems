"""
今有粟九斗八升，欲為御飯。問︰得幾何？
術曰：以粟求御飯，二十一之，二十五而一。
荅曰：為御飯 a斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem states that we have 9斗8升 of 粟 (grain) and want to calculate how much 御飯 (cooked rice) can be made. The method provided is to multiply the amount of 粟 by 21 and then divide by 25.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
grain = Fraction(9, 1) + Fraction(8, 10)  # 9斗8升, where 1斗 = 10升

# Calculation
a = grain * Fraction(21, 25)  # Multiply by 21 and divide by 25

# Result
a  # a斗 of 御飯
#----- content ends here -----


"""


The variable `a` will contain the amount of 御飯 in terms of 斗.
"""


"""
"""
