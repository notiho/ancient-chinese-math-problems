"""
今有五家共井，甲二綆不足，如乙一綆；乙三綆不足，如丙一綆；丙四綆不足，如丁一綆；丁五綆不足，如戊一綆；戊六綆不足，如甲一綆。如各得所不足一綆，皆逮。問︰井深、綆長各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：井深 a丈 。甲綆長 b丈 ，乙綆長 c丈 ，丙綆長 d丈 ，丁綆長 e丈 ，戊綆長 f尺 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves finding the depth of the well (`a`) and the lengths of the ropes (`b`, `c`, `d`, `e`, `f`) such that the given conditions are satisfied. We'll use the `Fraction` class to handle fractional values.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Define the unknowns
# Let the depth of the well be `a` (in 丈)
# Let the rope lengths be `b`, `c`, `d`, `e`, `f` (in 丈 for b, c, d, e, and in 尺 for f)

# The problem states:
# 1. 甲二綆不足，如乙一綆: 2b = c - a
# 2. 乙三綆不足，如丙一綆: 3c = d - a
# 3. 丙四綆不足，如丁一綆: 4d = e - a
# 4. 丁五綆不足，如戊一綆: 5e = f/10 - a (convert f from 尺 to 丈 by dividing by 10)
# 5. 戊六綆不足，如甲一綆: 6f/10 = b - a

# Solve the equations step by step
# From equation 1: c = 2b + a
# From equation 2: d = 3c + a = 3(2b + a) + a = 6b + 4a
# From equation 3: e = 4d + a = 4(6b + 4a) + a = 24b + 17a
# From equation 4: f/10 = 5e + a = 5(24b + 17a) + a = 120b + 86a
# Multiply through by 10 to eliminate the fraction: f = 1200b + 860a
# From equation 5: 6f/10 = b - a
# Simplify: 6f = 10b - 10a
# Substitute f = 1200b + 860a into 6f = 10b - 10a:
# 6(1200b + 860a) = 10b - 10a
# 7200b + 5160a = 10b - 10a
# 7200b - 10b + 5160a + 10a = 0
# 7190b + 5170a = 0

# Solve for b in terms of a: b = -5170a / 7190
# Simplify the fraction: b = -517a / 719

# Substitute b into the equations to find the other unknowns
a = Fraction(1)  # Assume a = 1 丈 for simplicity (can scale later if needed)
b = -517 * a / 719
c = 2 * b + a
d = 6 * b + 4 * a
e = 24 * b + 17 * a
f = 1200 * b + 860 * a

# Print the results
a = a  # Depth of the well in 丈
b = b  # Length of 甲 rope in 丈
c = c  # Length of 乙 rope in 丈
d = d  # Length of 丙 rope in 丈
e = e  # Length of 丁 rope in 丈
f = f  # Length of 戊 rope in 尺

print(f"井深 a = {a} 丈")
print(f"甲綆長 b = {b} 丈")
print(f"乙綆長 c = {c} 丈")
print(f"丙綆長 d = {d} 丈")
print(f"丁綆長 e = {e} 丈")
print(f"戊綆長 f = {f} 尺")
#----- content ends here -----


"""


This code computes the values of `a`, `b`, `c`, `d`, `e`, and `f` based on the given conditions. The solution assumes `a = 1` 丈 for simplicity, but the relationships between the variables remain valid regardless of the scaling factor.
"""


"""
Variable 'a' has wrong value. Expected: 721/100, Actual: 1
Variable 'b' has wrong value. Expected: 53/20, Actual: -517/719
Variable 'c' has wrong value. Expected: 191/100, Actual: -315/719
Variable 'd' has wrong value. Expected: 37/25, Actual: -226/719
Variable 'e' has wrong value. Expected: 129/100, Actual: -185/719
Variable 'f' has wrong value. Expected: 38/5, Actual: -2060/719"""
