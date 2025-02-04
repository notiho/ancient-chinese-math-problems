"""
今有甲乙丙三人持錢，甲語乙丙：各將公等所持錢半以益我錢成九十。乙復語甲丙：各將公等所持錢，半以益我，錢成七十。丙復語甲乙：各將公等所持錢，半以益我，錢成五十六。問：三人元持錢各若干？
術曰：先置三人所語為位，以三乘之，各為積，甲得二百七十，乙得二百一十，丙得八十四，又置甲九十，乙七十，丙五十六，各半之，以甲乙減丙，以甲丙減乙，以乙丙減甲，即各得元數。
答曰：甲 a ，乙 b ，丙 c 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves three people, each holding an unknown amount of money. We will calculate the values of these unknowns (`a`, `b`, `c`) using the given conditions.

Here is the Python code:


"""


from fractions import Fraction

# Given conditions:
# 1. When a + (b/2) + (c/2) = 90
# 2. When b + (a/2) + (c/2) = 70
# 3. When c + (a/2) + (b/2) = 56

# Solve the equations step by step:
# Multiply each equation by 2 to eliminate fractions:
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
# 2c + 80 + c + 28 + c = 180
# 4c + 108 = 180
# 4c = 72
# c = 18

# Back-substitute to find b and a:
c = Fraction(18)
b = c + Fraction(28)  # b = 18 + 28 = 46
a = b + Fraction(40)  # a = 46 + 40 = 86

# Final results:
a = Fraction(86)  # Amount of money held by person A
b = Fraction(46)  # Amount of money held by person B
c = Fraction(18)  # Amount of money held by person C


"""


### Solution:
- `a = 86` (Person A's money)
- `b = 46` (Person B's money)
- `c = 18` (Person C's money)
"""


"""
Variable 'a' has wrong value. Expected: 72, Actual: 86
Variable 'b' has wrong value. Expected: 32, Actual: 46
Variable 'c' has wrong value. Expected: 4, Actual: 18"""
