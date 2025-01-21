"""
今有上禾三秉，益實六斗，當下禾十秉。下禾五秉，益實一斗，當上禾二秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾三秉正，下禾一十秉負，益實六斗負。次置上禾二秉負，下禾五秉正，益實一斗負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a秉 實 b斗 ，下禾 c秉 實 d斗 。
"""

"""
This problem involves solving a system of equations using ancient Chinese methods, which is essentially equivalent to solving simultaneous linear equations. Let's break it down step by step and implement the solution in Python.

### Problem Description:
We are given:
1. 3 bundles of upper millet (上禾), when added to 6 dou of grain, are equivalent to 10 bundles of lower millet (下禾).
2. 5 bundles of lower millet, when added to 1 dou of grain, are equivalent to 2 bundles of upper millet.

We need to find the amount of grain (in dou) per bundle for both upper millet (上禾) and lower millet (下禾).

### Procedure:
The ancient method described is essentially Gaussian elimination for solving linear equations. Let's translate it into Python.


"""


from fractions import Fraction

# Given equations:
# 1. 3上禾 - 10下禾 = -6 (converted to standard form)
# 2. -2上禾 + 5下禾 = -1 (converted to standard form)

# Coefficients of the equations
# Equation 1: 3上禾 - 10下禾 = -6
a1, b1, c1 = 3, -10, -6

# Equation 2: -2上禾 + 5下禾 = -1
a2, b2, c2 = -2, 5, -1

# Step 1: Eliminate one variable (下禾) by multiplying equations and adding them
# Multiply the first equation by 5 and the second equation by 10 to align 下禾 coefficients
mult1, mult2 = 5, 10
a1, b1, c1 = a1 * mult1, b1 * mult1, c1 * mult1
a2, b2, c2 = a2 * mult2, b2 * mult2, c2 * mult2

# Add the equations to eliminate 下禾
a3 = a1 + a2  # Coefficient of 上禾
b3 = b1 + b2  # Coefficient of 下禾 (should be 0)
c3 = c1 + c2  # Constant term

# Now we have a single equation for 上禾:
# a3上禾 = c3
上禾實 = Fraction(c3, a3)

# Step 2: Substitute 上禾實 back into one of the original equations to solve for 下禾實
# Using the first equation: 3上禾 - 10下禾 = -6
下禾實 = Fraction((c1 - a1 * 上禾實), b1)

# Results
a = 1  # Each 上禾 represents 1 bundle
b = 上禾實  # Grain per bundle of 上禾
c = 1  # Each 下禾 represents 1 bundle
d = 下禾實  # Grain per bundle of 下禾

print(f"上禾 {a}秉 實 {b}斗 ，下禾 {c}秉 實 {d}斗 。")


"""


### Explanation of the Code:
1. **Equation Setup**: The two equations are set up in standard form: `ax + by = c`.
2. **Elimination**: We eliminate one variable (下禾) by aligning coefficients and adding the equations.
3. **Back Substitution**: Once 上禾實 is found, it is substituted back into one of the original equations to find 下禾實.
4. **Fraction Handling**: The `Fraction` class is used to ensure exact arithmetic with rational numbers.

### Final Answer:
The output will give the amount of grain (in dou) per bundle for both upper millet (上禾) and lower millet (下禾).
"""


"""
"""
