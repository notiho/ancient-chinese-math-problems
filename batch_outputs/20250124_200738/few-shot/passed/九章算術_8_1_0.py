"""
今有上禾七秉，損實一斗，益之下禾二秉，而實一十斗。下禾八秉，益實一斗與上禾二秉，而實一十斗。問︰上、下禾實一秉各幾何？
術曰：如方程。損之曰益，益之曰損。損實一斗者，其實過一十斗也。益實一斗者，其實不滿一十斗也。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a斗 ，下禾一秉實 b斗 。
"""

"""
This problem involves solving a system of linear equations to determine the yield per sheaf of upper and lower millet. The ancient Chinese method described is equivalent to solving simultaneous equations using elimination. Below is the Python implementation of the procedure:


"""

#----- content starts here -----

from fractions import Fraction

# Problem setup
# 上禾 (upper millet) = 7 sheaves, 下禾 (lower millet) = 8 sheaves
# Equation 1: 7 * 上禾 - 1 + 2 * 下禾 = 10
# Equation 2: 8 * 下禾 + 1 + 2 * 上禾 = 10

# Representing the equations in terms of coefficients:
# Equation 1: 7 * 上禾 + 2 * 下禾 = 11
# Equation 2: 2 * 上禾 + 8 * 下禾 = 9

# Coefficients for the equations
a1, b1, c1 = 7, 2, 11  # Coefficients for Equation 1
a2, b2, c2 = 2, 8, 9   # Coefficients for Equation 2

# Elimination process
# Multiply the first equation by 2 and the second equation by 7 to align coefficients of 上禾
mult1 = 2
mult2 = 7

a1, b1, c1 = a1 * mult1, b1 * mult1, c1 * mult1
a2, b2, c2 = a2 * mult2, b2 * mult2, c2 * mult2

# Subtract the second equation from the first to eliminate 上禾
b = b1 - b2
c = c1 - c2

# Solve for 下禾
下禾 = Fraction(c, b)

# Substitute 下禾 back into one of the original equations to solve for 上禾
上禾 = Fraction(c1 - b1 * 下禾, a1)

# Results
a = 上禾  # Yield per sheaf of upper millet
b = 下禾  # Yield per sheaf of lower millet

# Output the results
a, b
#----- content ends here -----


"""


### Explanation of the Code:
1. **Setup of Equations**: The problem is translated into two linear equations based on the given conditions.
2. **Elimination**: The coefficients of `上禾` are aligned by multiplying the equations by appropriate factors, and then one equation is subtracted from the other to eliminate `上禾`.
3. **Solve for 下禾**: The resulting equation is solved for `下禾`.
4. **Substitute Back**: The value of `下禾` is substituted back into one of the original equations to solve for `上禾`.
5. **Results**: The values of `上禾` and `下禾` are the yields per sheaf of upper and lower millet, respectively.

### Answer:
The yield per sheaf of upper millet is `a` dou, and the yield per sheaf of lower millet is `b` dou.
"""


"""
"""
