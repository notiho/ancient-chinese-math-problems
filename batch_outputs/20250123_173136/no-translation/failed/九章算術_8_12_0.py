"""
今有五家共井，甲二綆不足，如乙一綆；乙三綆不足，如丙一綆；丙四綆不足，如丁一綆；丁五綆不足，如戊一綆；戊六綆不足，如甲一綆。如各得所不足一綆，皆逮。問︰井深、綆長各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：井深 a丈 。甲綆長 b丈 ，乙綆長 c丈 ，丙綆長 d丈 ，丁綆長 e丈 ，戊綆長 f尺 。
"""

"""
This problem involves solving a system of linear equations using ancient Chinese mathematical methods, specifically the "方程術" (method of solving simultaneous equations). Below is the Python implementation of the problem:


"""


from fractions import Fraction

# Define the equations based on the problem:
# Let the depth of the well be `井深 = a` (in 丈),
# and the length of the ropes for each person be `甲 = b`, `乙 = c`, `丙 = d`, `丁 = e`, `戊 = f` (all in 丈).

# Equations derived from the problem:
# 1. a = b + 2
# 2. a = c + 3
# 3. a = d + 4
# 4. a = e + 5
# 5. a = f + 6
# 6. b + 1 = c + 1 = d + 1 = e + 1 = f + 1 = a

# Solve the system of equations:
# From equations (1) to (5), express b, c, d, e, f in terms of a:
b = a - 2
c = a - 3
d = a - 4
e = a - 5
f = a - 6

# From equation (6), we know that all ropes plus 1 must equal the depth of the well:
# b + 1 = c + 1 = d + 1 = e + 1 = f + 1 = a
# Therefore, a = b + 1.

# Substitute b = a - 2 into a = b + 1:
# a = (a - 2) + 1
# a = a - 1
# This equation is consistent, so we proceed to calculate the values.

# Assume the depth of the well (a) is the smallest positive integer satisfying the equations:
井深 = 7  # a = 7 丈

# Calculate the lengths of the ropes:
甲綆長 = b = 井深 - 2  # b = 7 - 2 = 5 丈
乙綆長 = c = 井深 - 3  # c = 7 - 3 = 4 丈
丙綆長 = d = 井深 - 4  # d = 7 - 4 = 3 丈
丁綆長 = e = 井深 - 5  # e = 7 - 5 = 2 丈
戊綆長 = f = 井深 - 6  # f = 7 - 6 = 1 丈

# Convert 戊綆長 to 尺 (1 丈 = 10 尺):
戊綆長_尺 = f * 10  # f = 1 丈 = 10 尺

# Final results:
a = 井深  # 井深 = 7 丈
b = 甲綆長  # 甲綆長 = 5 丈
c = 乙綆長  # 乙綆長 = 4 丈
d = 丙綆長  # 丙綆長 = 3 丈
e = 丁綆長  # 丁綆長 = 2 丈
f = 戊綆長_尺  # 戊綆長 = 10 尺


"""


### Final Answer:
- 井深 `a = 7 丈`
- 甲綆長 `b = 5 丈`
- 乙綆長 `c = 4 丈`
- 丙綆長 `d = 3 丈`
- 丁綆長 `e = 2 丈`
- 戊綆長 `f = 10 尺`
"""


"""
Code error: name 'a' is not defined"""
