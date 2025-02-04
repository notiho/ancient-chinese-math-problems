"""
假令有句股相乘冪七百六十五分之一，弦多於句三十六十分之九。問：三事各多少？
術曰：冪自乘，倍多數而一，為實。半多數，為廉法，從。開立方除之，即句。以弦多句加之，即弦。以句除冪，即股。
答曰：句 a ，股 b ，弦 c 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves finding the values of three unknowns: `a` (句), `b` (股), and `c` (弦). Here's the Python code:


"""


from fractions import Fraction

# Given data
mian = Fraction(1, 765)  # 冪 (mian) is 1/765
duo = Fraction(9, 36)    # 弦多於句 (duo) is 9/36

# Step 1: 冪自乘，倍多數而一，為實
shi = mian * mian * (2 * duo + 1)

# Step 2: 半多數，為廉法，從
lian = duo / 2

# Step 3: 開立方除之，即句
a = shi ** (1/3) / (1 + lian)

# Step 4: 以弦多句加之，即弦
c = a * (1 + duo)

# Step 5: 以句除冪，即股
b = mian / a

# Results
a, b, c


"""


This code calculates the values of `a` (句), `b` (股), and `c` (弦) based on the ancient Chinese mathematical procedure described in the problem. The results are stored in the variables `a`, `b`, and `c`.
"""


"""
Variable 'a' has wrong value. Expected: 287/20, Actual: 0.012164761737531832
Variable 'b' has wrong value. Expected: 246/5, Actual: 0.10745706086873857
Variable 'c' has wrong value. Expected: 205/4, Actual: 0.01520595217191479"""
