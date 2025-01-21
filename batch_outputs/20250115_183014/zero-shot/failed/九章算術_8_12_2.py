"""
今有五家共井，甲二綆不足，如乙一綆；乙三綆不足，如丙一綆；丙四綆不足，如丁一綆；丁五綆不足，如戊一綆；戊六綆不足，如甲一綆。如各得所不足一綆，皆逮。問︰井深、綆長各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：井深 a丈 。甲綆長 b丈 ，乙綆長 c丈 ，丙綆長 d丈 ，丁綆長 e丈 ，戊綆長 f尺 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves finding the depth of the well (`a`) and the lengths of the ropes (`b`, `c`, `d`, `e`, `f`) such that the given conditions are satisfied. We'll use the `Fraction` class to handle fractional values.

Here is the Python code:


"""


from fractions import Fraction

# Define the unknowns
# Let the depth of the well be `a` (in 丈)
# Let the rope lengths be `b`, `c`, `d`, `e` (in 丈), and `f` (in 尺)

# The relationships given in the problem:
# 1. a - 2b = c
# 2. a - 3c = d
# 3. a - 4d = e
# 4. a - 5e = f / 10 (convert 尺 to 丈 by dividing by 10)
# 5. a - 6f / 10 = b

# Solve the equations step by step
# From equation 4: f = 10 * (a - 5e)
# Substitute f into equation 5: a - 6 * (10 * (a - 5e)) / 10 = b
# Simplify: a - 6(a - 5e) = b
# a - 6a + 30e = b
# -5a + 30e = b  (Equation A)

# From equation 3: e = a - 4d
# Substitute e into Equation A: -5a + 30(a - 4d) = b
# Simplify: -5a + 30a - 120d = b
# 25a - 120d = b  (Equation B)

# From equation 2: d = a - 3c
# Substitute d into Equation B: 25a - 120(a - 3c) = b
# Simplify: 25a - 120a + 360c = b
# -95a + 360c = b  (Equation C)

# From equation 1: c = a - 2b
# Substitute c into Equation C: -95a + 360(a - 2b) = b
# Simplify: -95a + 360a - 720b = b
# 265a - 720b = b
# 265a = 721b
# b = 265a / 721

# Now substitute b back to find other variables
a = Fraction(721, 265)  # Depth of the well in 丈
b = Fraction(265, 721) * a  # Length of rope b in 丈
c = a - 2 * b  # Length of rope c in 丈
d = a - 3 * c  # Length of rope d in 丈
e = a - 4 * d  # Length of rope e in 丈
f = 10 * (a - 5 * e)  # Length of rope f in 尺

# Results
a  #井深 (depth of the well) in 丈
b  #甲綆長 (length of rope b) in 丈
c  #乙綆長 (length of rope c) in 丈
d  #丙綆長 (length of rope d) in 丈
e  #丁綆長 (length of rope e) in 丈
f  #戊綆長 (length of rope f) in 尺


"""


### Explanation:
1. The problem is modeled as a system of linear equations.
2. The relationships between the variables are derived step by step.
3. The `Fraction` class ensures precise calculations for fractional values.
4. The final results are stored in variables `a`, `b`, `c`, `d`, `e`, and `f`.

You can run this code to compute the exact values of the unknowns.
"""


"""
Variable 'a' has wrong value. Expected: 721/100, Actual: 721/265
Variable 'b' has wrong value. Expected: 53/20, Actual: 1
Variable 'c' has wrong value. Expected: 191/100, Actual: 191/265
Variable 'd' has wrong value. Expected: 37/25, Actual: 148/265
Variable 'e' has wrong value. Expected: 129/100, Actual: 129/265
Variable 'f' has wrong value. Expected: 38/5, Actual: 152/53"""
