"""
今有上禾五秉，損實一斗一升，當下禾七秉。上禾七秉，損實二斗五升，當下禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾五秉正，下禾七秉負，損實一斗一升正。次置上禾七秉正，下禾五秉負，損實二斗五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a秉 b升 ，下禾 c秉 d升 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical procedure into Python code step by step. The problem involves solving a system of linear equations using the described method, which is essentially Gaussian elimination. Here's the implementation:


"""


from fractions import Fraction

# Define the equations based on the problem:
# Equation 1: 5 * 上禾 - 7 * 下禾 = 1斗1升 (11升, since 1斗 = 10升)
# Equation 2: 7 * 上禾 - 5 * 下禾 = 2斗5升 (25升, since 1斗 = 10升)

# Convert the constants to "升" for uniformity
eq1_constant = 10 + 1  # 1斗1升 = 11升
eq2_constant = 20 + 5  # 2斗5升 = 25升

# Coefficients of the equations
# Equation 1: 5 * 上禾 - 7 * 下禾 = 11
# Equation 2: 7 * 上禾 - 5 * 下禾 = 25
matrix = [
    [5, -7, eq1_constant],  # Coefficients of equation 1
    [7, -5, eq2_constant]   # Coefficients of equation 2
]

# Perform Gaussian elimination
# Step 1: Normalize the first row
factor = matrix[0][0]
matrix[0] = [Fraction(x, factor) for x in matrix[0]]

# Step 2: Eliminate the first variable from the second row
factor = matrix[1][0]
matrix[1] = [matrix[1][i] - factor * matrix[0][i] for i in range(3)]

# Step 3: Solve for 下禾 (second variable)
下禾 = Fraction(matrix[1][2], matrix[1][1])

# Step 4: Back-substitute to solve for 上禾 (first variable)
上禾 = Fraction(matrix[0][2] - matrix[0][1] * 下禾, matrix[0][0])

# Convert the results to "斗" and "升"
a = 上禾 // 10  # Number of "斗" for 上禾
b = 上禾 % 10   # Remaining "升" for 上禾
c = 下禾 // 10  # Number of "斗" for 下禾
d = 下禾 % 10   # Remaining "升" for 下禾

# Output the results
a, b, c, d


"""


### Explanation of the Code:
1. **Equation Setup**: The problem is translated into two linear equations based on the given conditions. The constants are converted to "升" for uniformity.
2. **Gaussian Elimination**: The method described in the problem is essentially Gaussian elimination. We normalize the first row, eliminate the first variable from the second row, and then solve for the variables.
3. **Conversion to Units**: The results are converted back to "斗" and "升" for the final answer.

### Final Answer:
- 上禾: `a斗 b升`
- 下禾: `c斗 d升`
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 0
Variable 'c' has wrong value. Expected: 1, Actual: 0"""
