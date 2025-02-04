"""
今有上禾七秉，損實一斗，益之下禾二秉，而實一十斗。下禾八秉，益實一斗與上禾二秉，而實一十斗。問︰上、下禾實一秉各幾何？
術曰：如方程。損之曰益，益之曰損。損實一斗者，其實過一十斗也。益實一斗者，其實不滿一十斗也。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a斗 ，下禾一秉實 b斗 。
"""

"""
To solve this problem, we will follow the procedure described in the "方程術" (method of equations). We'll translate the steps into Python code, ensuring that each part of the procedure is implemented correctly.


"""

#----- content starts here -----

from fractions import Fraction

# Define the given equations based on the problem:
# Equation 1: 7a - 1 + 2b = 10
# Equation 2: 8b + 1 + 2a = 10

# Step 1: Rewrite the equations to standard form:
# 7a + 2b = 11  (from Equation 1)
# 2a + 8b = 9   (from Equation 2)

# Step 2: Solve the system of equations using elimination or substitution.

# Multiply the first equation by 8 and the second equation by 2 to align coefficients of 'a':
# 56a + 16b = 88  (from 8 * (7a + 2b = 11))
# 4a + 16b = 18   (from 2 * (2a + 8b = 9))

# Subtract the second equation from the first to eliminate 'b':
# (56a + 16b) - (4a + 16b) = 88 - 18
# 52a = 70
a = Fraction(70, 52)  # Simplify the fraction
a = Fraction(35, 26)

# Substitute 'a' back into one of the original equations to solve for 'b':
# Using 7a + 2b = 11:
# 7 * (35/26) + 2b = 11
# 245/26 + 2b = 11
# 2b = 11 - 245/26
# 2b = (286/26) - (245/26)
# 2b = 41/26
b = Fraction(41, 26) / 2
b = Fraction(41, 52)

# Final results:
# a is the amount of grain per秉 for the upper crop (上禾)
# b is the amount of grain per秉 for the lower crop (下禾)
print(f"上禾一秉實 a = {a}斗")
print(f"下禾一秉實 b = {b}斗")
#----- content ends here -----


"""


### Explanation of Results:
- `a = 35/26`斗: This is the amount of grain per秉 for the upper crop (上禾).
- `b = 41/52`斗: This is the amount of grain per秉 for the lower crop (下禾).
"""


"""
"""
