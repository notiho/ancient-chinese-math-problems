"""
又有邪田，正廣六十五步，一畔從一百步，一畔從七十二步。問：為田幾何？
術曰：并兩邪而半之，以乘正從若廣。又可半正從若廣，以乘并。畝法而一。
荅曰： a畝 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the area of a field with irregular sides. Here's the solution:


"""


from fractions import Fraction

# Given values
正廣 = 65  # 正廣 (width) in steps
一畔從 = 100  # One side length in steps
一畔從_2 = 72  # The other side length in steps

# Calculation
# 并兩邪而半之: Add the two irregular sides and divide by 2 (average of the two sides)
average_side = Fraction(一畔從 + 一畔從_2, 2)

# 以乘正從若廣: Multiply the average side by the 正廣 (width)
area_in_steps = average_side * 正廣

# 畝法而一: Convert the area in steps to 畝 (1 畝 = 240 steps²)
a = area_in_steps / 240

# Result
a  # The area in 畝


"""


This code calculates the area of the irregular field in 畝 (`a`). The result is stored in the variable `a`.
"""


"""
"""
