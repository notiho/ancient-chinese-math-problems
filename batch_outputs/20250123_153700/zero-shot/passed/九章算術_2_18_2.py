"""
今有粟二斗，欲為櫱。問︰得幾何？
術曰：以粟求櫱，七之，二而一。
荅曰：為櫱 a斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem states that to convert "粟" (grain) into "櫱" (a unit of measure), the rule is to multiply by 7 and then divide by 2. The given amount of grain is 2斗. Let's compute the value of "a" (櫱).

Here is the Python code:


"""


from fractions import Fraction

# Given data
grain = Fraction(2)  # 粟 (grain) in 斗

# Conversion rule: multiply by 7, then divide by 2
a = grain * 7 / 2  # 櫱 (a) in 斗

# Result
a  # 櫱 in 斗


"""


The value of `a` will be the answer in terms of 櫱 (斗).
"""


"""
"""
