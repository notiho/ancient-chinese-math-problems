"""
假令有句股相乘冪七百六十五分之一，弦多於句三十六十分之九。問：三事各多少？
術曰：冪自乘，倍多數而一，為實。半多數，為廉法，從。開立方除之，即句。以弦多句加之，即弦。以句除冪，即股。
答曰：句 a ，股 b ，弦 c 。
"""

"""
To solve this ancient Chinese math problem, we will translate the given instructions into Python code. Here's the solution:


"""


from fractions import Fraction

# Given values
mian = Fraction(1, 765)  # 冪 (mian) is 1/765
duo = Fraction(9, 36)    # 弦多於句 (duo) is 9/36

# Step 1: 冪自乘，倍多數而一，為實
shi = mian * mian * (2 * duo + 1)

# Step 2: 半多數，為廉法，從
lian = duo / 2

# Step 3: 開立方除之，即句
a = (shi / lian) ** Fraction(1, 3)  # 句 (a)

# Step 4: 以弦多句加之，即弦
c = a + duo  # 弦 (c)

# Step 5: 以句除冪，即股
b = mian / a  # 股 (b)

# Results
a, b, c


"""


### Explanation:
1. **冪自乘，倍多數而一，為實**: Compute `shi` by squaring `mian` (冪), multiplying by `(2 * duo + 1)`.
2. **半多數，為廉法，從**: Compute `lian` as half of `duo`.
3. **開立方除之，即句**: Compute `a` (句) as the cube root of `shi / lian`.
4. **以弦多句加之，即弦**: Compute `c` (弦) as `a + duo`.
5. **以句除冪，即股**: Compute `b` (股) as `mian / a`.

The variables `a`, `b`, and `c` hold the final results for 句, 股, and 弦 respectively.
"""


"""
Variable 'a' has wrong value. Expected: 287/20, Actual: 0.027370713909446624
Variable 'b' has wrong value. Expected: 246/5, Actual: 0.04775869371943936
Variable 'c' has wrong value. Expected: 205/4, Actual: 0.2773707139094466"""
