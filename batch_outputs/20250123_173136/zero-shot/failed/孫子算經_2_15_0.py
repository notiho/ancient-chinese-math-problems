"""
今有索，長五千七百九十四步。欲使作方。問：幾何？
術曰：置長五千七百九十四步，以四除之，得一千四百四十八步，餘二步，以六因之，得一丈二尺，以四除之，得三尺，通計即得。
答曰： a步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given length in steps
length_in_steps = 5794

# Divide the length by 4
a = length_in_steps // 4  # Integer division to get the quotient
remainder = length_in_steps % 4  # Remainder after division

# Multiply the remainder by 6 to convert to smaller units (e.g., zhang and chi)
smaller_units = remainder * 6  # This gives 1丈2尺 (12 chi)

# Divide the smaller units by 4 to convert to chi
chi = smaller_units // 4  # Integer division to get the quotient in chi
remaining_chi = smaller_units % 4  # Remaining chi

# Final answer in steps
a = a + Fraction(remaining_chi, 4)  # Combine the steps and fractional chi

# The answer is stored in variable 'a'


"""


Explanation:
1. The total length is 5794 steps.
2. Divide the length by 4 to get the quotient (`a`) and the remainder.
3. Multiply the remainder by 6 to convert it into smaller units (丈 and 尺).
4. Divide the smaller units by 4 to convert them into chi.
5. Combine the integer steps and fractional chi to get the final answer.

The variable `a` contains the final result in steps.
"""


"""
Variable 'a' has wrong value. Expected: 2897/2, Actual: 1448"""
