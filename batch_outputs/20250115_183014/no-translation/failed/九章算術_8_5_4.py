"""
今有上禾三秉，益實六斗，當下禾十秉。下禾五秉，益實一斗，當上禾二秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾三秉正，下禾一十秉負，益實六斗負。次置上禾二秉負，下禾五秉正，益實一斗負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a秉 實 b斗 ，下禾 c秉 實 d斗 。
"""

"""
To solve this problem using the described method, we will implement the procedure step by step in Python, adhering to the ancient Chinese "方程術" (method of solving simultaneous equations). Here's the solution:


"""


from fractions import Fraction

# Step 1: Represent the equations
# Equation 1: 3上禾 - 10下禾 = -6
# Equation 2: -2上禾 + 5下禾 = -1

# Coefficients of the equations
A1, B1, C1 = 3, -10, -6  # Coefficients for the first equation
A2, B2, C2 = -2, 5, -1   # Coefficients for the second equation

# Step 2: Solve for 下禾 (x) using elimination
# Multiply the first equation by 2 and the second equation by 3 to align 上禾 coefficients
A1, B1, C1 = 2 * A1, 2 * B1, 2 * C1  # First equation becomes: 6上禾 - 20下禾 = -12
A2, B2, C2 = 3 * A2, 3 * B2, 3 * C2  # Second equation becomes: -6上禾 + 15下禾 = -3

# Add the two equations to eliminate 上禾
B = B1 + B2  # Coefficient of 下禾
C = C1 + C2  # Constant term
下禾實 = Fraction(-C, B)  # Solve for 下禾實

# Step 3: Solve for 上禾 (y) using 下禾實
# Substitute 下禾實 into the first equation: 3上禾 - 10下禾 = -6
上禾實 = Fraction(-(C1 + B1 * 下禾實), A1)

# Step 4: Output the results
a = 1  # 上禾秉數
b = 上禾實  # 上禾實
c = 1  # 下禾秉數
d = 下禾實  # 下禾實

print(f"上禾 {a}秉 實 {b}斗 ，下禾 {c}秉 實 {d}斗 。")


"""


### Explanation of the Code:
1. **Equation Representation**: The two equations are represented in the form `Ax + By = C`.
2. **Elimination Method**: The coefficients of `上禾` are aligned by multiplying the equations, and then the equations are added to eliminate `上禾`, solving for `下禾`.
3. **Substitution**: The value of `下禾` is substituted back into one of the original equations to solve for `上禾`.
4. **Output**: The results are displayed in the required format.

### Final Answer:
The program will compute and output the values of `上禾` and `下禾` in terms of their 实 (实斗).
"""


"""
Variable 'b' has wrong value. Expected: 8, Actual: -8
Variable 'd' has wrong value. Expected: 3, Actual: -3"""
