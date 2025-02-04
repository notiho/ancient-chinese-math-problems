"""
今有粟八斗六升，欲為鑿飯。問︰得幾何？
術曰：以粟求鑿飯，二十四之，二十五而一。
荅曰：為鑿飯 a斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem states that we have 8斗6升 of 粟 (grain) and want to convert it into 鑿飯. The method provided is to multiply the amount of 粟 by 24 and then divide by 25.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
粟 = Fraction(8, 1) + Fraction(6, 10)  # 8斗6升 (1斗 = 10升)

# Conversion formula
a = 粟 * 24 / 25  # Multiply by 24 and divide by 25

# Result
a  # 鑿飯 in 斗
#----- content ends here -----


"""


The variable `a` will contain the result in terms of 鑿飯 (斗).
"""


"""
"""
