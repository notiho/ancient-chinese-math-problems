"""
今有圓困，高一丈三尺三寸、少半寸，容米二千斛。問︰周幾何？
術曰：置米積尺，以十二乘之，令高而一，所得，開方除之，即周。
荅曰： a丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the circumference (周) of a cylindrical container given its height and volume. Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
height = Fraction(1, 1) * 10 + Fraction(3, 10) + Fraction(3, 100) - Fraction(1, 200)  # Height in 丈 (1丈 = 10尺)
volume = Fraction(2000, 1)  # 米二千斛 (volume in 斛)

# Step 1: Convert the volume into cubic 尺 (1斛 = 10 cubic 尺)
volume_cubic_chi = volume * 10

# Step 2: Multiply the volume by 12
volume_times_12 = volume_cubic_chi * 12

# Step 3: Divide the result by the height
base_area = volume_times_12 / height

# Step 4: Take the square root of the base area to find the diameter
diameter = base_area ** Fraction(1, 2)

# Step 5: Calculate the circumference (周) using the formula 周 = π * diameter
# Using an approximation for π = 3 (as was common in ancient Chinese mathematics)
circumference = diameter * 3

# Assign the result to the variable "a"
a = circumference

# Output the result
a
#----- content ends here -----


"""


The variable `a` will contain the circumference in 丈.
"""


"""
Variable 'a' has wrong value. Expected: 27/5, Actual: 457.384923803794"""
