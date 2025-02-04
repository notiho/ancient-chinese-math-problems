"""
今有索，長五千七百九十四步。欲使作方。問：幾何？
術曰：置長五千七百九十四步，以四除之，得一千四百四十八步，餘二步，以六因之，得一丈二尺，以四除之，得三尺，通計即得。
答曰： a步 。
"""

"""
To solve the problem, we will translate the ancient Chinese math problem into Python code. The problem involves converting a length of 5794 steps into a square (a side length in steps). The solution involves dividing the length by 4, handling the remainder, and converting it into smaller units (e.g., zhang and chi). Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given length in steps
length = 5794

# Step 1: Divide the length by 4
a = length // 4  # Quotient in steps
remainder = length % 4  # Remainder in steps

# Step 2: Convert the remainder into zhang and chi
# 1 step = 6 chi
zhang = remainder * 6  # Convert remainder steps to chi
chi = zhang // 4  # Convert chi to zhang
remaining_chi = zhang % 4  # Remaining chi

# Final result
a = Fraction(a) + Fraction(chi, 10) + Fraction(remaining_chi, 100)

# The side length of the square is stored in variable 'a'
#----- content ends here -----


"""


The variable `a` now contains the side length of the square in steps, represented as a `Fraction`.
"""


"""
Variable 'a' has wrong value. Expected: 2897/2, Actual: 14483/10"""
