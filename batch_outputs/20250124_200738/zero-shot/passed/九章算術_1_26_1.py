"""
今有邪田，一頭廣三十步，一頭廣四十二步，正從六十四步。問：為田幾何？
術曰：并兩邪而半之，以乘正從若廣。又可半正從若廣，以乘并。畝法而一。
荅曰： a畝 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
width1 = 30  # in steps
width2 = 42  # in steps
length = 64  # in steps

# Calculation
average_width = Fraction(width1 + width2, 2)  # Average of the two widths
area_in_steps = average_width * length  # Area in square steps
a = area_in_steps / 240  # Convert square steps to "畝" (1 畝 = 240 square steps)

# Result
a  # The area in 畝
#----- content ends here -----


"""


The variable `a` will contain the answer in 畝.
"""


"""
"""
