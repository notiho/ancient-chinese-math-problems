"""
今有甲乙丙三人持錢，甲語乙丙：各將公等所持錢半以益我錢成九十。乙復語甲丙：各將公等所持錢，半以益我，錢成七十。丙復語甲乙：各將公等所持錢，半以益我，錢成五十六。問：三人元持錢各若干？
術曰：先置三人所語為位，以三乘之，各為積，甲得二百七十，乙得二百一十，丙得八十四，又置甲九十，乙七十，丙五十六，各半之，以甲乙減丙，以甲丙減乙，以乙丙減甲，即各得元數。
答曰：甲 a ，乙 b ，丙 c 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. We will compute the values of the unknowns `a`, `b`, and `c` (the amounts of money originally held by the three individuals: 甲, 乙, 丙). Here's the Python code:


"""


from fractions import Fraction

# Given conditions:
# 1. 甲 (a) says: If each of you (乙 and 丙) gives me half of your money, I will have 90.
# 2. 乙 (b) says: If each of you (甲 and 丙) gives me half of your money, I will have 70.
# 3. 丙 (c) says: If each of you (甲 and 乙) gives me half of your money, I will have 56.

# Translate these conditions into equations:
# a + b/2 + c/2 = 90
# b + a/2 + c/2 = 70
# c + a/2 + b/2 = 56

# Solve for a, b, and c:
# Multiply through by 2 to eliminate fractions:
# 2a + b + c = 180
# 2b + a + c = 140
# 2c + a + b = 112

# Subtract equations to isolate variables:
# (2a + b + c) - (2b + a + c) = 180 - 140
# a - b = 40  --> a = b + 40

# (2b + a + c) - (2c + a + b) = 140 - 112
# b - c = 28  --> b = c + 28

# Substitute b = c + 28 and a = b + 40 into the first equation:
# 2a + b + c = 180
# 2(b + 40) + (c + 28) + c = 180
# 2c + 56 + c + 28 + c = 180
# 4c + 84 = 180
# 4c = 96
# c = 24

# Solve for b and a:
c = Fraction(24)
b = c + Fraction(28)  # b = 24 + 28 = 52
a = b + Fraction(40)  # a = 52 + 40 = 92

# Final results:
a, b, c


"""


### Explanation of the Code:
1. We start by translating the problem into equations based on the conditions provided.
2. We eliminate fractions by multiplying through by 2.
3. We subtract equations to isolate variables and solve step by step.
4. Finally, we substitute back to find the values of `a`, `b`, and `c`.

### Solution:
- 甲 (a) originally had 92 units of money.
- 乙 (b) originally had 52 units of money.
- 丙 (c) originally had 24 units of money.
"""


"""
Variable 'a' has wrong value. Expected: 72, Actual: 92
Variable 'b' has wrong value. Expected: 32, Actual: 52
Variable 'c' has wrong value. Expected: 4, Actual: 24"""
