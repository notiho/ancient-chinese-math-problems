"""
今有五家共井，甲二綆不足，如乙一綆；乙三綆不足，如丙一綆；丙四綆不足，如丁一綆；丁五綆不足，如戊一綆；戊六綆不足，如甲一綆。如各得所不足一綆，皆逮。問︰井深、綆長各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：井深 a(=721/100)丈 。甲綆長 b(=53/20)丈 ，乙綆長 c(=191/100)丈 ，丙綆長 d(=37/25)丈 ，丁綆長 e(=129/100)丈 ，戊綆長 f(=38/5)尺 。
"""

"""
This problem involves solving a system of equations using ancient Chinese methods, specifically the "正負術" (positive-negative method) and "方程術" (method of solving equations). Below is the Python implementation of the solution.


"""


from fractions import Fraction

# Problem setup:
# Let the depth of the well be `井深` (a), and the lengths of the ropes for each family be:
# 甲綆長 (b), 乙綆長 (c), 丙綆長 (d), 丁綆長 (e), 戊綆長 (f).

# The relationships are:
# b = c - 2
# c = d - 3
# d = e - 4
# e = f - 5
# f = b - 6
# Additionally, the depth of the well (a) is equal to the length of each rope plus the deficiency:
# a = b + 2 = c + 3 = d + 4 = e + 5 = f + 6

# Step 1: Express all variables in terms of `b` (甲綆長).
# From the relationships:
c = lambda b: b + 2  # 乙綆長
d = lambda b: c(b) + 3  # 丙綆長
e = lambda b: d(b) + 4  # 丁綆長
f = lambda b: e(b) + 5  # 戊綆長
a = lambda b: b + 2  # 井深

# Step 2: Solve for `b` using the cyclic relationship f = b - 6.
# Substituting f(b) into the equation:
# f(b) = b - 6
# e(b) + 5 = b - 6
# d(b) + 4 + 5 = b - 6
# c(b) + 3 + 4 + 5 = b - 6
# b + 2 + 3 + 4 + 5 = b - 6
# 14 = -6
#

"""

"""


"""
Variable 'a' has wrong value. Expected: 721/100, Actual: <function <lambda> at 0x7f1fdfa17640>
Missing variable in output: 'b'
Variable 'c' has wrong value. Expected: 191/100, Actual: <function <lambda> at 0x7f1fdfa17a30>
Variable 'd' has wrong value. Expected: 37/25, Actual: <function <lambda> at 0x7f1fdfa17d00>
Variable 'e' has wrong value. Expected: 129/100, Actual: <function <lambda> at 0x7f1fdfa17880>
Variable 'f' has wrong value. Expected: 38/5, Actual: <function <lambda> at 0x7f1fdfa171c0>"""
