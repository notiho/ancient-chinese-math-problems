"""
今有獸，六首四足；禽，二首二足，上有七十六首，下有四十六足。問：禽、獸各幾何？
術曰：倍足以減首，餘半之，即獸；以四乘獸，減足，餘半之，即禽。
答曰： a 獸 b 禽。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves finding the number of beasts (`a`) and birds (`b`) given the total number of heads and legs. Here's the solution:


"""


from fractions import Fraction

# Given data
total_heads = 76  # Total number of heads
total_legs = 46   # Total number of legs

# Step 1: Calculate the number of beasts (a)
a = Fraction(2 * total_legs - total_heads, 2)

# Step 2: Calculate the number of birds (b)
b = Fraction(total_heads - 4 * a, 2)

# Results
a, b


"""


This code calculates the number of beasts (`a`) and birds (`b`) using the method described in the problem. The results are stored in the variables `a` and `b`.
"""


"""
Variable 'b' has wrong value. Expected: 7, Actual: 22"""
