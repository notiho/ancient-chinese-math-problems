"""
今有田廣一里，從一里。問：為田幾何？
里田術曰：廣從里數相乘得積里。以三百七十五乘之，即畝數。
荅曰： a頃 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
width = Fraction(1)  # 1 里
length = Fraction(1)  # 1 里

# Calculate the area in square 里
area_in_li = width * length  # 廣從里數相乘得積里

# Convert square 里 to 畝 (1 square 里 = 375 畝)
a = area_in_li * 375  # 以三百七十五乘之，即畝數

# The result is stored in variable 'a'
a
#----- content ends here -----


"""


The variable `a` will contain the number of 畝 (mu) for the given area.
"""


"""
Variable 'a' has wrong value. Expected: 15/4, Actual: 375"""
