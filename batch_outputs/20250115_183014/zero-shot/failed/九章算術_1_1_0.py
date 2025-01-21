"""
又有田廣十二步，從十四步。問：為田幾何？
方田術曰：廣從步數相乘得積步。以畝法二百四十步除之，即畝數。百畝為一頃。
荅曰： a步 。
"""

"""
To solve this problem, we need to calculate the area of a rectangular field given its width (廣) and length (從). The area is then converted into 畝 (a traditional Chinese unit of area) by dividing the total area in square steps (步²) by 240. Let's compute this in Python:


"""


from fractions import Fraction

# Given dimensions of the field
width = 12  # 廣 (steps)
length = 14  # 從 (steps)

# Calculate the area in square steps
area_in_steps = width * length  # 廣從步數相乘得積步

# Convert the area into 畝
a = Fraction(area_in_steps, 240)  # 以畝法二百四十步除之，即畝數

# The result is stored in variable 'a'


"""


The variable `a` now contains the area of the field in 畝 as a fraction.
"""


"""
Variable 'a' has wrong value. Expected: 168, Actual: 7/10"""
