"""
今有上禾三秉，益實六斗，當下禾十秉。下禾五秉，益實一斗，當上禾二秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾三秉正，下禾一十秉負，益實六斗負。次置上禾二秉負，下禾五秉正，益實一斗負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a秉 實 b斗 ，下禾 c秉 實 d斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical procedure into Python code step by step, following the described "方程術" (method of solving equations). The problem involves solving a system of linear equations to determine the amount of grain (實) per秉 for both 上禾 and 下禾.

### Problem Setup:
We are given two equations:
1. \( 3x - 10y = -6 \)
2. \( -2x + 5y = -1 \)

Where:
- \( x \) represents the實 (grain per秉) of上禾.
- \( y \) represents the實 (grain per秉) of下禾.

We will solve this system using the described method.

---


"""


from fractions import Fraction

# Step 1: Define the coefficients of the equations
# Equation 1: 3x - 10y = -6
a1, b1, c1 = 3, -10, -6

# Equation 2: -2x + 5y = -1
a2, b2, c2 = -2, 5, -1

# Step 2: Solve for下禾 (y) first
# Multiply the first equation by b2 (5) and the second equation by b1 (-10)
# This eliminates y when the equations are added together
mult1 = b2
mult2 = -b1

# Adjusted equations:
# (3 * 5)x + (-10 * 5)y = -6 * 5
# (-2 * -10)x + (5 * -10)y = -1 * -10
a1_new, b1_new, c1_new = a1 * mult1, b1 * mult1, c1 * mult1
a2_new, b2_new, c2_new = a2 * mult2, b2 * mult2, c2 * mult2

# Add the two equations to eliminate y
x_numerator = c1_new + c2_new
x_denominator = a1_new + a2_new
x = Fraction(x_numerator, x_denominator)

# Step 3: Solve for上禾 (x) using one of the original equations
# Substitute x into the first equation: 3x - 10y = -6
y_numerator = c1 - a1 * x
y_denominator = b1
y = Fraction(y_numerator, y_denominator)

# Step 4: Output the results
a = 1  # 上禾秉數
b = x  # 上禾實 (grain per秉)
c = 1  # 下禾秉數
d = y  # 下禾實 (grain per秉)

print(f"上禾 {a}秉 實 {b}斗 ，下禾 {c}秉 實 {d}斗 。")


"""


### Explanation:
1. **Elimination Method**: The procedure uses elimination to solve the system of equations. By multiplying the equations to align the coefficients of \( y \), we can eliminate \( y \) and solve for \( x \).
2. **Substitution**: Once \( x \) is found, it is substituted back into one of the original equations to solve for \( y \).
3. **Fraction Handling**: The `Fraction` class is used to ensure exact arithmetic, as the results may not be integers.

### Final Answer:
The values of \( a, b, c, d \) represent the秉數 and實 for both上禾 and下禾.
"""


"""
"""
