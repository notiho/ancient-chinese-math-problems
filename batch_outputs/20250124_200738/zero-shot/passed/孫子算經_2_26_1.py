"""
今有人盜庫絹，不知所失幾何？但聞草中分絹，人得六匹，盈六匹；人得七匹，不足七匹。問人、絹各幾何？
術曰：先置人得六匹于右上，盈六匹于右下，後置人得七匹于左上，不足七匹于左下，維乘之所得，并之為絹，并盈不足為人。
答曰：賊 a人 ，絹 b匹 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical method into Python code. Here's how we compute the values of the unknowns `a` (number of people) and `b` (number of silk pieces):


"""

#----- content starts here -----

from fractions import Fraction

# Given conditions:
# Each person gets 6 pieces of silk, with 6 pieces left over.
# Each person gets 7 pieces of silk, but 7 pieces are short.

# Let a = number of people, b = total pieces of silk
# According to the problem:
# b = 6a + 6  (1)
# b = 7a - 7  (2)

# Solve for a and b:
# From (1) and (2), set the equations equal to each other:
# 6a + 6 = 7a - 7
# Simplify:
# 6 + 7 = 7a - 6a
# a = 13

# Substitute a = 13 into (1) to find b:
# b = 6a + 6
# b = 6 * 13 + 6
# b = 78 + 6
# b = 84

# Final answers:
a = 13  # Number of people
b = 84  # Total pieces of silk
#----- content ends here -----


"""


The solution is:
- `a = 13` (number of people)
- `b = 84` (total pieces of silk)
"""


"""
"""
