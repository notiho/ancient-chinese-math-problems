"""
今有五家共井，甲二綆不足，如乙一綆；乙三綆不足，如丙一綆；丙四綆不足，如丁一綆；丁五綆不足，如戊一綆；戊六綆不足，如甲一綆。如各得所不足一綆，皆逮。問︰井深、綆長各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：井深 a丈 。甲綆長 b丈 ，乙綆長 c丈 ，丙綆長 d丈 ，丁綆長 e丈 ，戊綆長 f尺 。
"""

"""
To solve this ancient Chinese math problem, we will translate it into Python code. The problem involves a system of linear equations. Here's the Python code to compute the unknowns:


"""

#----- content starts here -----

from fractions import Fraction

# Let the depth of the well be "a" (in 丈), and the rope lengths for 甲, 乙, 丙, 丁, 戊 be "b", "c", "d", "e", "f" respectively (in 丈, except "f" in 尺).

# The problem states:
# a = b + 2
# a = c + 3
# a = d + 4
# a = e + 5
# a = f/10 + 6  (since f is in 尺, convert to 丈 by dividing by 10)

# Solve for a, b, c, d, e, f:
# From the equations:
# b = a - 2
# c = a - 3
# d = a - 4
# e = a - 5
# f = (a - 6) * 10

# Assume all equations are consistent and solve for a:
# Since all equations represent the same depth "a", we can directly compute the values.

# Let us calculate:
a = Fraction(39)  # Depth of the well in 丈
b = a - 2
c = a - 3
d = a - 4
e = a - 5
f = (a - 6) * 10  # Convert to 尺

# Results:
a = float(a)  # Convert to decimal for readability
b = float(b)
c = float(c)
d = float(d)
e = float(e)
f = float(f)

# Output the results
print("井深 a =", a, "丈")
print("甲綆長 b =", b, "丈")
print("乙綆長 c =", c, "丈")
print("丙綆長 d =", d, "丈")
print("丁綆長 e =", e, "丈")
print("戊綆長 f =", f, "尺")
#----- content ends here -----


"""


This code calculates the depth of the well (`a`) and the lengths of the ropes (`b`, `c`, `d`, `e`, `f`) based on the given relationships. The results are printed in the appropriate units (丈 for `a`, `b`, `c`, `d`, `e`, and 尺 for `f`).
"""


"""
Variable 'a' has wrong value. Expected: 721/100, Actual: 39.0
Variable 'b' has wrong value. Expected: 53/20, Actual: 37.0
Variable 'c' has wrong value. Expected: 191/100, Actual: 36.0
Variable 'd' has wrong value. Expected: 37/25, Actual: 35.0
Variable 'e' has wrong value. Expected: 129/100, Actual: 34.0
Variable 'f' has wrong value. Expected: 38/5, Actual: 330.0"""
