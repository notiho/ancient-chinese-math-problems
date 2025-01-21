"""
今有五家共井甲二綆不足如乙一綆乙三綆不足如丙一綆丙四綆不足如丁一綆丁五綆不足如戊一綆戊六綆不足如甲一綆如各得所不足一綆皆逮問井深綆長各幾何
術曰如方程以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰井深 a丈 甲綆長 b丈 乙綆長 c丈 丙綆長 d丈 丁綆長 e丈 戊綆長 f尺 
"""

"""
This problem is a classic example of a system of linear equations, where the relationships between the lengths of the ropes and the depth of the well are described. The solution involves solving these equations using the ancient Chinese "fangcheng" (方程) method, which is essentially a precursor to modern matrix operations.

Here is the solution encoded in Python:


"""


from fractions import Fraction

# Define the system of equations based on the problem:
# Let the depth of the well be `a` (in zhang), and the rope lengths for A, B, C, D, E be `b`, `c`, `d`, `e`, `f` (in zhang).
# The equations are:
# b = a - 2
# c = a - 3
# d = a - 4
# e = a - 5
# f = a - 6

# Step 1: Represent the equations in terms of `a` (井深):
# b = a - 2
# c = a - 3
# d = a - 4
# e = a - 5
# f = a - 6

# Step 2: Solve for `a` (井深):
# Since each rope is 1 zhang short of the next, the depth of the well is determined by the longest rope plus its shortage.

# Calculate the depth of the well (井深):
a = 6  # The depth of the well in zhang (since the longest rope is 6 zhang short).

# Step 3: Calculate the lengths of the ropes:
b = a - 2  # Rope length for A
c = a - 3  # Rope length for B
d = a - 4  # Rope length for C
e = a - 5  # Rope length for D
f = a - 6  # Rope length for E

# Convert the results to fractions for precision:
a = Fraction(a)
b = Fraction(b)
c = Fraction(c)
d = Fraction(d)
e = Fraction(e)
f = Fraction(f)

# Output the results:
print(f"井深: {a}丈")
print(f"甲綆長: {b}丈")
print(f"乙綆長: {c}丈")
print(f"丙綆長: {d}丈")
print(f"丁綆長: {e}丈")
print(f"戊綆長: {f}丈")


"""


### Explanation of the Solution:
1. **Problem Setup**:
   - The problem describes a scenario where five families share a well, and each family's rope is shorter than the depth of the well by a certain amount.
   - The relationships between the ropes and the depth of the well are given as linear equations.

2. **Fangcheng Method**:
   - The ancient Chinese "fangcheng" method is essentially a way to solve systems of linear equations. In this case, the equations are simple enough to solve directly without needing advanced matrix operations.

3. **Solution**:
   - The depth of the well (`a`) is determined by the longest rope's shortage (6 zhang).
   - The lengths of the ropes are calculated by subtracting the respective shortages from the depth of the well.

4. **Output**:
   - The depth of the well and the lengths of the ropes are expressed in zhang (丈), with the results converted to fractions for precision.

### Final Answer:
- 井深: 6丈
- 甲綆長: 4丈
- 乙綆長: 3丈
- 丙綆長: 2丈
- 丁綆長: 1丈
- 戊綆長: 0丈
"""


"""
Variable 'a' has wrong value. Expected: 721/100, Actual: 6
Variable 'b' has wrong value. Expected: 53/20, Actual: 4
Variable 'c' has wrong value. Expected: 191/100, Actual: 3
Variable 'd' has wrong value. Expected: 37/25, Actual: 2
Variable 'e' has wrong value. Expected: 129/100, Actual: 1
Variable 'f' has wrong value. Expected: 38/5, Actual: 0"""
