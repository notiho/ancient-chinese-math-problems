"""
今有不善行者先行一十里，善行者追之一百里，先至不善行者二十里。問︰善行者幾何里及之？
術曰：置不善行者先行一十里，以善行者先至二十里增之，以為法。以不善行者先行一十里，乘善行者一百里，為實。實如法得一里。
荅曰： a里 。
"""

"""
Here is the Python code to compute the value of `a`:


"""


from fractions import Fraction

# Variables
distance_not_good = 10  # 不善行者先行的距離 (里)
distance_good = 100  # 善行者追的距離 (里)
distance_ahead = 20  # 善行者先至的距離 (里)

# Calculation
a = Fraction(distance_not_good * distance_good, distance_not_good + distance_ahead)

# Output the result
a  # 善行者幾何里及之


"""


The value of `a` will be computed as a fraction representing the distance in "里".
"""


"""
"""
