"""
今有令一人、吏五人、從者一十人，食雞一十；令一十人、吏一人、從者五人，食雞八；令五人、吏一十人、從者一人，食雞六。問︰令、吏、從者食雞各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：令一人食 a(=45/122)雞 ，吏一人食 b(=41/122)雞 ，從者一人食 c(=97/122)雞 。
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method of elimination, which is similar to Gaussian elimination. Here's how we translate the problem into Python code:

### Problem Setup
We are given three equations based on the consumption of chickens by different groups:
1. A group of 1 Ling (令), 5 Li (吏), and 10 Congzhe (從者) eats 10 chickens.
2. A group of 10 Ling, 1 Li, and 5 Congzhe eats 8 chickens.
3. A group of 5 Ling, 10 Li, and 1 Congzhe eats 6 chickens.

We need to find how many chickens are eaten by one Ling, one Li, and one Congzhe.

### Procedure
The ancient Chinese method of elimination is described in the "方程術" (method of solving equations). It involves systematically eliminating variables to solve for the unknowns.

### Python Code


"""

#----- content starts here -----

from fractions import Fraction

# Coefficients of the equations
# Equation 1: 1令 + 5吏 + 10從者 = 10
# Equation 2: 10令 + 1吏 + 5從者 = 8
# Equation 3: 5令 + 10吏 + 1從者 = 6

# Representing the equations as a matrix
matrix = [
    [1, 5, 10, 10],  # Coefficients and constant term for Equation 1
    [10, 1, 5, 8],   # Coefficients and constant term for Equation 2
    [5, 10, 1, 6]    # Coefficients and constant term for Equation 3
]

# Step 1: Normalize the first row
factor = matrix[0][0]
matrix[0] = [Fraction(x, factor) for x in matrix[0]]

# Step 2: Eliminate the first variable from the second and third rows
for i in range(1, 3):
    factor = matrix[i][0]
    matrix[i] = [matrix[i][j] - factor * matrix[0][j] for j in range(4)]

# Step 3: Normalize the second row
factor = matrix[1][1]
matrix[1] = [Fraction(x, factor) for x in matrix[1]]

# Step 4: Eliminate the second variable from the third row
factor = matrix[2][1]
matrix[2] = [matrix[2][j] - factor * matrix[1][j] for j in range(4)]

# Step 5: Normalize the third row
factor = matrix[2][2]
matrix[2] = [Fraction(x, factor) for x in matrix[2]]

# Step 6: Back substitution to solve for the variables
c = matrix[2][3]  # Value of 從者 (Congzhe)
b = matrix[1][3] - matrix[1][2] * c  # Value of 吏 (Li)
a = matrix[0][3] - matrix[0][2] * c - matrix[0][1] * b  # Value of 令 (Ling)

# Results
a = Fraction(a)  # 45/122
b = Fraction(b)  # 41/122
c = Fraction(c)  # 97/122

# Output the results
a, b, c
#----- content ends here -----


"""


### Explanation of the Code
1. **Matrix Representation**: The equations are represented as a matrix where each row corresponds to an equation, and the last column contains the constant terms.
2. **Normalization**: Each row is normalized by dividing by the leading coefficient to simplify calculations.
3. **Elimination**: Variables are systematically eliminated from subsequent rows by subtracting a multiple of the normalized row.
4. **Back Substitution**: After the matrix is in row-echelon form, the variables are solved starting from the last row and substituting back into previous rows.

### Answer
- One Ling (令) eats \( a = \frac{45}{122} \) chickens.
- One Li (吏) eats \( b = \frac{41}{122} \) chickens.
- One Congzhe (從者) eats \( c = \frac{97}{122} \) chickens.
"""


"""
"""
