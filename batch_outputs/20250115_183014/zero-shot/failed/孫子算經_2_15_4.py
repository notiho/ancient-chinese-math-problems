"""
今有索，長五千七百九十四步。欲使作方。問：幾何？
術曰：置長五千七百九十四步，以四除之，得一千四百四十八步，餘二步，以六因之，得一丈二尺，以四除之，得三尺，通計即得。
答曰： a步 b尺 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given length in steps
length_in_steps = 5794

# Divide the length by 4 to get the side length in steps
side_length_in_steps = length_in_steps // 4
remainder_steps = length_in_steps % 4

# Convert the remainder into smaller units (1 step = 6 feet, 1 foot = 10 inches)
remainder_in_feet = remainder_steps * 6
side_length_in_feet = remainder_in_feet // 4
remainder_in_inches = remainder_in_feet % 4

# Convert the remaining inches into feet (1 foot = 10 inches)
side_length_in_inches = remainder_in_inches * 10 // 4

# Final results
a = side_length_in_steps
b = side_length_in_inches

# Output the results
a, b


"""


This code calculates the side length in steps (`a`) and the remaining length in inches (`b`).
"""


"""
Variable 'b' has wrong value. Expected: 3, Actual: 0"""
