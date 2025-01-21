"""
今有不善行者先行一十里，善行者追之一百里，先至不善行者二十里。問︰善行者幾何里及之？
術曰：置不善行者先行一十里，以善行者先至二十里增之，以為法。以不善行者先行一十里，乘善行者一百里，為實。實如法得一里。
荅曰： a里 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given values
distance_not_good_walker = 10  # 不善行者先行一十里
distance_good_walker = 100  # 善行者追之一百里
distance_ahead_good_walker = 20  # 善行者先至二十里

# Calculation
a = Fraction(distance_not_good_walker * distance_good_walker, distance_not_good_walker + distance_ahead_good_walker)

# Result
a  # This represents the distance (in "里") that the good walker catches up.


"""


The variable `a` will contain the result in terms of "里".
"""


"""
"""
