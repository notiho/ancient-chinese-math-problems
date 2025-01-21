"""
今有上禾七秉，損實一斗，益之下禾二秉，而實一十斗。下禾八秉，益實一斗與上禾二秉，而實一十斗。問︰上、下禾實一秉各幾何？
術曰：如方程。損之曰益，益之曰損。損實一斗者，其實過一十斗也。益實一斗者，其實不滿一十斗也。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a秉 實 b斗 ，下禾 c秉 實 d斗 。
"""

"""
This problem is a classic system of linear equations problem, where we solve for the yield (實) of one秉 of 上禾 and 下禾. Let's translate the procedure into Python code step by step.


"""


from fractions import Fraction

# Given data:
# 上禾七秉，損實一斗，益之下禾二秉，而實一十斗
# 下禾八秉，益實一斗與上禾二秉，而實一十斗

# Let 上禾實 (yield per 秉 of 上禾) = x
# Let 下禾實 (yield per 秉 of 下禾) = y

# Equation 1: 7x - 1 + 2y = 10
# Simplify: 7x + 2y = 11

# Equation 2: 8y + 1 + 2x = 10
# Simplify: 2x + 8y = 9

# Solve the system of equations using the procedure:

# Step 1: Define the coefficients of the equations
a1, b1, c1 = 7, 2, 11  # Coefficients for the first equation (7x + 2y = 11)
a2, b2, c2 = 2, 8, 9   # Coefficients for the second equation (2x + 8y = 9)

# Step 2: Eliminate one variable (e.g., x) by multiplying and subtracting
# Multiply the first equation by 2 and the second equation by 7 to align coefficients of x
a1, b1, c1 = 2 * a1, 2 * b1, 2 * c1  # First equation becomes: 14x + 4y = 22
a2, b2, c2 = 7 * a2, 7 * b2, 7 * c2  # Second equation becomes: 14x + 56y = 63

# Subtract the first equation from the second to eliminate x
b = b2 - b1  # Coefficient of y
c = c2 - c1  # Constant term
# Resulting equation: by = c
y = Fraction(c, b)  # Solve for y (下禾實)

# Step 3: Substitute y back into one of the original equations to solve for x
# Using the first equation: 7x + 2y = 11
x = Fraction(c1 - b1 * y, a1)  # Solve for x (上禾實)

# Results:
a = 7  # 上禾秉
b = x  # 上禾實
c = 8  # 下禾秉
d = y  # 下禾實

# Output the results
print(f"上禾 {a}秉 實 {b}斗 ，下禾 {c}秉 實 {d}斗 。")


"""


### Explanation of the Code:
1. The problem is translated into a system of linear equations:
   - \( 7x + 2y = 11 \)
   - \( 2x + 8y = 9 \)
2. The procedure involves eliminating one variable (e.g., \( x \)) by aligning coefficients and subtracting equations.
3. After solving for \( y \) (下禾實), substitute it back into one of the original equations to solve for \( x \) (上禾實).
4. The results are expressed in terms of fractions to maintain precision.

### Final Answer:
The Python code will compute the exact values of \( x \) and \( y \) (實 for 上禾 and 下禾).
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 7
Variable 'c' has wrong value. Expected: 1, Actual: 8"""
