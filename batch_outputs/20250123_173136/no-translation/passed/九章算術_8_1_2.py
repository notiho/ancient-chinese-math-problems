"""
今有上禾七秉，損實一斗，益之下禾二秉，而實一十斗。下禾八秉，益實一斗與上禾二秉，而實一十斗。問︰上、下禾實一秉各幾何？
術曰：如方程。損之曰益，益之曰損。損實一斗者，其實過一十斗也。益實一斗者，其實不滿一十斗也。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a斗 ，下禾一秉實 b斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical procedure into Python code step by step, following the "方程術" (method of simultaneous equations). Here's the solution:


"""


from fractions import Fraction

# Define the given conditions
# 上禾七秉，損實一斗，益之下禾二秉，而實一十斗
# 下禾八秉，益實一斗與上禾二秉，而實一十斗

# Let 上禾實 = x (per 秉), 下禾實 = y (per 秉)
# The equations based on the problem are:
# 7x - 1 + 2y = 10  (Equation 1)
# 8y + 1 + 2x = 10  (Equation 2)

# Simplify the equations:
# Equation 1: 7x + 2y = 11
# Equation 2: 2x + 8y = 9

# Solve the equations using the 方程術 (method of elimination)

# Step 1: Eliminate one variable
# Multiply Equation 1 by 4 to align coefficients of y
# 4 * (7x + 2y) = 4 * 11
# 28x + 8y = 44  (New Equation 1)

# Subtract Equation 2 from the new Equation 1:
# (28x + 8y) - (2x + 8y) = 44 - 9
# 26x = 35
x = Fraction(35, 26)  # Solve for x (上禾實 per 秉)

# Step 2: Substitute x into one of the original equations to solve for y
# Substitute x into Equation 1: 7x + 2y = 11
# 7 * (35/26) + 2y = 11
# (245/26) + 2y = 11
# 2y = 11 - (245/26)
# 2y = (286/26) - (245/26)
# 2y = 41/26
y = Fraction(41, 52)  # Solve for y (下禾實 per 秉)

# Final results
a = x  # 上禾一秉實
b = y  # 下禾一秉實

# Print results
print(f"上禾一秉實 a = {a}斗")
print(f"下禾一秉實 b = {b}斗")


"""


### Explanation of the Code:
1. **Define Variables**: We represent the unknowns (上禾實 and 下禾實) as `x` and `y`, respectively.
2. **Set Up Equations**: The problem gives two conditions, which are translated into two linear equations.
3. **Elimination Method**: The 方程術 (method of elimination) is used to solve the system of equations step by step.
4. **Fraction Representation**: The `Fraction` class is used to ensure precise calculations with fractions, as required by the problem.
5. **Results**: The values of `x` (上禾一秉實) and `y` (下禾一秉實) are computed and displayed.

### Final Answer:
- 上禾一秉實 \( a = \frac{35}{26} \) 斗
- 下禾一秉實 \( b = \frac{41}{52} \) 斗
"""


"""
"""
