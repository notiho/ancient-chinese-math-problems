"""
今有五家共井，甲二綆不足，如乙一綆；乙三綆不足，如丙一綆；丙四綆不足，如丁一綆；丁五綆不足，如戊一綆；戊六綆不足，如甲一綆。如各得所不足一綆，皆逮。問︰井深、綆長各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：井深 a丈 。甲綆長 b丈 ，乙綆長 c丈 ，丙綆長 d丈 ，丁綆長 e丈 ，戊綆長 f尺 。
"""

"""
To solve this problem, we need to use the ancient Chinese "方程術" (method of simultaneous equations). The problem describes a system of linear equations based on the relationships between the lengths of the ropes (綆) and the depth of the well (井深). Let's translate this into Python code step by step.


"""

#----- content starts here -----

from fractions import Fraction

# Define the unknowns:
# Let the depth of the well be `a` (in 丈).
# Let the rope lengths for 甲, 乙, 丙, 丁, 戊 be `b`, `c`, `d`, `e`, `f` respectively (in 丈).

# The relationships are:
# 1. b + 2 = c
# 2. c + 3 = d
# 3. d + 4 = e
# 4. e + 5 = f
# 5. f + 6 = b + a

# Rewrite the equations in terms of `a`:
# From (1): c = b + 2
# From (2): d = c + 3 = b + 2 + 3 = b + 5
# From (3): e = d + 4 = b + 5 + 4 = b + 9
# From (4): f = e + 5 = b + 9 + 5 = b + 14
# From (5): f + 6 = b + a -> b + 14 + 6 = b + a -> a = 20

# Solve for the rope lengths:
a = 20  #井深 (in 丈)
b = Fraction(0)  #甲綆長 (in 丈)
c = b + 2  #乙綆長 (in 丈)
d = c + 3  #丙綆長 (in 丈)
e = d + 4  #丁綆長 (in 丈)
f = e + 5  #戊綆長 (in 丈)

# Convert to 丈 and 尺 where necessary:
# 1 丈 = 10 尺
井深 = a  # in 丈
甲綆長 = b  # in 丈
乙綆長 = c  # in 丈
丙綆長 = d  # in 丈
丁綆長 = e  # in 丈
戊綆長 = f * 10  # in 尺

# Output the results:
print(f"井深 {井深} 丈。")
print(f"甲綆長 {甲綆長} 丈，乙綆長 {乙綆長} 丈，丙綆長 {丙綆長} 丈，丁綆長 {丁綆長} 丈，戊綆長 {戊綆長} 尺。")
#----- content ends here -----


"""


### Explanation:
1. The equations are derived from the problem statement, where each person's rope length is related to the next person's rope length plus a fixed amount.
2. The depth of the well (`a`) is determined by the cyclic relationship involving all five ropes.
3. The solution uses fractions to ensure accuracy in calculations.
4. The final results are converted to the appropriate units (丈 for depth and rope lengths, 尺 for the last rope length).

### Results:
- 井深: `a` 丈
- 甲綆長: `b` 丈
- 乙綆長: `c` 丈
- 丙綆長: `d` 丈
- 丁綆長: `e` 丈
- 戊綆長: `f` 尺
"""


"""
Variable 'a' has wrong value. Expected: 721/100, Actual: 20
Variable 'b' has wrong value. Expected: 53/20, Actual: 0
Variable 'c' has wrong value. Expected: 191/100, Actual: 2
Variable 'd' has wrong value. Expected: 37/25, Actual: 5
Variable 'e' has wrong value. Expected: 129/100, Actual: 9
Variable 'f' has wrong value. Expected: 38/5, Actual: 14"""
