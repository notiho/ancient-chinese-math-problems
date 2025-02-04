"""
又有積五十六萬四千七百五十二步、四分步之一。問︰為方幾何？
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a total area of 564,752 and 1/4 bu².
Question: what is the side length of the square field?

Answer: the side length is *a* bu.
"""

# Total area in bu²
total_area = Fraction(564752 * 4 + 1, 4)

# To find the side length of a square, take the square root of the area
# The side length `a` satisfies: a² = total_area
# Therefore, a = sqrt(total_area)

# Since we cannot use external libraries, we solve this manually by finding the integer part and fractional part.

# Step 1: Find the integer part of the square root
integer_part = 752  # Approximation since 752² = 564,504, which is close to 564,752

# Step 2: Check if there is a fractional part
remainder = total_area - integer_part**2

# Step 3: Express the fractional part as a fraction
fractional_part = Fraction(remainder, 2 * integer_part)

# Final side length
a = integer_part + fractional_part

a  # The side length of the square field in bu#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1503/2, Actual: 4521025/6016"""
