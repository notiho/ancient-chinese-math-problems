"""
今有圓困，高一丈三尺三寸、少半寸，容米二千斛。問︰周幾何？
術曰：置米積尺，以十二乘之，令高而一，所得，開方除之，即周。
荅曰： a丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction
import math

# Given values
height = Fraction(1, 1) + Fraction(3, 10) + Fraction(3, 100) - Fraction(1, 200)  # height in 丈
volume = 2000  # volume in 斛

# Step 1: Convert volume from 斛 to cubic 丈 (1 斛 = 1/12 cubic 丈)
volume_cubic_zhang = Fraction(volume, 12)

# Step 2: Divide the volume by the height to get the base area
base_area = volume_cubic_zhang / height

# Step 3: Compute the circumference (周)
circumference = 2 * math.sqrt(base_area)  # circumference in 丈

# Assign the result to variable 'a'
a = Fraction.from_float(circumference).limit_denominator()

# Output the result
a


"""


The variable `a` will contain the circumference in 丈 as a fraction.
"""


"""
Variable 'a' has wrong value. Expected: 27/5, Actual: 20194953/900319"""
