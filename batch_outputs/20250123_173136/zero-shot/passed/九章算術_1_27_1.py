"""
又有邪田，正廣六十五步，一畔從一百步，一畔從七十二步。問：為田幾何？
術曰：并兩邪而半之，以乘正從若廣。又可半正從若廣，以乘并。畝法而一。
荅曰： a畝 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the area of a slanted field (邪田) where the width (正廣) is 65 steps, one side length (正從) is 100 steps, and the other side length (正從) is 72 steps. The formula provided in the problem can be interpreted as follows:

1. Add the two slanted sides (100 and 72), divide by 2, and multiply by the width (65).
2. Divide the result by the conversion factor for steps to 畝 (畝法).

We will compute the area in 畝 using the given formula.

Here is the Python code:


"""


from fractions import Fraction

# Given values
width = 65  # 正廣 in steps
side1 = 100  # 一畔從 in steps
side2 = 72  # 一畔從 in steps

# Step 1: Compute the average of the two slanted sides
average_side = Fraction(side1 + side2, 2)

# Step 2: Multiply the average side by the width
area_in_steps = average_side * width

# Step 3: Convert steps to 畝 (assuming 1 畝 = 240 steps² as a conversion factor)
conversion_factor = 240
a = area_in_steps / conversion_factor

# The result is stored in variable 'a'


"""


The variable `a` contains the area of the field in 畝 as a `Fraction`.
"""


"""
"""
