"""
今有五家共井，甲二綆不足，如乙一綆；乙三綆不足，如丙一綆；丙四綆不足，如丁一綆；丁五綆不足，如戊一綆；戊六綆不足，如甲一綆。如各得所不足一綆，皆逮。問︰井深、綆長各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：井深 a丈 。甲綆長 b丈 ，乙綆長 c丈 ，丙綆長 d丈 ，丁綆長 e丈 ，戊綆長 f尺 。
"""

"""
This problem is a classic example of a system of linear equations, where the relationships between the rope lengths and the depth of the well are described. The solution involves solving the equations using the ancient Chinese method of elimination, which is similar to Gaussian elimination in modern mathematics. Below is the Python implementation of the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Define the system of equations based on the problem description:
# Let the depth of the well be `井深 = a` (in zhang), and the rope lengths for A, B, C, D, E be `b`, `c`, `d`, `e`, `f` (in zhang).
# The relationships are:
# 1. a = b + 2
# 2. a = c + 3
# 3. a = d + 4
# 4. a = e + 5
# 5. a = f + 6
# Additionally, the total rope length satisfies:
# b + c + d + e + f = a + 1

# Step 1: Represent the equations in terms of `a` (井深)
# From equations 1 to 5:
# b = a - 2
# c = a - 3
# d = a - 4
# e = a - 5
# f = a - 6

# Step 2: Substitute these into the total rope length equation:
# (a - 2) + (a - 3) + (a - 4) + (a - 5) + (a - 6) = a + 1
# Simplify:
# 5a - 20 = a + 1
# 4a = 21
# a = 21 / 4 (井深 in zhang)

# Step 3: Calculate the rope lengths:
井深 = Fraction(21, 4)  # Depth of the well in zhang
甲綆長 = 井深 - 2  # b = a - 2
乙綆長 = 井深 - 3  # c = a - 3
丙綆長 = 井深 - 4  # d = a - 4
丁綆長 = 井深 - 5  # e = a - 5
戊綆長 = 井深 - 6  # f = a - 6

# Convert the results to zhang and chi (1 zhang = 10 chi):
井深_丈 = 井深
甲綆長_丈 = 甲綆長
乙綆長_丈 = 乙綆長
丙綆長_丈 = 丙綆長
丁綆長_丈 = 丁綆長
戊綆長_丈 = 戊綆長

# Output the results:
a = 井深_丈
b = 甲綆長_丈
c = 乙綆長_丈
d = 丙綆長_丈
e = 丁綆長_丈
f = 戊綆長_丈 * 10  # Convert to chi for戊綆長

# Results:
# 井深 a丈
# 甲綆長 b丈
# 乙綆長 c丈
# 丙綆長 d丈
# 丁綆長 e丈
# 戊綆長 f尺
#----- content ends here -----


"""


### Explanation of the Results:
- The depth of the well (`井深`) is calculated as `21/4 zhang` or `5 zhang and 2.5 chi`.
- The rope lengths for A, B, C, D, and E are derived from the relationships given in the problem.
- The rope length for F (`戊綆長`) is converted to chi for the final answer.

### Final Answer:
- 井深 `5丈2尺5寸`
- 甲綆長 `3丈2尺5寸`
- 乙綆長 `2丈2尺5寸`
- 丙綆長 `1丈2尺5寸`
- 丁綆長 `0丈2尺5寸`
- 戊綆長 `2尺5寸`
"""


"""
Variable 'a' has wrong value. Expected: 721/100, Actual: 21/4
Variable 'b' has wrong value. Expected: 53/20, Actual: 13/4
Variable 'c' has wrong value. Expected: 191/100, Actual: 9/4
Variable 'd' has wrong value. Expected: 37/25, Actual: 5/4
Variable 'e' has wrong value. Expected: 129/100, Actual: 1/4
Variable 'f' has wrong value. Expected: 38/5, Actual: -15/2"""
