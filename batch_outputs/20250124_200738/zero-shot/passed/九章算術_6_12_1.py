"""
今有不善行者先行一十里，善行者追之一百里，先至不善行者二十里。問︰善行者幾何里及之？
術曰：置不善行者先行一十里，以善行者先至二十里增之，以為法。以不善行者先行一十里，乘善行者一百里，為實。實如法得一里。
荅曰： a里 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
distance_not_good = 10  # 不善行者先行的距离 (10 里)
distance_good = 100  # 善行者追的距离 (100 里)
lead_good = 20  # 善行者先至的距离 (20 里)

# Calculation
a = Fraction(distance_not_good * distance_good, distance_not_good + lead_good)

# The result is stored in variable 'a'
a
#----- content ends here -----


"""


The variable `a` represents the distance (in 里) that the good walker needs to travel to catch up.
"""


"""
"""
