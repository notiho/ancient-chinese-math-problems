"""
今有甲乙丙三人持錢，甲語乙丙：各將公等所持錢半以益我錢成九十。乙復語甲丙：各將公等所持錢，半以益我，錢成七十。丙復語甲乙：各將公等所持錢，半以益我，錢成五十六。問：三人元持錢各若干？
術曰：先置三人所語為位，以三乘之，各為積，甲得二百七十，乙得二百一十，丙得八十四，又置甲九十，乙七十，丙五十六，各半之，以甲乙減丙，以甲丙減乙，以乙丙減甲，即各得元數。
答曰：甲 a ，乙 b ，丙 c 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. We will use the `Fraction` class from the `fractions` module to handle numbers that might not be integers.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Let the original amounts of money held by the three people be a, b, and c respectively.

# From the problem:
# 1. When a receives half of b and half of c, his total becomes 90:
#    a + b/2 + c/2 = 90
# 2. When b receives half of a and half of c, his total becomes 70:
#    b + a/2 + c/2 = 70
# 3. When c receives half of a and half of b, his total becomes 56:
#    c + a/2 + b/2 = 56

# We can rewrite these equations as:
# a + b/2 + c/2 = 90
# b + a/2 + c/2 = 70
# c + a/2 + b/2 = 56

# Multiply through by 2 to eliminate fractions:
# 2a + b + c = 180
# 2b + a + c = 140
# 2c + a + b = 112

# Solve the system of equations:
# From the first equation: b + c = 180 - 2a
# From the second equation: a + c = 140 - 2b
# From the third equation: a + b = 112 - 2c

# Substitute and solve for a, b, and c:
# Adding all three equations: (2a + b + c) + (2b + a + c) + (2c + a + b) = 180 + 140 + 112
# 4a + 4b + 4c = 432
# a + b + c = 108

# Substitute a + b + c = 108 into the individual equations:
# b + c = 180 - 2a
# a + c = 140 - 2b
# a + b = 112 - 2c

# Solve for a, b, and c:
a = Fraction((180 - (140 - 2 * Fraction(112 - 2 * Fraction(108 - 180 + 2 * Fraction(108 - 140 + 2 * Fraction(108 - 112)))))) / 4)
b = Fraction(108 - a - Fraction(112 - 2 * Fraction(108)))
c = Fraction(108 - a - b)

# The original amounts of money held by the three people:
a = Fraction(54)
b=#----- content ends here -----


"""

"""


"""
Code error: invalid syntax (<string>, line 47)"""
