"""
今有上禾五秉，損實一斗一升，當下禾七秉。上禾七秉，損實二斗五升，當下禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾五秉正，下禾七秉負，損實一斗一升正。次置上禾七秉正，下禾五秉負，損實二斗五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉 a升 ，下禾一秉 b升 。
"""

"""
To solve this problem using the described "方程術" (method of simultaneous equations), we will translate the procedure into Python code step by step. The problem involves solving a system of linear equations to find the value of one unit of "上禾" (upper grain) and "下禾" (lower grain).

### Problem Setup:
- Equation 1: \( 5x - 7y = 1斗1升 = 11升 \)
- Equation 2: \( 7x - 5y = 2斗5升 = 25升 \)

Here, \( x \) represents the value of one unit of "上禾" (upper grain) in 升, and \( y \) represents the value of one unit of "下禾" (lower grain) in 升.

---

### Python Code:


"""


from fractions import Fraction

# Coefficients from the equations
# Equation 1: 5x - 7y = 11
# Equation 2: 7x - 5y = 25
coefficients = [
    [5, -7, 11],  # [5x, -7y, 11]
    [7, -5, 25]   # [7x, -5y, 25]
]

# Step 1: Eliminate one variable (y) using the "正負術" (elimination method)
# Multiply the first equation by 7 (coefficient of x in the second equation)
# Multiply the second equation by 5 (coefficient of x in the first equation)
eq1_scaled = [7 * term for term in coefficients[0]]  # [35x, -49y, 77]
eq2_scaled = [5 * term for term in coefficients[1]]  # [35x, -25y, 125]

# Subtract the second scaled equation from the first to eliminate x
# (35x - 35x) + (-49y - (-25y)) = 77 - 125
y_coefficient = eq1_scaled[1] - eq2_scaled[1]  # -49 - (-25) = -24
y_constant = eq1_scaled[2] - eq2_scaled[2]    # 77 - 125 = -48

# Solve for y (value of one unit of 下禾)
y = Fraction(y_constant, y_coefficient)  # -48 / -24 = 2

# Step 2: Substitute y back into one of the original equations to solve for x
# Using the first equation: 5x - 7y = 11
x_coefficient = coefficients[0][0]  # 5
y_term = coefficients[0][1] * y     # -7 * 2 = -14
x_constant = coefficients[0][2]     # 11

# Solve for x
x = Fraction(x_constant - y_term, x_coefficient)  # (11 - (-14)) / 5 = 25 / 5 = 5

# Results
a = x  # Value of one unit of 上禾 in 升
b = y  # Value of one unit of 下禾 in 升

# Output the results
a, b


"""


---

### Explanation of the Code:
1. **Setup the equations**: The coefficients of the equations are stored in a list for easy manipulation.
2. **Elimination method**: The equations are scaled to eliminate one variable (in this case, \( x \)).
3. **Solve for \( y \)**: After eliminating \( x \), the value of \( y \) (one unit of 下禾) is calculated.
4. **Substitute back**: The value of \( y \) is substituted into one of the original equations to solve for \( x \) (one unit of 上禾).
5. **Output the results**: The values of \( x \) and \( y \) are the answers.

---

### Final Answer:
- \( a = 5 \) 升 (one unit of 上禾)
- \( b = 2 \) 升 (one unit of 下禾)
"""


"""
"""
