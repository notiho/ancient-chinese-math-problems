"""
今有甲乙丙三人持錢，甲語乙丙：各將公等所持錢半以益我錢成九十。乙復語甲丙：各將公等所持錢，半以益我，錢成七十。丙復語甲乙：各將公等所持錢，半以益我，錢成五十六。問：三人元持錢各若干？
術曰：先置三人所語為位，以三乘之，各為積，甲得二百七十，乙得二百一十，丙得八十四，又置甲九十，乙七十，丙五十六，各半之，以甲乙減丙，以甲丙減乙，以乙丙減甲，即各得元數。
答曰：甲 a ，乙 b ，丙 c 。
"""

"""
To solve the problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given conditions:
# 1. When half of the money of乙 and丙 is added to甲's money, it becomes 90.
# 2. When half of the money of甲 and丙 is added to乙's money, it becomes 70.
# 3. When half of the money of甲 and乙 is added to丙's money, it becomes 56.

# Let the original amounts of money held by甲,乙,丙 be a, b, c respectively.

# Equations derived from the problem:
# a + (b / 2) + (c / 2) = 90
# b + (a / 2) + (c / 2) = 70
# c + (a / 2) + (b / 2) = 56

# Solve for a, b, c:
# Multiply through by 2 to eliminate fractions:
# 2a + b + c = 180
# 2b + a + c = 140
# 2c + a + b = 112

# Subtract equations to isolate variables:
# (2a + b + c) - (2b + a + c) = 180 - 140
# a - b = 40  -> (1)

# (2b + a + c) - (2c + a + b) = 140 - 112
# b - c = 28  -> (2)

# (2c + a + b) - (2a + b + c) = 112 - 180
# c - a = -68 -> (3)

# Solve the system of equations:
# From (1): a = b + 40
# From (2): b = c + 28
# From (3): c = a - 68

# Substitute b and c in terms of a:
# b = c + 28 = (a - 68) + 28 = a - 40
# c = a - 68

# Substitute b and c into the first equation:
# 2a + b + c = 180
# 2a + (a - 40) + (a - 68) = 180
# 4a - 108 = 180
# 4a = 288
# a = 72

# Calculate b and c:
a = Fraction(72)
b = a - 40  # b = 72 - 40 = 32
c = a - 68  # c = 72 - 68 = 4

# Final values:
# a = 72, b = 32, c = 4


"""


The solution is:
- 甲 (a) = 72
- 乙 (b) = 32
- 丙 (c) = 4
"""


"""
"""
