"""
今有獸，六首四足；禽，二首二足，上有七十六首，下有四十六足。問：禽、獸各幾何？
術曰：倍足以減首，餘半之，即獸；以四乘獸，減足，餘半之，即禽。
答曰： a 獸 b 禽。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves finding the number of beasts (獸) and birds (禽) based on the given number of heads and feet. Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
total_heads = 76  # Total number of heads
total_feet = 46   # Total number of feet

# Step 1: Calculate the number of beasts (獸)
# Formula: (2 * total_feet - total_heads) / 2
a = Fraction(2 * total_feet - total_heads, 2)

# Step 2: Calculate the number of birds (禽)
# Formula: (total_heads - 4 * beasts) / 2
b = Fraction(total_heads - 4 * a, 2)

# Results
a, b
#----- content ends here -----


"""


This code computes the values of `a` (number of beasts) and `b` (number of birds) using the formulas provided in the problem. The results are stored in variables `a` and `b`.
"""


"""
Variable 'b' has wrong value. Expected: 7, Actual: 22"""
