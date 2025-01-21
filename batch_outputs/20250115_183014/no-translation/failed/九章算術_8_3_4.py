"""
今有上禾五秉，損實一斗一升，當下禾七秉。上禾七秉，損實二斗五升，當下禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾五秉正，下禾七秉負，損實一斗一升正。次置上禾七秉正，下禾五秉負，損實二斗五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a秉 b升 ，下禾 c秉 d升 。
"""

"""
To solve this problem, we will translate the ancient Chinese procedure into Python code. The problem involves solving a system of linear equations using the method described in the "方程術" (method of simultaneous equations). Here's the step-by-step implementation:


"""


from fractions import Fraction

# Problem setup
# First equation: 5上禾 - 7下禾 = 1斗1升
# Second equation: 7上禾 - 5下禾 = 2斗5升

# Convert all measurements to "升" (1斗 = 10升)
eq1_constant = 1 * 10 + 1  # 1斗1升 = 11升
eq2_constant = 2 * 10 + 5  # 2斗5升 = 25升

# Coefficients of the equations
# Equation 1: 5上禾 - 7下禾 = 11升
# Equation 2: 7上禾 - 5下禾 = 25升
coefficients = [
    [5, -7, eq1_constant],  # First equation
    [7, -5, eq2_constant],  # Second equation
]

# Solve using the method described in the 方程術
# Step 1: Eliminate one variable (下禾) by combining the equations
# Multiply the first equation by 5 and the second equation by 7 to align the 下禾 coefficients
multiplier1 = 5
multiplier2 = 7

new_eq1 = [coefficients[0][0] * multiplier1, coefficients[0][1] * multiplier1, coefficients[0][2] * multiplier1]
new_eq2 = [coefficients[1][0] * multiplier2, coefficients[1][1] * multiplier2, coefficients[1][2] * multiplier2]

# Add the two equations to eliminate 下禾
combined_eq = [
    new_eq1[0] + new_eq2[0],  # Coefficient of 上禾
    new_eq1[2] + new_eq2[2],  # Constant term
]

# Solve for 上禾 (a single variable equation)
上禾實 = Fraction(combined_eq[1], combined_eq[0])

# Step 2: Solve for 下禾 using one of the original equations
# Substitute 上禾實 into the first equation: 5上禾 - 7下禾 = 11升
下禾實 = Fraction(eq1_constant - coefficients[0][0] * 上禾實, -coefficients[0][1])

# Convert results back to 斗 and 升
a = 上禾實 // 10  # 斗
b = 上禾實 % 10   # 升

c = 下禾實 // 10  # 斗
d = 下禾實 % 10   # 升

# Results
print(f"上禾實: {a}斗 {b}升")
print(f"下禾實: {c}斗 {d}升")


"""


### Explanation of the Code:
1. **Setup**: The problem is converted into two linear equations with coefficients for 上禾 and 下禾, and constants converted to "升".
2. **Elimination**: The coefficients are aligned to eliminate 下禾 by multiplying the equations appropriately and adding them.
3. **Solve for 上禾**: The resulting single-variable equation is solved for 上禾.
4. **Substitute**: The value of 上禾 is substituted back into one of the original equations to solve for 下禾.
5. **Convert Units**: The results are converted back from "升" to "斗" and "升".

### Output:
The program will output the values of 上禾 and 下禾 in terms of "斗" and "升".
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 0
Variable 'b' has wrong value. Expected: 5, Actual: 115/37
Variable 'c' has wrong value. Expected: 1, Actual: -1
Variable 'd' has wrong value. Expected: 2, Actual: 346/37"""
