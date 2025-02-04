"""
又有箕田，舌廣一百一十七步，踵廣五十步，正從一百三十五步。問：為田幾何？
術曰：并踵、舌而半之，以乘正從。畝法而一。
荅曰： a畝 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem describes a trapezoidal field (箕田) with the following dimensions:

- The width of the shorter base (舌廣) is 117 steps.
- The width of the longer base (踵廣) is 50 steps.
- The height (正從) is 135 steps.

The formula provided in the problem is:
1. Add the lengths of the two bases (舌廣 and 踵廣).
2. Divide the sum by 2 to get the average width.
3. Multiply the average width by the height (正從).
4. Convert the result into 畝 (a unit of area).

Here is the Python code to compute the area of the field in 畝:


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions
舌廣 = 117  # steps
踵廣 = 50   # steps
正從 = 135  # steps

# Compute the area
average_width = Fraction(舌廣 + 踵廣, 2)
area_in_steps = average_width * 正從
a = area_in_steps / 240  # Convert to 畝 (1 畝 = 240 square steps)

# The result is stored in variable 'a'
#----- content ends here -----


"""


The variable `a` will contain the area of the field in 畝 as a `Fraction`.
"""


"""
"""
