"""
今有上禾五秉，損實一斗一升，當下禾七秉。上禾七秉，損實二斗五升，當下禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾五秉正，下禾七秉負，損實一斗一升正。次置上禾七秉正，下禾五秉負，損實二斗五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉 a升 ，下禾一秉 b升 。
"""

"""
To solve this problem using the described ancient Chinese method (方程術), we will translate the procedure into Python code step by step. The problem involves solving a system of linear equations using the described elimination method.

### Problem Setup:
1. **Equation 1**: 5上禾 - 7下禾 = 1斗1升 (11升)
2. **Equation 2**: 7上禾 - 5下禾 = 2斗5升 (25升)

We will solve for the amount of grain in one "上禾" (a) and one "下禾" (b).

---


"""

#----- content starts here -----

from fractions import Fraction

# Convert given values to "升" (1斗 = 10升)
eq1_constant = 1 * 10 + 1  # 1斗1升 = 11升
eq2_constant = 2 * 10 + 5  # 2斗5升 = 25升

# Coefficients of the equations
# Equation 1: 5上禾 - 7下禾 = 11升
# Equation 2: 7上禾 - 5下禾 = 25升
coefficients = [
    [5, -7, eq1_constant],  # [5, -7, 11]
    [7, -5, eq2_constant],  # [7, -5, 25]
]

# Step 1: Eliminate one variable (下禾) using the elimination method
# Multiply the first equation by 5 and the second equation by 7 to align 下禾 coefficients
row1 = [coefficients[0][0] * 5, coefficients[0][1] * 5, coefficients[0][2] * 5]  # [25, -35, 55]
row2 = [coefficients[1][0] * 7, coefficients[1][1] * 7, coefficients[1][2] * 7]  # [49, -35, 175]

# Subtract row1 from row2 to eliminate 下禾
eliminated_row = [
    row2[0] - row1[0],  # 上禾 coefficient
    row2[1] - row1[1],  # 下禾 coefficient (should be 0)
    row2[2] - row1[2],  # constant term
]  # [24, 0, 120]

# Step 2: Solve for 上禾 (a)
a = Fraction(eliminated_row[2], eliminated_row[0])  # a = 120 / 24 = 5升

# Step 3: Substitute a back into one of the original equations to solve for 下禾 (b)
# Using Equation 1: 5a - 7b = 11
b = Fraction(coefficients[0][0] * a - coefficients[0][2], -coefficients[0][1])  # b = (5*5 - 11) / -7 = 2升

# Final Results
print(f"上禾一秉 a = {a} 升")  # 5升
print(f"下禾一秉 b = {b} 升")  # 2升
#----- content ends here -----


"""


### Explanation of the Code:
1. **Equation Setup**: The problem is converted into two linear equations with coefficients for 上禾 and 下禾.
2. **Elimination Method**: One variable (下禾) is eliminated by aligning coefficients and subtracting equations.
3. **Back-Substitution**: The value of 上禾 is substituted back into one of the original equations to solve for 下禾.
4. **Results**: The values of 上禾 and 下禾 are expressed in 升.

### Final Answer:
- 上禾一秉 \( a = 5 \) 升
- 下禾一秉 \( b = 2 \) 升
"""


"""
"""
