"""
今有人盜庫絹，不知所失幾何？但聞草中分絹，人得六匹，盈六匹；人得七匹，不足七匹。問人、絹各幾何？
術曰：先置人得六匹于右上，盈六匹于右下，後置人得七匹于左上，不足七匹于左下，維乘之所得，并之為絹，并盈不足為人。
答曰：賊 a人 ，絹 b匹 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given conditions:
# When each person gets 6匹, there are 6匹 left (盈六匹).
# When each person gets 7匹, there are 7匹 missing (不足七匹).

# Let the number of people be 'a' and the total number of 絹 be 'b'.
# According to the problem:
# b = 6a + 6  (1)
# b = 7a - 7  (2)

# Solve for 'a' and 'b':
# From (1) and (2):
# 6a + 6 = 7a - 7
# 6 + 7 = 7a - 6a
# a = 13

# Substitute 'a' into (1) to find 'b':
# b = 6a + 6
# b = 6 * 13 + 6
# b = 78 + 6
# b = 84

# Final answers:
a = 13  # Number of people
b = 84  # Total number of 絹


"""


The solution is:
- 賊 a人 = 13人
- 絹 b匹 = 84匹
"""


"""
"""
