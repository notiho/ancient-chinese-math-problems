"""
今有粟三斗六升，欲為粺飯。問︰得幾何？
術曰：以粟求粺飯，二十七之，二十五而一。
荅曰：為粺飯 a斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem states that we have 3斗6升 of 粟 (grain) and want to calculate how much 粺飯 (refined rice) we can obtain. The method provided involves multiplying the amount of 粟 by 27 and dividing by 25.

In ancient Chinese measurements:
- 1斗 = 10升.

Thus, 3斗6升 = 3斗 + 6升 = 3 + 6/10 斗 = 3.6斗.

The formula provided is:
粟 × 27 ÷ 25 = 粺飯.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given 粟 in 斗
grain = Fraction(3) + Fraction(6, 10)  # 3斗6升 = 3.6斗

# Formula to calculate 粺飯
a = grain * Fraction(27, 25)

# Result
a  # 粺飯 in 斗
#----- content ends here -----


"""


The variable `a` will contain the amount of 粺飯 in 斗 as a `Fraction`.
"""


"""
"""
