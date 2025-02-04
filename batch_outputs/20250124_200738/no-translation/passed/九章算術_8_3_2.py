"""
今有上禾五秉，損實一斗一升，當下禾七秉。上禾七秉，損實二斗五升，當下禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾五秉正，下禾七秉負，損實一斗一升正。次置上禾七秉正，下禾五秉負，損實二斗五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉 a升 ，下禾一秉 b升 。
"""

"""
To solve this problem using the described "方程術" (method of simultaneous equations), we translate the procedure into Python code step by step. The problem involves two equations with two unknowns, representing the yield of one秉 (bundle) of 上禾 (upper grain) and 下禾 (lower grain).

### Problem Setup:
1. **Equation 1**: 5 bundles of 上禾 and 7 bundles of 下禾 result in a loss of 1斗1升 (11升, since 1斗 = 10升).
2. **Equation 2**: 7 bundles of 上禾 and 5 bundles of 下禾 result in a loss of 2斗5升 (25升).

We aim to find the yield of one bundle of 上禾 (`a`) and one bundle of 下禾 (`b`).

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Define the equations:
# 5a - 7b = 11 (converted to 11升)
# 7a - 5b = 25 (converted to 25升)

# Coefficients of the equations
coeff1 = [5, -7, 11]  # 5a - 7b = 11
coeff2 = [7, -5, 25]  # 7a - 5b = 25

# Step 1: Eliminate one variable using the "正負術" (elimination method)
# Multiply the first equation by 7 (coeff2[0]) and the second equation by 5 (coeff1[0])
# This aligns the coefficients of 'a' for elimination.
eq1_scaled = [7 * x for x in coeff1]  # 35a - 49b = 77
eq2_scaled = [5 * x for x in coeff2]  # 35a - 25b = 125

# Subtract the scaled equations to eliminate 'a'
# (35a - 49b) - (35a - 25b) = 77 - 125
b_coeff = eq1_scaled[1] - eq2_scaled[1]  # Coefficient of 'b'
b_value = eq1_scaled[2] - eq2_scaled[2]  # Constant term
b = Fraction(b_value, b_coeff)  # Solve for b

# Step 2: Substitute 'b' back into one of the original equations to solve for 'a'
# Using the first equation: 5a - 7b = 11
a_coeff = coeff1[0]  # Coefficient of 'a'
a_value = coeff1[2] - coeff1[1] * b  # Constant term adjusted for 'b'
a = Fraction(a_value, a_coeff)  # Solve for a

# Convert results to 升
a_in_升 = a
b_in_升 = b

# Output the results
a = a_in_升
b = b_in_升
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Equation Setup**: The two equations are set up based on the problem statement.
2. **Elimination Method**: The coefficients of `a` are aligned by scaling the equations, and then one variable (`a`) is eliminated by subtraction.
3. **Substitution**: The value of `b` is substituted back into one of the original equations to solve for `a`.
4. **Fraction Handling**: The `Fraction` class ensures precise arithmetic for non-integer results.

---

### Final Answer:
- 上禾一秉 yields `a` 升.
- 下禾一秉 yields `b` 升.
"""


"""
"""
