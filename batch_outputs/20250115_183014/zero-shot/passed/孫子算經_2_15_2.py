"""
今有索，長五千七百九十四步。欲使作方。問：幾何？
術曰：置長五千七百九十四步，以四除之，得一千四百四十八步，餘二步，以六因之，得一丈二尺，以四除之，得三尺，通計即得。
答曰： a步 b尺 。
"""

"""
To solve the problem, we need to calculate the side length of a square (方) given the total length of the rope (索) is 5794 steps (步). The problem describes dividing the total length by 4 to find the side length in steps, then converting the remainder into smaller units (丈 and 尺). Here's the Python code:


"""


from fractions import Fraction

# Total length of the rope in steps
total_length = 5794

# Step 1: Divide the total length by 4 to find the side length in steps
a = total_length // 4  # Integer division to get the whole number of steps
remainder_steps = total_length % 4  # Remainder in steps

# Step 2: Convert the remainder into smaller units
# 1 step = 6 尺 (chi), so multiply the remainder by 6
remainder_chi = remainder_steps * 6

# Step 3: Divide the remainder in 尺 by 4 to find the additional 尺
b = remainder_chi // 4  # Integer division to get the whole number of 尺
remainder_fraction = Fraction(remainder_chi % 4, 4)  # Fractional part in 尺

# Final answer
a = Fraction(a)  # Side length in steps
b = Fraction(b) + remainder_fraction  # Side length in 尺


"""


The solution is stored in variables `a` (in steps) and `b` (in 尺).
"""


"""
"""
