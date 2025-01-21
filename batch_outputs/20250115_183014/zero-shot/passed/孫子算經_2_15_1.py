"""
今有索，長五千七百九十四步。欲使作方。問：幾何？
術曰：置長五千七百九十四步，以四除之，得一千四百四十八步，餘二步，以六因之，得一丈二尺，以四除之，得三尺，通計即得。
答曰： a步 b尺 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves converting a length of 5794 steps into a square (方). The solution involves dividing the length by 4, handling the remainder, and converting it into smaller units (steps and chi).

Here is the Python code:


"""


from fractions import Fraction

# Given length in steps
length_in_steps = 5794

# Step 1: Divide the length by 4
a = length_in_steps // 4  # Integer division to get the number of steps
remainder_steps = length_in_steps % 4  # Remainder after division

# Step 2: Convert the remainder into smaller units
# 1 step = 6 chi (尺)
remainder_chi = remainder_steps * 6

# Step 3: Divide the remainder in chi by 4 to get the final chi
b = remainder_chi // 4  # Integer division to get the number of chi
final_remainder_chi = remainder_chi % 4  # Remainder in chi

# Final result
a = a  # Steps
b = Fraction(b) + Fraction(final_remainder_chi, 4)  # Chi as a fraction

# Output variables a (steps) and b (chi)
a, b


"""


### Explanation:
1. Divide the total length (5794 steps) by 4 to get the number of steps (`a`) and the remainder.
2. Convert the remainder into chi (1 step = 6 chi).
3. Divide the chi by 4 to get the final chi (`b`), including any fractional part.

### Solution:
The variables `a` and `b` represent the number of steps and chi, respectively.
"""


"""
"""
