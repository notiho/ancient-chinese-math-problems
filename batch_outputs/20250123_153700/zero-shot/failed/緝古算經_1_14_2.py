"""
假令有句股相乘冪七百六十五分之一，弦多於句三十六十分之九。問：三事各多少？
術曰：冪自乘，倍多數而一，為實。半多數，為廉法，從。開立方除之，即句。以弦多句加之，即弦。以句除冪，即股。
答曰：句 a ，股 b ，弦 c 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves a right triangle where the square of the hypotenuse (弦, "c") minus the square of one leg (句, "a") equals the square of the other leg (股, "b"). Additionally, the hypotenuse is given to be greater than one leg by a specific fraction.

Here is the Python code to compute the values of the unknowns:


"""


from fractions import Fraction

# Given values
mian = Fraction(1, 765)  # 冪 (square of the hypotenuse minus the square of one leg)
extra = Fraction(9, 36)  # 弦多於句 (hypotenuse is greater than one leg by this fraction)

# Step 1: 冪自乘，倍多數而一，為實
shi = mian * mian * (2 * extra + 1)

# Step 2: 半多數，為廉法，從
lian = extra / 2

# Step 3: 開立方除之，即句
a = (shi / lian) ** Fraction(1, 3)  # 句 (one leg)

# Step 4: 以弦多句加之，即弦
c = a + a * extra  # 弦 (hypotenuse)

# Step 5: 以句除冪，即股
b = mian / a  # 股 (the other leg)

# The results
a, b, c


"""


This code calculates the values of `a` (句), `b` (股), and `c` (弦) based on the given problem. The results are stored in the variables `a`, `b`, and `c`, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 287/20, Actual: 0.027370713909446624
Variable 'b' has wrong value. Expected: 246/5, Actual: 0.04775869371943936
Variable 'c' has wrong value. Expected: 205/4, Actual: 0.03421339238680828"""
