"""
今有粟二斗，欲為櫱。問︰得幾何？
術曰：以粟求櫱，七之，二而一。
荅曰：為櫱 a斗 。
"""

"""
To solve this problem, we need to translate the ancient Chinese math problem into Python code. The problem states that we have 2斗 of 粟 (grain) and want to convert it into 櫱 (seedlings). The method described is "七之，二而一," which means multiplying by 7 and then dividing by 2.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
粟 = 2  # in 斗

# Calculation
a = Fraction(粟 * 7, 2)  # Multiply by 7 and divide by 2

# Result
a  # in 斗
#----- content ends here -----


"""


The variable `a` will contain the result in 斗.
"""


"""
"""
