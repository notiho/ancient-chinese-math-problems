"""
今有甲乙二人持錢不知其數。甲得乙半而錢五十，乙得甲太半而亦錢五十。問︰甲、乙持錢各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：甲持 a錢 ，乙持 b錢 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical procedure into Python code step by step. The problem involves solving a system of equations using a method similar to Gaussian elimination, as described in the "方程術."

The equations derived from the problem are:
1. \( x + \frac{y}{2} = 50 \) (where \( x \) is the amount of money held by 甲, and \( y \) is the amount of money held by 乙)
2. \( y + \frac{3x}{2} = 50 \)

We will solve this system using the described procedure.


"""


from fractions import Fraction

# Step 1: Represent the equations in matrix form
# Equation 1: x + y/2 = 50
# Equation 2: y + 3x/2 = 50
# Matrix form:
# [1, 1/2, 50]
# [3/2, 1, 50]

# Initialize the matrix
matrix = [
    [Fraction(1), Fraction(1, 2), Fraction(50)],  # First equation
    [Fraction(3, 2), Fraction(1), Fraction(50)]   # Second equation
]

# Step 2: Eliminate the first variable from the second equation
# Multiply the first row by 3/2 (to match the coefficient of x in the second row)
factor = matrix[1][0] / matrix[0][0]
for i in range(len(matrix[0])):
    matrix[1][i] -= factor * matrix[0][i]

# Step 3: Solve for y (second variable)
# The second row now represents: (1/4)y = 25
y = matrix[1][2] / matrix[1][1]

# Step 4: Back-substitute to solve for x (first variable)
# Substitute y into the first equation: x + y/2 = 50
x = (matrix[0][2] - (matrix[0][1] * y)) / matrix[0][0]

# Results
a = x  # 甲持錢
b = y  # 乙持錢

# Output the results
a, b


"""


### Explanation of the Code:
1. **Matrix Representation**: The equations are represented in augmented matrix form, where the last column represents the constants on the right-hand side of the equations.
2. **Elimination**: The first variable (\( x \)) is eliminated from the second equation by scaling and subtracting rows.
3. **Back-substitution**: After elimination, the second variable (\( y \)) is solved directly, and then the first variable (\( x \)) is solved using back-substitution.
4. **Fractions**: The `Fraction` class is used to ensure exact arithmetic, as required by the problem.

### Final Answer:
The values of \( a \) (money held by 甲) and \( b \) (money held by 乙) are computed and returned.
"""


"""
Variable 'a' has wrong value. Expected: 75/2, Actual: 100
Variable 'b' has wrong value. Expected: 25, Actual: -100"""
