"""
今有令一人、吏五人、從者一十人，食雞一十；令一十人、吏一人、從者五人，食雞八；令五人、吏一十人、從者一人，食雞六。問︰令、吏、從者食雞各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：令一人食 a(=45/122)雞 ，吏一人食 b(=41/122)雞 ，從者一人食 c(=97/122)雞 。
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method of elimination, similar to Gaussian elimination. The problem describes three equations based on the consumption of chickens by different groups of people (officials, clerks, and attendants). Let's translate this into Python code step by step.

### Problem Setup
We have three equations:
1. \( x + 5y + 10z = 10 \)  (1 official, 5 clerks, 10 attendants eat 10 chickens)
2. \( 10x + y + 5z = 8 \)   (10 officials, 1 clerk, 5 attendants eat 8 chickens)
3. \( 5x + 10y + z = 6 \)   (5 officials, 10 clerks, 1 attendant eat 6 chickens)

Where:
- \( x \) is the number of chickens eaten by one official,
- \( y \) is the number of chickens eaten by one clerk,
- \( z \) is the number of chickens eaten by one attendant.

We will solve this system using the elimination method described in the procedure.

---

### Python Code Implementation


"""

#----- content starts here -----

from fractions import Fraction

# Coefficients of the equations
# Equation 1: x + 5y + 10z = 10
# Equation 2: 10x + y + 5z = 8
# Equation 3: 5x + 10y + z = 6

# Initial matrix representation of the system
# Each row represents [x-coefficient, y-coefficient, z-coefficient, constant]
matrix = [
    [1, 5, 10, 10],  # Row 1
    [10, 1, 5, 8],   # Row 2
    [5, 10, 1, 6]    # Row 3
]

# Step 1: Normalize the first row (make the leading coefficient of x in the first row 1)
factor = matrix[0][0]
matrix[0] = [Fraction(value, factor) for value in matrix[0]]

# Step 2: Eliminate x from the second and third rows
for i in range(1, 3):  # Rows 2 and 3
    factor = matrix[i][0]  # Coefficient of x in the current row
    matrix[i] = [matrix[i][j] - factor * matrix[0][j] for j in range(4)]

# Step 3: Normalize the second row (make the leading coefficient of y in the second row 1)
factor = matrix[1][1]
matrix[1] = [Fraction(value, factor) for value in matrix[1]]

# Step 4: Eliminate y from the third row
factor = matrix[2][1]  # Coefficient of y in the third row
matrix[2] = [matrix[2][j] - factor * matrix[1][j] for j in range(4)]

# Step 5: Normalize the third row (make the leading coefficient of z in the third row 1)
factor = matrix[2][2]
matrix[2] = [Fraction(value, factor) for value in matrix[2]]

# Step 6: Back-substitution to solve for x, y, z
z = matrix[2][3]  # The constant in the third row
y = matrix[1][3] - matrix[1][2] * z  # Solve for y using the second row
x = matrix[0][3] - matrix[0][1] * y - matrix[0][2] * z  # Solve for x using the first row

# Results
a = x  # Number of chickens eaten by one official
b = y  # Number of chickens eaten by one clerk
c = z  # Number of chickens eaten by one attendant

# Output the results
a, b, c  # a = 45/122, b = 41/122, c = 97/122
#----- content ends here -----


"""


---

### Explanation of the Code
1. **Matrix Representation**: The system of equations is represented as a matrix where each row corresponds to an equation, and the last column represents the constants on the right-hand side of the equations.
2. **Normalization**: Each row is normalized to make the leading coefficient (pivot) 1.
3. **Elimination**: Using the normalized rows, we eliminate variables from subsequent rows to simplify the system.
4. **Back-Substitution**: Once the matrix is in row-echelon form, we solve for the variables starting from the last row and substituting back into the earlier rows.

---

### Final Answer
- \( a = \frac{45}{122} \) chickens per official,
- \( b = \frac{41}{122} \) chickens per clerk,
- \( c = \frac{97}{122} \) chickens per attendant.
"""


"""
"""
