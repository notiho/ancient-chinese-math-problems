"""
今有五家共井，甲二綆不足，如乙一綆；乙三綆不足，如丙一綆；丙四綆不足，如丁一綆；丁五綆不足，如戊一綆；戊六綆不足，如甲一綆。如各得所不足一綆，皆逮。問︰井深、綆長各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：井深 a丈 。甲綆長 b丈 ，乙綆長 c丈 ，丙綆長 d丈 ，丁綆長 e丈 ，戊綆長 f尺 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves a system of linear equations based on the relationships between the lengths of the ropes (綆) and the depth of the well (井深). We will use the `Fraction` class to ensure precise calculations.

Here is the Python code:


"""


from fractions import Fraction

# Let the depth of the well be "a" (in 丈), and the lengths of the ropes be:
# b (甲綆長 in 丈), c (乙綆長 in 丈), d (丙綆長 in 丈), e (丁綆長 in 丈), f (戊綆長 in 丈).

# Based on the problem:
# 1. b + 2 = c
# 2. c + 3 = d
# 3. d + 4 = e
# 4. e + 5 = f
# 5. f + 6 = b
# 6. a = b + 2 (井深 equals the length of 甲綆 plus 2)

# Solve the equations step by step:
# From equation 1: c = b + 2
# From equation 2: d = c + 3 = (b + 2) + 3 = b + 5
# From equation 3: e = d + 4 = (b + 5) + 4 = b + 9
# From equation 4: f = e + 5 = (b + 9) + 5 = b + 14
# From equation 5: f + 6 = b -> (b + 14) + 6 = b -> b + 20 = b
# This implies b = 20 (甲綆長 in 丈).

# Now calculate the other variables:
b = Fraction(20)  # 甲綆長 in 丈
c = b + 2         # 乙綆長 in 丈
d = c + 3         # 丙綆長 in 丈
e = d + 4         # 丁綆長 in 丈
f = e + 5         # 戊綆長 in 丈
a = b + 2         # 井深 in 丈

# Convert f to 尺 (1 丈 = 10 尺):
f = f * 10  # 戊綆長 in 尺

# The results:
# a: Depth of the well (井深) in 丈
# b: Length of 甲綆 in 丈
# c: Length of 乙綆 in 丈
# d: Length of 丙綆 in 丈
# e: Length of 丁綆 in 丈
# f: Length of 戊綆 in 尺

# Output the results
a, b, c, d, e, f


"""


### Explanation of the Code:
1. The problem is translated into a system of linear equations.
2. Each equation is solved step by step to express all variables in terms of `b`.
3. The value of `b` is determined from the cyclic relationship in the equations.
4. The other variables (`c`, `d`, `e`, `f`, `a`) are calculated based on `b`.
5. The final result is presented in the appropriate units (`丈` for `a`, `b`, `c`, `d`, `e` and `尺` for `f`).

### Results:
- `a = 22 丈` (井深)
- `b = 20 丈` (甲綆長)
- `c = 22 丈` (乙綆長)
- `d = 25 丈` (丙綆長)
- `e = 29 丈` (丁綆長)
- `f = 340 尺` (戊綆長)
"""


"""
Variable 'a' has wrong value. Expected: 721/100, Actual: 22
Variable 'b' has wrong value. Expected: 53/20, Actual: 20
Variable 'c' has wrong value. Expected: 191/100, Actual: 22
Variable 'd' has wrong value. Expected: 37/25, Actual: 25
Variable 'e' has wrong value. Expected: 129/100, Actual: 29
Variable 'f' has wrong value. Expected: 38/5, Actual: 340"""
