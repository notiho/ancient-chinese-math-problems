"""
今有五家共井甲二綆不足如乙一綆乙三綆不足如丙一綆丙四綆不足如丁一綆丁五綆不足如戊一綆戊六綆不足如甲一綆如各得所不足一綆皆逮問井深綆長各幾何
術曰如方程以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰井深 a丈 甲綆長 b丈 乙綆長 c丈 丙綆長 d丈 丁綆長 e丈 戊綆長 f尺 
"""

"""
This problem involves solving a system of equations using ancient Chinese methods, specifically the "方程術" (method of solving simultaneous equations). The problem is complex and involves multiple variables and relationships between them. Below is the solution translated into Python code, following the structure of the procedure described.


"""


"""
Suppose there are five families sharing a well:
- Family A's rope is 2 units short of reaching the water as Family B's rope is 1 unit short.
- Family B's rope is 3 units short of reaching the water as Family C's rope is 1 unit short.
- Family C's rope is 4 units short of reaching the water as Family D's rope is 1 unit short.
- Family D's rope is 5 units short of reaching the water as Family E's rope is 1 unit short.
- Family E's rope is 6 units short of reaching the water as Family A's rope is 1 unit short.

If each family receives the amount of rope they are short by, all ropes will reach the water.

Question: What is the depth of the well and the length of each family's rope?

The procedure says: Use the method of solving simultaneous equations ("方程術").
The answer says: The well is *a* zhang deep, and the ropes of families A, B, C, D, and E are *b*, *c*, *d*, *e*, and *f* zhang respectively.
"""

from fractions import Fraction

# Define the variables:
# Let the depth of the well be `井深 = a`
# Let the rope lengths of families A, B, C, D, and E be `甲綆 = b`, `乙綆 = c`, `丙綆 = d`, `丁綆 = e`, and `戊綆 = f`.

# The relationships between the ropes and the well depth are:
# 1. a = b + 2
# 2. a = c + 3
# 3. a = d + 4
# 4. a = e + 5
# 5. a = f + 6

# Additionally, the total amount of rope added to each family to make up the shortfall is equal to the depth of the well:
# (2 + 1) + (3 + 1) + (4 + 1) + (5 + 1) + (6 + 1) = a

# Solve for the depth of the well (a):
a = 2 + 1 + 3 + 1 + 4 + 1 + 5 + 1 + 6 + 1  # Total shortfall
a = Fraction(a)  # Depth of the well in zhang

# Solve for the rope lengths:
b = a - 2  # Rope length for family A
c = a - 3  # Rope length for family B
d = a - 4  # Rope length for family C
e = a - 5  # Rope length for family D
f = a - 6  # Rope length for family E

# Output the results:
井深 = a
甲綆 = b
乙綆 = c
丙綆 = d
丁綆 = e
戊綆 = f

井深, 甲綆, 乙綆, 丙綆, 丁綆, 戊綆


"""


### Explanation:
1. The depth of the well (`a`) is calculated by summing up all the shortfall amounts for each family.
2. The rope lengths for each family are derived from the depth of the well minus their respective shortfall amounts.
3. The solution uses the `Fraction` class to ensure precise calculations, as the results may not always be integers.

### Answer:
- The well is `a` zhang deep.
- The rope lengths for families A, B, C, D, and E are `b`, `c`, `d`, `e`, and `f` zhang respectively.
"""


"""
Variable 'a' has wrong value. Expected: 721/100, Actual: 25
Variable 'b' has wrong value. Expected: 53/20, Actual: 23
Variable 'c' has wrong value. Expected: 191/100, Actual: 22
Variable 'd' has wrong value. Expected: 37/25, Actual: 21
Variable 'e' has wrong value. Expected: 129/100, Actual: 20
Variable 'f' has wrong value. Expected: 38/5, Actual: 19"""
