"""
又有邪田，正廣六十五步，一畔從一百步，一畔從七十二步。問：為田幾何？
術曰：并兩邪而半之，以乘正從若廣。又可半正從若廣，以乘并。畝法而一。
荅曰： a畝 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem describes a field with slanted sides and asks for the area in "畝" (a traditional Chinese unit of area). Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
正廣 = 65  # 正廣 (width) in steps
一畔從 = 100  # One slanted side in steps
另一畔從 = 72  # The other slanted side in steps

# Calculation
並兩邪 = 一畔從 + 另一畔從  # Sum of the two slanted sides
半並兩邪 = Fraction(並兩邪, 2)  # Half of the sum of the two slanted sides
田面積 = 半並兩邪 * 正廣  # Area of the field in square steps

# Convert to 畝 (1 畝 = 240 square steps)
a = Fraction(田面積, 240)

# Result
a  # Area in 畝
#----- content ends here -----


"""


This code computes the area of the field in "畝" and assigns the result to the variable `a`.
"""


"""
"""
