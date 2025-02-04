"""
假令有句股相乘冪七百六十五分之一，弦多於句三十六十分之九。問：三事各多少？
術曰：冪自乘，倍多數而一，為實。半多數，為廉法，從。開立方除之，即句。以弦多句加之，即弦。以句除冪，即股。
答曰：句 a ，股 b ，弦 c 。
"""

"""
To solve this problem, let's translate the ancient Chinese math problem into Python code. We'll use the `Fraction` class to handle numbers that might not be integers.

The problem involves a right triangle where:
- The product of the legs (句 and 股) is given as \( \frac{1}{765} \) (冪).
- The hypotenuse (弦) exceeds one leg (句) by \( \frac{9}{36} = \frac{1}{4} \).

The solution involves:
1. Calculating the leg (句, denoted as `a`).
2. Calculating the other leg (股, denoted as `b`).
3. Calculating the hypotenuse (弦, denoted as `c`).

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
mian = Fraction(1, 765)  # 冪 (product of the legs)
extra = Fraction(9, 36)  # Difference between 弦 and 句

# Step 1: Calculate 句 (a)
# 冪自乘，倍多數而一，為實。
shi = mian * mian * 2 + 1

# 半多數，為廉法，從。
lianfa = extra / 2

# 開立方除之，即句。
a = (shi / lianfa) ** (1/3)

# Step 2: Calculate 弦 (c)
# 以弦多句加之，即弦。
c = a + extra

# Step 3: Calculate 股 (b)
# 以句除冪，即股。
b = mian / a

# Results
a, b, c
#----- content ends here -----


"""


This code computes the values of `a`, `b`, and `c` based on the ancient Chinese math problem. Note that the `Fraction` class ensures precise calculations for fractional values.
"""


"""
Variable 'a' has wrong value. Expected: 287/20, Actual: 2.0000022783234046
Variable 'b' has wrong value. Expected: 246/5, Actual: 0.0006535940266925459
Variable 'c' has wrong value. Expected: 205/4, Actual: 2.2500022783234046"""
