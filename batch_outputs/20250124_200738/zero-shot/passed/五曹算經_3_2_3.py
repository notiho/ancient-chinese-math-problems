"""
今有粟五百六十斛。問：為糳米㡬何？
術曰：列粟五百六十斛，以二十四乘之得一萬三千四百四十斛，以五十除之即得。
答曰： a斛 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the amount of 糳米 (processed rice) from a given amount of 粟 (unprocessed grain). Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
粟 = 560  # 粟 in 斛
multiplier = 24  # Multiplier for processing
divisor = 50  # Divisor for final calculation

# Calculation
a = Fraction(粟 * multiplier, divisor)  # 糳米 in 斛

# Result
a  # This variable holds the answer in 斛
#----- content ends here -----


"""


The value of `a` will represent the amount of 糳米 in 斛.
"""


"""
"""
