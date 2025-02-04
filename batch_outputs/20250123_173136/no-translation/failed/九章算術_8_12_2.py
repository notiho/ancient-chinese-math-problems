"""
今有五家共井，甲二綆不足，如乙一綆；乙三綆不足，如丙一綆；丙四綆不足，如丁一綆；丁五綆不足，如戊一綆；戊六綆不足，如甲一綆。如各得所不足一綆，皆逮。問︰井深、綆長各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：井深 a丈 。甲綆長 b丈 ，乙綆長 c丈 ，丙綆長 d丈 ，丁綆長 e丈 ，戊綆長 f尺 。
"""

"""
To solve this problem, we need to use the ancient Chinese method of solving simultaneous equations, as described in the "方程術" (method of solving systems of equations). The problem involves five families sharing a well, with specific relationships between their rope lengths and the depth of the well. Here's the Python implementation:


"""


from fractions import Fraction

# Define the variables:
# Let the depth of the well be `井深 = a`
# Let the rope lengths for each family be:
# 甲綆長 = b, 乙綆長 = c, 丙綆長 = d, 丁綆長 = e, 戊綆長 = f

# The relationships are:
# b = a - 2
# c = a - 3
# d = a - 4
# e = a - 5
# f = a - 6

# Additionally, the total rope length for all families is such that
# b + c + d + e + f = a + 1 (each family gets one additional rope length to meet their needs)

# Step 1: Express the total rope length in terms of `a`
# b + c + d + e + f = (a - 2) + (a - 3) + (a - 4) + (a - 5) + (a - 6)
total_rope_length = (a - 2) + (a - 3) + (a - 4) + (a - 5) + (a - 6)

# Step 2: Set up the equation for total rope length
# total_rope_length = a + 1
# Simplify:
# 5a - 20 = a + 1
# 4a = 21
a = Fraction(21, 4)  # Depth of the well in 丈

# Step 3: Calculate the rope lengths for each family
b = a - 2  # Rope length for 甲
c = a - 3  # Rope length for 乙
d = a - 4  # Rope length for 丙
e = a - 5  # Rope length for 丁
f = a - 6  # Rope length for 戊

# Convert the results to 丈 and 尺 (1 丈 = 10 尺)
井深_丈 = a
甲綆長_丈 = b
乙綆長_丈 = c
丙綆長_丈 = d
丁綆長_丈 = e
戊綆長_丈 = f

# Convert 戊綆長 to 丈 and 尺
戊綆長_丈 = int(f)
戊綆長_尺 = (f - 戊綆長_丈) * 10

# Output the results
print(f"井深 {井深_丈} 丈")
print(f"甲綆長 {甲綆長_丈} 丈")
print(f"乙綆長 {乙綆長_丈} 丈")
print(f"丙綆長 {丙綆長_丈} 丈")
print(f"丁綆長 {丁綆長_丈} 丈")
print(f"戊綆長 {戊綆長_丈} 丈 {戊綆長_尺} 尺")


"""


### Explanation:
1. The relationships between the rope lengths and the well depth are expressed as equations.
2. The total rope length equation is derived from the problem statement.
3. The equations are solved using basic algebra to find the depth of the well (`a`) and the rope lengths for each family.
4. The results are converted into the appropriate units (丈 and 尺) for the final output.

### Final Answer:
- 井深 \( a \) 丈
- 甲綆長 \( b \) 丈
- 乙綆長 \( c \) 丈
- 丙綆長 \( d \) 丈
- 丁綆長 \( e \) 丈
- 戊綆長 \( f \) 尺
"""


"""
Code error: name 'a' is not defined"""
