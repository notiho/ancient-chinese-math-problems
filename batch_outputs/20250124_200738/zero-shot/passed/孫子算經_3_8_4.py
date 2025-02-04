"""
今有綿，九萬一千一百三十五觔，給與三萬六千四百五十四戶。問：戶得幾何？
術曰：置九萬一千一百三十五觔，為實；以三萬六千四百五十四戶，為法。除之，得二觔，不盡一萬八千二百二十七觔，以一十六乘之，得二十九萬一千六百三十二兩，以戶除之，即得。
答曰： a觔 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
total_weight = 91135  # in 觔
total_households = 36454  # number of households

# Calculate the weight per household
a = Fraction(total_weight, total_households)

# Result
a  # in 觔
#----- content ends here -----


"""


The variable `a` will hold the weight per household in 觔 as a fraction.
"""


"""
"""
