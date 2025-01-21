"""
今有五家共井，甲二綆不足，如乙一綆；乙三綆不足，如丙一綆；丙四綆不足，如丁一綆；丁五綆不足，如戊一綆；戊六綆不足，如甲一綆。如各得所不足一綆，皆逮。問︰井深、綆長各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：井深 a丈 。甲綆長 b丈 ，乙綆長 c丈 ，丙綆長 d丈 ，丁綆長 e丈 ，戊綆長 f尺 。
"""

"""
This problem involves solving a system of equations using ancient Chinese methods, specifically the "正負術" (positive and negative method) and "方程術" (method of equations). I'll translate the procedure into Python code to solve for the depth of the well and the rope lengths.


"""


from fractions import Fraction

# Define the equations based on the problem:
# Let the depth of the well be `井深 = a` (in 丈), and the rope lengths for each person be:
# 甲綆長 = b, 乙綆長 = c, 丙綆長 = d, 丁綆長 = e, 戊綆長 = f (all in 丈).

# Equations derived from the problem:
# 1. a = b + 2
# 2. a = c + 3
# 3. a = d + 4
# 4. a = e + 5
# 5. a = f + 6
# 6. b + c + d + e + f = a + 5 (each gets one extra rope length to make up for the deficit)

# Solve the system of equations:
# From equations 1-5, express b, c, d, e, f in terms of a:
b = a - 2
c = a - 3
d = a - 4
e = a - 5
f = a - 6

# Substitute these into equation 6:
# (a - 2) + (a - 3) + (a - 4) + (a - 5) + (a - 6) = a + 5
# Simplify:
5 * a - 20 = a + 5
4 * a = 25
a = Fraction(25, 4)  # Depth of the well in 丈

# Calculate the rope lengths:
b = a - 2
c = a - 3
d = a - 4
e = a - 5
f = a - 6

# Convert the results to 丈 and 尺 (1 丈 = 10 尺):
井深 = a
甲綆長 = b
乙綆長 = c
丙綆長 = d
丁綆長 = e
戊綆長 = f * 10  # Convert to 尺 for 戊

# Output the results:
井深丈 = 井深
甲綆長丈 = 甲綆長
乙綆長丈 = 乙綆長
丙綆長丈 = 丙綆長
丁綆長丈 = 丁綆長
戊綆長尺 = 戊綆長

井深丈, 甲綆長丈, 乙綆長丈, 丙綆長丈, 丁綆長丈, 戊綆長尺


"""


### Explanation of Results:
- `井深丈` is the depth of the well in 丈.
- `甲綆長丈`, `乙綆長丈`, `丙綆長丈`, `丁綆長丈` are the rope lengths for 甲, 乙, 丙, 丁 in 丈.
- `戊綆長尺` is the rope length for 戊 in 尺.

This code follows the ancient Chinese method of solving systems of equations and provides the solution in terms of fractions to ensure accuracy.
"""


"""
Code error: cannot assign to expression here. Maybe you meant '==' instead of '='? (<string>, line 28)"""
