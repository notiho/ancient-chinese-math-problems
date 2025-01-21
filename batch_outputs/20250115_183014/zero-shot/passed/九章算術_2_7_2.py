"""
今有粟三斗六升，欲為粺飯。問︰得幾何？
術曰：以粟求粺飯，二十七之，二十五而一。
荅曰：為粺飯 a斗 。
"""

"""
To solve this problem, we need to compute the amount of 粺飯 (refined rice) obtained from 3斗6升 of 粟 (unrefined rice). The method described in the problem involves multiplying the amount of 粟 by 27 and then dividing by 25.

1斗 = 10升, so 3斗6升 = 3.6斗.

Here is the Python code to compute the value of `a`:


"""


from fractions import Fraction

# Given amount of 粟 in 斗
粟 = Fraction(36, 10)  # 3斗6升 = 3.6斗

# Formula to compute 粺飯
a = 粟 * Fraction(27, 25)

# Result
a  # 粺飯 in 斗


"""


The variable `a` will contain the amount of 粺飯 in 斗 as a `Fraction`.
"""


"""
"""
