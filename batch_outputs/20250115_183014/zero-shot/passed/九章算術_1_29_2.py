"""
又有箕田，舌廣一百一十七步，踵廣五十步，正從一百三十五步。問：為田幾何？
術曰：并踵、舌而半之，以乘正從。畝法而一。
荅曰： a畝 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the area of a trapezoidal field (箕田). The formula provided in the problem is:

1. Add the lengths of the two parallel sides (舌廣 and 踵廣).
2. Divide the sum by 2 to get the average width.
3. Multiply the average width by the height (正從).
4. Convert the result into 畝 (a traditional Chinese unit of area).

Here is the Python code:


"""


from fractions import Fraction

# Given values
舌廣 = 117  # in steps
踵廣 = 50   # in steps
正從 = 135  # in steps

# Calculation
average_width = Fraction(舌廣 + 踵廣, 2)  # Average width
area_in_steps = average_width * 正從  # Area in square steps

# Conversion to 畝 (assuming 1 畝 = 240 square steps)
a = area_in_steps / 240  # Area in 畝

# Result
a  # The area in 畝


"""


The variable `a` will contain the area of the field in 畝.
"""


"""
"""
