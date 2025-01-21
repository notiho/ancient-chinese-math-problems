"""
今有五家共井，甲二綆不足，如乙一綆；乙三綆不足，如丙一綆；丙四綆不足，如丁一綆；丁五綆不足，如戊一綆；戊六綆不足，如甲一綆。如各得所不足一綆，皆逮。問︰井深、綆長各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：井深 a丈 。甲綆長 b丈 ，乙綆長 c丈 ，丙綆長 d丈 ，丁綆長 e丈 ，戊綆長 f尺 。
"""

"""
This problem involves solving a system of linear equations, which is described in the ancient Chinese mathematical text using the "方程術" (method of solving simultaneous equations). Below is the Python implementation of the procedure:


"""


from fractions import Fraction

# Define the equations based on the problem:
# Let the depth of the well be `井深 = a` (in 丈), and the rope lengths for each person be:
# 甲綆長 = b, 乙綆長 = c, 丙綆長 = d, 丁綆長 = e, 戊綆長 = f (all in 丈).

# Equations derived from the problem:
# 1. b = a - 2
# 2. c = a - 3
# 3. d = a - 4
# 4. e = a - 5
# 5. f = a - 6
# 6. b + c + d + e + f = a + 5 (each gets one extra rope length to reach the well depth)

# Step 1: Express all rope lengths in terms of `a`:
# Substitute equations 1-5 into equation 6:
# (a - 2) + (a - 3) + (a - 4) + (a - 5) + (a - 6) = a + 5

# Step 2: Simplify the equation:
# 5a - 20 = a + 5
# 4a = 25
# a = 25 / 4

# Step 3: Calculate the rope lengths:
井深 = Fraction(25, 4)  # Well depth in 丈
甲綆長 = 井深 - 2
乙綆長 = 井深 - 3
丙綆長 = 井深 - 4
丁綆長 = 井深 - 5
戊綆長 = 井深 - 6

# Convert 戊綆長 to 尺 (1 丈 = 10 尺):
戊綆長_尺 = 戊綆長 * 10

# Results:
a = 井深  # Well depth in 丈
b = 甲綆長  # Rope length for 甲 in 丈
c = 乙綆長  # Rope length for 乙 in 丈
d = 丙綆長  # Rope length for 丙 in 丈
e = 丁綆長  # Rope length for 丁 in 丈
f = 戊綆長_尺  # Rope length for 戊 in 尺


"""


### Final Answer:
- 井深 (Well depth): `a = 6丈2尺` (or `25/4 丈`)
- 甲綆長 (Rope length for 甲): `b = 4丈2尺` (or `17/4 丈`)
- 乙綆長 (Rope length for 乙): `c = 3丈2尺` (or `13/4 丈`)
- 丙綆長 (Rope length for 丙): `d = 2丈2尺` (or `9/4 丈`)
- 丁綆長 (Rope length for 丁): `e = 1丈2尺` (or `5/4 丈`)
- 戊綆長 (Rope length for 戊): `f = 2尺` (or `1/2 丈`)
"""


"""
Variable 'a' has wrong value. Expected: 721/100, Actual: 25/4
Variable 'b' has wrong value. Expected: 53/20, Actual: 17/4
Variable 'c' has wrong value. Expected: 191/100, Actual: 13/4
Variable 'd' has wrong value. Expected: 37/25, Actual: 9/4
Variable 'e' has wrong value. Expected: 129/100, Actual: 5/4
Variable 'f' has wrong value. Expected: 38/5, Actual: 5/2"""
