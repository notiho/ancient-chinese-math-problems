"""
今有上禾七秉，損實一斗，益之下禾二秉，而實一十斗。下禾八秉，益實一斗與上禾二秉，而實一十斗。問︰上、下禾實一秉各幾何？
術曰：如方程。損之曰益，益之曰損。損實一斗者，其實過一十斗也。益實一斗者，其實不滿一十斗也。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a秉 實 b斗 ，下禾 c秉 實 d斗 。
"""

"""
This problem involves solving a system of equations to determine the yield of one sheaf of upper and lower millet. The procedure describes a method similar to Gaussian elimination for solving the equations. Below is the Python implementation of the procedure:


"""


from fractions import Fraction

# 上禾七秉，損實一斗，益之下禾二秉，而實一十斗
# 下禾八秉，益實一斗與上禾二秉，而實一十斗

# Define the coefficients of the equations
# Let x = yield of one sheaf of upper millet (上禾)
# Let y = yield of one sheaf of lower millet (下禾)

# Equation 1: 7x - 1 + 2y = 10
# Simplify: 7x + 2y = 11
eq1_coeffs = [7, 2]  # Coefficients of x and y
eq1_const = 11       # Constant term

# Equation 2: 2x + 8y + 1 = 10
# Simplify: 2x + 8y = 9
eq2_coeffs = [2, 8]  # Coefficients of x and y
eq2_const = 9        # Constant term

# Step 1: Eliminate x from the second equation
# Multiply eq1 by 2 and eq2 by 7 to align the coefficients of x
eq1_scaled = [2 * c for c in eq1_coeffs]  # [14, 4]
eq1_const_scaled = 2 * eq1_const          # 22

eq2_scaled = [7 * c for c in eq2_coeffs]  # [14, 56]
eq2_const_scaled = 7 * eq2_const          # 63

# Subtract eq1_scaled from eq2_scaled to eliminate x
# (14x + 56y = 63) - (14x + 4y = 22)
y_coeff = eq2_scaled[1] - eq1_scaled[1]   # 56 - 4 = 52
y_const = eq2_const_scaled - eq1_const_scaled  # 63 - 22 = 41

# Solve for y
y = Fraction(y_const, y_coeff)  # y = 41 / 52

# Step 2: Solve for x using eq1
# Substitute y into eq1: 7x + 2y = 11
x_coeff = eq1_coeffs[0]  # 7
x_const = eq1_const - eq1_coeffs[1] * y  # 11 - 2 * (41 / 52)

x = Fraction(x_const, x_coeff)  # x = (11 - 82/52) / 7

# Convert x and y to simplified fractions
x = x.limit_denominator()
y = y.limit_denominator()

# Results
a = 7  # 上禾秉數
b = x  # 上禾實
c = 8  # 下禾秉數
d = y  # 下禾實

# Output the results
print(f"上禾 {a}秉 實 {b}斗")
print(f"下禾 {c}秉 實 {d}斗")


"""


### Explanation:
1. **Equations Setup**:
   - The problem gives two equations based on the yields of upper and lower millet sheaves.
   - These equations are simplified into a standard linear form.

2. **Elimination**:
   - The coefficients of `x` are aligned by scaling the equations.
   - Subtraction eliminates `x`, leaving an equation for `y`.

3. **Back Substitution**:
   - The value of `y` is substituted back into one of the original equations to solve for `x`.

4. **Results**:
   - The yields of one sheaf of upper millet (`x`) and lower millet (`y`) are calculated as fractions.

### Final Answer:
- 上禾 7秉 實 `b`斗
- 下禾 8秉 實 `d`斗
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 7
Variable 'c' has wrong value. Expected: 1, Actual: 8"""
