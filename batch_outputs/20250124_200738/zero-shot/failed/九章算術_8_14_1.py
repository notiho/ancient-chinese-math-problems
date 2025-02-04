"""
今有甲禾二秉、乙禾三秉、丙禾四秉，重皆過於石。甲二重如乙一，乙三重如丙一，丙四重如甲一。問︰甲、乙、丙禾一秉各重幾何？
術曰：如方程，置重過於石之物為負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：甲禾一秉重 a石 ，乙禾一秉重 b石 ，丙禾一秉重 c石 。
"""

"""
To solve the problem, we will translate the ancient Chinese math problem into Python code. The problem involves three types of grain (甲, 乙, 丙) with weights that are related to each other. We will use the relationships provided to compute the weights of one秉 (unit) of each type of grain.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Relationships between the weights:
# 甲二重如乙一: 2a = b
# 乙三重如丙一: 3b = c
# 丙四重如甲一: 4c = a

# Solve for a, b, c:
# From 2a = b, we get b = 2a
# From 3b = c, we get c = 3b = 3(2a) = 6a
# From 4c = a, we get a = 4c = 4(6a) = 24a, which implies a = 1/24

a = Fraction(1, 24)  # Weight of 甲禾一秉 in 石
b = 2 * a            # Weight of 乙禾一秉 in 石
c = 6 * a            # Weight of 丙禾一秉 in 石

# Results:
a, b, c
#----- content ends here -----


"""


### Explanation:
1. The relationships between the weights are given as:
   - 甲二重如乙一: \( 2a = b \)
   - 乙三重如丙一: \( 3b = c \)
   - 丙四重如甲一: \( 4c = a \)

2. Substitute \( b = 2a \) into \( c = 3b \), giving \( c = 6a \).

3. Substitute \( c = 6a \) into \( 4c = a \), giving \( a = \frac{1}{24} \).

4. Using \( a = \frac{1}{24} \), compute \( b = 2a = \frac{2}{24} = \frac{1}{12} \) and \( c = 6a = \frac{6}{24} = \frac{1}{4} \).

### Final Answer:
- \( a = \frac{1}{24} \) 石 (weight of 甲禾一秉)
- \( b = \frac{1}{12} \) 石 (weight of 乙禾一秉)
- \( c = \frac{1}{4} \) 石 (weight of 丙禾一秉)
"""


"""
Variable 'a' has wrong value. Expected: 17/23, Actual: 1/24
Variable 'b' has wrong value. Expected: 11/23, Actual: 1/12
Variable 'c' has wrong value. Expected: 10/23, Actual: 1/4"""
