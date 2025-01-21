"""
又有田廣十二步，從十四步。問：為田幾何？
方田術曰：廣從步數相乘得積步。以畝法二百四十步除之，即畝數。百畝為一頃。
荅曰： a步 。
"""

"""
To solve this problem, we calculate the area of the field in "步" (square steps) and then convert it into "畝" using the given conversion factor (240 square steps = 1 畝). Here's the Python code:


"""


from fractions import Fraction

# Given dimensions of the field
廣 = 12  # breadth in steps
從 = 14  # length in steps

# Calculate the area in square steps
積步 = 廣 * 從

# Convert square steps to 畝
畝 = Fraction(積步, 240)

# Assign the answer to variable 'a'
a = 畝

# Output the result
a


"""


The variable `a` will contain the solution in 畝.
"""


"""
Variable 'a' has wrong value. Expected: 168, Actual: 7/10"""
