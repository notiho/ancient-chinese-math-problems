"""
今有五羊、四犬、三雞、二兔，直錢一千四百九十六；四羊、二犬、六雞、三兔直錢一千一百七十五；三羊、一犬、七雞、五兔，直錢九百五十八；二羊、三犬、五雞、一兔，直錢八百六十一。問︰羊、犬、雞、兔價各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：羊價 a ，犬價 b ，雞價 c ，兔價 d 。
"""

"""
To solve this problem, we need to translate the ancient Chinese method of solving simultaneous linear equations (方程術) into Python code. The problem provides four equations with four unknowns (羊, 犬, 雞, 兔). Here's how we can implement the solution step by step:


"""


from fractions import Fraction

# Define the coefficients of the equations
# Equation 1: 5羊 + 4犬 + 3雞 + 2兔 = 1496
# Equation 2: 4羊 + 2犬 + 6雞 + 3兔 = 1175
# Equation 3: 3羊 + 1犬 + 7雞 + 5兔 = 958
# Equation 4: 2羊 + 3犬 + 5雞 + 1兔 = 861

# Coefficient matrix
coefficients = [
    [5, 4, 3, 2],
    [4, 2, 6, 3],
    [3, 1, 7, 5],
    [2, 3, 5, 1]
]

# Constants (right-hand side of the equations)
constants = [1496, 1175, 958, 861]

# Step 1: Forward elimination to create an upper triangular matrix
for i in range(4):
    # Normalize the current row
    divisor = coefficients[i][i]
    for j in range(i, 4):
        coefficients[i][j] = Fraction(coefficients[i][j], divisor)
    constants[i] = Fraction(constants[i], divisor)
    
    # Eliminate the current variable from the rows below
    for k in range(i + 1, 4):
        factor = coefficients[k][i]
        for j in range(i, 4):
            coefficients[k][j] -= factor * coefficients[i][j]
        constants[k] -= factor * constants[i]

# Step 2: Back substitution to solve for the variables
results = [0] * 4
for i in range(3, -1, -1):
    results[i] = constants[i]
    for j in range(i + 1, 4):
        results[i] -= coefficients[i][j] * results[j]

# Assign the results to the respective variables
a, b, c, d = results

# Output the results
a, b, c, d


"""


### Explanation of the Code:
1. **Matrix Representation**: The coefficients of the equations are stored in a 2D list (`coefficients`), and the constants are stored in a separate list (`constants`).

2. **Forward Elimination**: This step transforms the coefficient matrix into an upper triangular form by normalizing each row and eliminating the variable from the rows below.

3. **Back Substitution**: Once the matrix is in upper triangular form, the values of the variables are calculated starting from the last row and moving upwards.

4. **Fraction Handling**: The `Fraction` class is used to ensure that all calculations are exact and avoid floating-point errors.

### Output:
The variables `a`, `b`, `c`, and `d` represent the prices of 羊 (sheep), 犬 (dog), 雞 (chicken), and 兔 (rabbit), respectively.
"""


"""
"""
