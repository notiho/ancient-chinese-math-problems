"""
今有甲乙丙三人持錢，甲語乙丙：各將公等所持錢半以益我錢成九十。乙復語甲丙：各將公等所持錢，半以益我，錢成七十。丙復語甲乙：各將公等所持錢，半以益我，錢成五十六。問：三人元持錢各若干？
術曰：先置三人所語為位，以三乘之，各為積，甲得二百七十，乙得二百一十，丙得八十四，又置甲九十，乙七十，丙五十六，各半之，以甲乙減丙，以甲丙減乙，以乙丙減甲，即各得元數。
答曰：甲 a ，乙 b ，丙 c 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given conditions
# Let a, b, c represent the original amounts of money held by 甲, 乙, 丙 respectively.

# Equations derived from the problem:
# 1. a + (b / 2) + (c / 2) = 90
# 2. b + (a / 2) + (c / 2) = 70
# 3. c + (a / 2) + (b / 2) = 56

# Solve for a, b, c
# Multiply through by 2 to eliminate fractions:
# 2a + b + c = 180
# 2b + a + c = 140
# 2c + a + b = 112

# Use elimination to solve the system of equations:
# Subtract the third equation from the first:
# (2a + b + c) - (2c + a + b) = 180 - 112
# a - c = 68  --> (1)

# Subtract the second equation from the first:
# (2a + b + c) - (2b + a + c) = 180 - 140
# a - b = 40  --> (2)

# Subtract the third equation from the second:
# (2b + a + c) - (2c + a + b) = 140 - 112
# b - c = 28  --> (3)

# Solve equations (1), (2), and (3):
# From (2): a = b + 40
# From (3): b = c + 28
# Substitute b = c + 28 into a = b + 40:
# a = (c + 28) + 40
# a = c + 68

# Substitute a = c + 68 and b = c + 28 into the first original equation:
# 2a + b + c = 180
# 2(c + 68) + (c + 28) + c = 180
# 2c + 136 + c + 28 + c = 180
# 4c + 164 = 180
# 4c = 16
# c = 4

# Solve for b and a:
c = Fraction(4)
b = c + 28
a = c + 68

# Results
a, b, c
#----- content ends here -----


"""


The values of `a`, `b`, and `c` represent the original amounts of money held by 甲, 乙, and 丙 respectively.
"""


"""
"""
