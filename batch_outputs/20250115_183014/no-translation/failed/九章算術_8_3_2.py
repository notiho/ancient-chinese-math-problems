"""
今有上禾五秉，損實一斗一升，當下禾七秉。上禾七秉，損實二斗五升，當下禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾五秉正，下禾七秉負，損實一斗一升正。次置上禾七秉正，下禾五秉負，損實二斗五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a秉 b升 ，下禾 c秉 d升 。
"""

"""
To solve this problem using the described "方程術" (method of simultaneous equations), we will translate the procedure into Python code step by step. The problem involves solving a system of linear equations to determine the yield of one秉 (bundle) of 上禾 (upper crop) and 下禾 (lower crop).

### Problem setup:
We are given two equations:
1. \( 5x - 7y = 1斗1升 \) (where \( x \) is the yield of 上禾 per秉 and \( y \) is the yield of 下禾 per秉).
2. \( 7x - 5y = 2斗5升 \).

We need to solve for \( x \) and \( y \).

---

### Python Code:


"""


from fractions import Fraction

# Convert mixed units (斗升) into a single unit (升)
def convert_to_升(斗, 升):
    return 10 * 斗 + 升

# Convert back from 升 to 斗升
def convert_to_斗升(升):
    斗 = 升 // 10
    升 = 升 % 10
    return 斗, 升

# Problem setup
# Equation 1: 5x - 7y = 1斗1升
eq1_coeff_x = 5
eq1_coeff_y = -7
eq1_rhs = convert_to_升(1, 1)  # Convert 1斗1升 to 升

# Equation 2: 7x - 5y = 2斗5升
eq2_coeff_x = 7
eq2_coeff_y = -5
eq2_rhs = convert_to_升(2, 5)  # Convert 2斗5升 to 升

# Solve using elimination (正負術)
# Multiply equations to align coefficients for elimination
multiplier_eq1 = eq2_coeff_x
multiplier_eq2 = eq1_coeff_x

# Eliminate x by combining the equations
new_eq1_coeff_y = multiplier_eq1 * eq1_coeff_y
new_eq2_coeff_y = multiplier_eq2 * eq2_coeff_y
new_rhs = multiplier_eq2 * eq2_rhs - multiplier_eq1 * eq1_rhs

# Solve for y (下禾 yield per秉)
y = Fraction(new_rhs, new_eq1_coeff_y - new_eq2_coeff_y)

# Substitute y back into one of the original equations to solve for x (上禾 yield per秉)
x = Fraction(eq1_rhs - eq1_coeff_y * y, eq1_coeff_x)

# Convert results back to 斗升
a_斗, a_升 = convert_to_斗升(x)
c_斗, c_升 = convert_to_斗升(y)

# Output results
a, b = a_斗, a_升  # 上禾 yield per秉 in 斗升
c, d = c_斗, c_升  # 下禾 yield per秉 in 斗升

# Results
print(f"上禾: {a}斗 {b}升")
print(f"下禾: {c}斗 {d}升")


"""


---

### Explanation of the Code:
1. **Unit Conversion**: The problem uses two units (斗 and 升). We first convert all values into a single unit (升) for calculation and then convert back to 斗升 for the final answer.
2. **Elimination Method**: We use the elimination method (正負術) to solve the system of linear equations. This involves aligning coefficients and subtracting equations to eliminate one variable.
3. **Fraction Handling**: The `Fraction` class is used to ensure precise arithmetic with rational numbers.
4. **Final Conversion**: After solving for \( x \) and \( y \), the results are converted back to the original units (斗升).

---

### Final Answer:
The code will output the yield of 上禾 and 下禾 per秉 in the format \( a斗b升 \) and \( c斗d升 \), respectively.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: -1
Variable 'b' has wrong value. Expected: 5, Actual: 47/5
Variable 'c' has wrong value. Expected: 1, Actual: -1
Variable 'd' has wrong value. Expected: 2, Actual: 8"""
