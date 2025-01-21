"""
今有獸，六首四足；禽，二首二足，上有七十六首，下有四十六足。問：禽、獸各幾何？
術曰：倍足以減首，餘半之，即獸；以四乘獸，減足，餘半之，即禽。
答曰： a 獸 b 禽。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given data
total_heads = 76  # Total number of heads
total_feet = 46   # Total number of feet

# Step 1: Double the total feet and subtract the total heads, then divide by 2 to get the number of beasts (獸).
a = (2 * total_feet - total_heads) / 2

# Step 2: Multiply the number of beasts by 4, subtract the total feet, then divide by 2 to get the number of birds (禽).
b = (4 * a - total_feet) / 2

# Convert to Fraction if needed
a = Fraction(a)
b = Fraction(b)

# The result
a, b


"""


The variables `a` and `b` represent the number of beasts (獸) and birds (禽), respectively.
"""


"""
Variable 'b' has wrong value. Expected: 7, Actual: -7"""
