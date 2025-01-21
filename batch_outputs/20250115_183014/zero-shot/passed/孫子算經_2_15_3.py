"""
今有索，長五千七百九十四步。欲使作方。問：幾何？
術曰：置長五千七百九十四步，以四除之，得一千四百四十八步，餘二步，以六因之，得一丈二尺，以四除之，得三尺，通計即得。
答曰： a步 b尺 。
"""

"""
To solve this problem, let's translate the ancient Chinese math problem into Python code. The problem involves dividing a length of 5794 steps into a square and calculating the side length in steps and additional smaller units (like "尺"). Here's the Python code:


"""


from fractions import Fraction

# Given length in steps
length = 5794

# Divide the length by 4 to get the side length in steps
a = length // 4  # Integer division to get the whole steps
remainder_steps = length % 4  # Remainder in steps

# Convert the remainder steps into smaller units (丈 and 尺)
# 1 step = 6 尺
remainder_chi = remainder_steps * 6  # Convert remaining steps to 尺

# Divide 尺 by 4 to get the remaining 尺
b = remainder_chi // 4  # Integer division to get the whole 尺
remainder_chi_final = remainder_chi % 4  # Remaining 尺 (if any)

# Final answer
a = a  # Side length in steps
b = b + Fraction(remainder_chi_final, 4)  # Remaining 尺 as a fraction


"""


### Explanation:
1. Divide the total length (5794 steps) by 4 to get the side length in steps (`a`).
2. The remainder from the division is converted into smaller units (尺) using the conversion factor (1 step = 6 尺).
3. Divide the smaller units (尺) by 4 to get the remaining 尺 (`b`), including any fractional part.

### Final Answer:
The side length is `a` steps and `b` 尺.
"""


"""
"""
