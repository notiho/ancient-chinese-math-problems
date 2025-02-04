"""
今有粟九斗八升，欲為大䵂。問︰得幾何？
術曰：以粟求大䵂，二十七之，二十五而一。
荅曰：為大䵂 a斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem states that we have 9斗8升 of 粟 (grain) and want to convert it into 大䵂 (a larger unit). The method provided says to multiply the amount of 粟 by 27 and divide by 25 to find the amount of 大䵂.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
粟 = Fraction(9, 1) + Fraction(8, 10)  # 9斗8升, where 1斗 = 10升

# Conversion formula
a = 粟 * Fraction(27, 25)  # Multiply by 27 and divide by 25

# Result
a  # a is the amount of 大䵂 in 斗
#----- content ends here -----


"""


The variable `a` will contain the result in terms of 大䵂.
"""


"""
"""
