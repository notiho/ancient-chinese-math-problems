"""
今有令一人吏五人從者一十人食雞一十令一十人吏一人從者五人食雞八令五人吏一十人從者一人食雞六問令吏從者食雞各幾何
術曰如方程以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰令一人食 a雞 吏一人食 b雞 從者一人食 c雞 
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method of elimination, as described in the "方程術" (method of solving systems of linear equations). Let's translate this into Python code step by step.

The problem can be summarized as follows:

1. A group of people (composed of leaders, officials, and followers) consumes a certain number of chickens, and the consumption rates of each type of person need to be determined.
2. The equations are:
   - \( 1 \cdot \text{令} + 5 \cdot \text{吏} + 10 \cdot \text{從者} = 10 \) (Equation 1)
   - \( 10 \cdot \text{令} + 1 \cdot \text{吏} + 5 \cdot \text{從者} = 8 \) (Equation 2)
   - \( 5 \cdot \text{令} + 10 \cdot \text{吏} + 1 \cdot \text{從者} = 6 \) (Equation 3)

The solution involves applying the elimination method described in the "方程術". Here's the Python implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Coefficients of the equations
# Equation 1: 1令 + 5吏 + 10從者 = 10
# Equation 2: 10令 + 1吏 + 5從者 = 8
# Equation 3: 5令 + 10吏 + 1從者 = 6

# Representing the system of equations as a matrix
# Each row is [令, 吏, 從者, constant]
matrix = [
    [1, 5, 10, 10],
    [10, 1, 5, 8],
    [5, 10, 1, 6]
]

# Step 1: Normalize the first row (make the leading coefficient 1)
factor = matrix[0][0]
matrix[0] = [Fraction(x, factor) for x in matrix[0]]

# Step 2: Eliminate the first variable (令) from the second and third rows
for i in range(1, 3):
    factor = matrix[i][0]
    matrix[i] = [matrix[i][j] - factor * matrix[0][j] for j in range(4)]

# Step 3: Normalize the second row (make the leading coefficient of 吏 1)
factor = matrix[1][1]
matrix[1] = [Fraction(x, factor) for x in matrix[1]]

# Step 4: Eliminate the second variable (吏) from the first and third rows
for i in [0, 2]:
    factor = matrix[i][1]
    matrix[i] = [matrix[i][j] - factor * matrix[1][j] for j in range(4)]

# Step 5: Normalize the third row (make the leading coefficient of 從者 1)
factor = matrix[2][2]
matrix[2] = [Fraction(x, factor) for x in matrix[2]]

# Step 6: Eliminate the third variable (從者) from the first and second rows
for i in [0, 1]:
    factor = matrix[i][2]
    matrix[i] = [matrix[i][j] - factor * matrix[2][j] for j in range(4)]

# The solution is now in the last column of the matrix
a = matrix[0][3]  # 令
b = matrix[1][3]  # 吏
c = matrix[2][3]  # 從者

# Output the results
a, b, c
#----- content ends here -----


"""


### Explanation of the Code:
1. **Matrix Representation**: The system of equations is represented as a matrix, where each row corresponds to an equation, and the last column is the constant term.
2. **Normalization**: Each row is normalized by dividing through by the leading coefficient to make it 1.
3. **Elimination**: Variables are eliminated from other rows by subtracting a multiple of the normalized row.
4. **Back Substitution**: Once the matrix is in reduced row-echelon form, the solution is read directly from the last column.

### Answer:
The solution gives the amount of chicken consumed by one leader (\(a\)), one official (\(b\)), and one follower (\(c\)).
"""


"""
"""
