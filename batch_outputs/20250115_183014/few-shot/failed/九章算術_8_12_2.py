"""
今有五家共井，甲二綆不足，如乙一綆；乙三綆不足，如丙一綆；丙四綆不足，如丁一綆；丁五綆不足，如戊一綆；戊六綆不足，如甲一綆。如各得所不足一綆，皆逮。問︰井深、綆長各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：井深 a丈 。甲綆長 b丈 ，乙綆長 c丈 ，丙綆長 d丈 ，丁綆長 e丈 ，戊綆長 f尺 。
"""

"""
This problem involves solving a system of linear equations using ancient Chinese methods, specifically the "正負術" (positive and negative method) and "方程術" (method of equations). The problem describes a scenario where five families share a well, and their rope lengths are interrelated. The goal is to find the depth of the well and the rope lengths for each family.

Let's translate this into Python step by step.


"""


from fractions import Fraction

# Define the system of equations based on the problem:
# Let the depth of the well be `井深 = a` (in zhang), and the rope lengths for each family be:
# 甲綆長 = b, 乙綆長 = c, 丙綆長 = d, 丁綆長 = e, 戊綆長 = f (all in zhang).

# Equations derived from the problem:
# 1. a = b + 2
# 2. a = c + 3
# 3. a = d + 4
# 4. a = e + 5
# 5. a = f + 6
# 6. b = c + 1
# 7. c = d + 1
# 8. d = e + 1
# 9. e = f + 1

# Solve the system step by step using substitution.

# Start with the last equation: e = f + 1
f = Fraction(1)  # Assume f = 1 (尺, smallest unit)
e = f + 1

# d = e + 1
d = e + 1

# c = d + 1
c = d + 1

# b = c + 1
b = c + 1

# a = b + 2
a = b + 2

# Convert the depth of the well (a) and rope lengths to zhang and chi.
井深 = a  # Depth of the well in zhang
甲綆長 = b  # Rope length for 甲 in zhang
乙綆長 = c  # Rope length for 乙 in zhang
丙綆長 = d  # Rope length for 丙 in zhang
丁綆長 = e  # Rope length for 丁 in zhang
戊綆長 = f  # Rope length for 戊 in zhang

# Output the results.
print(f"井深: {井深} 丈")
print(f"甲綆長: {甲綆長} 丈")
print(f"乙綆長: {乙綆長} 丈")
print(f"丙綆長: {丙綆長} 丈")
print(f"丁綆長: {丁綆長} 丈")
print(f"戊綆長: {戊綆長} 丈")


"""


### Explanation of the Code:
1. **Equations Setup**: The problem is translated into a system of linear equations based on the relationships between the well's depth and the rope lengths.
2. **Substitution**: The equations are solved step by step using substitution, starting from the last equation (`e = f + 1`) and working upwards.
3. **Fractions**: The `Fraction` class is used to ensure precise arithmetic for non-integer values.
4. **Output**: The results are printed in terms of zhang (丈), the unit of measurement for depth and rope lengths.

### Answer:
The depth of the well (`井深`) and the rope lengths for each family (`甲綆長`, `乙綆長`, `丙綆長`, `丁綆長`, `戊綆長`) are calculated and displayed.
"""


"""
Variable 'a' has wrong value. Expected: 721/100, Actual: 7
Variable 'b' has wrong value. Expected: 53/20, Actual: 5
Variable 'c' has wrong value. Expected: 191/100, Actual: 4
Variable 'd' has wrong value. Expected: 37/25, Actual: 3
Variable 'e' has wrong value. Expected: 129/100, Actual: 2
Variable 'f' has wrong value. Expected: 38/5, Actual: 1"""
