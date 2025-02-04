"""
今有人盜庫絹，不知所失幾何？但聞草中分絹，人得六匹，盈六匹；人得七匹，不足七匹。問人、絹各幾何？
術曰：先置人得六匹于右上，盈六匹于右下，後置人得七匹于左上，不足七匹于左下，維乘之所得，并之為絹，并盈不足為人。
答曰：賊 a人 ，絹 b匹 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given conditions:
# When each person gets 6匹, there are 6匹 left.
# When each person gets 7匹, there are 7匹 missing.

# Let the number of people be 'a' and the total number of 絹 be 'b'.

# Equation 1: b = 6a + 6 (when each person gets 6匹, 6匹 are left)
# Equation 2: b = 7a - 7 (when each person gets 7匹, 7匹 are missing)

# Solve for 'a' and 'b':
# From Equation 1 and Equation 2:
# 6a + 6 = 7a - 7
# 6 + 7 = 7a - 6a
# a = 13

# Substitute 'a' into Equation 1 to find 'b':
# b = 6a + 6
# b = 6 * 13 + 6
# b = 78 + 6
# b = 84

# Assign the results to variables:
a = 13  # Number of people
b = 84  # Total number of 絹
#----- content ends here -----


"""


### Final Answer:
- 賊 **a = 13** 人
- 絹 **b = 84** 匹
"""


"""
"""
