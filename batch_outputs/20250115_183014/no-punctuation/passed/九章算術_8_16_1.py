"""
今有五羊四犬三雞二兔直錢一千四百九十六四羊二犬六雞三兔直錢一千一百七十五三羊一犬七雞五兔直錢九百五十八二羊三犬五雞一兔直錢八百六十一問羊犬雞兔價各幾何
術曰如方程以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰羊價 a 犬價 b 雞價 c 兔價 d 
"""

"""
This problem involves solving a system of linear equations using ancient Chinese methods, specifically the "fangcheng" (方程) method, which is equivalent to solving simultaneous equations. The problem gives the prices of combinations of animals (sheep, dogs, chickens, and rabbits) and asks for the individual prices of each animal.

The equations are as follows:
1. \( 5x + 4y + 3z + 2w = 1496 \)
2. \( 4x + 2y + 6z + 3w = 1175 \)
3. \( 3x + 1y + 7z + 5w = 958 \)
4. \( 2x + 3y + 5z + 1w = 861 \)

Where:
- \( x \) is the price of a sheep,
- \( y \) is the price of a dog,
- \( z \) is the price of a chicken,
- \( w \) is the price of a rabbit.

The solution will follow the "fangcheng" method, which involves elimination and substitution.


"""


from fractions import Fraction

# Coefficients of the equations
# Equation 1: 5x + 4y + 3z + 2w = 1496
# Equation 2: 4x + 2y + 6z + 3w = 1175
# Equation 3: 3x + 1y + 7z + 5w = 958
# Equation 4: 2x + 3y + 5z + 1w = 861

# Initialize the matrix (augmented matrix of coefficients and constants)
matrix = [
    [5, 4, 3, 2, 1496],
    [4, 2, 6, 3, 1175],
    [3, 1, 7, 5, 958],
    [2, 3, 5, 1, 861]
]

# Step 1: Eliminate the first variable (x)
for i in range(1, 4):
    factor = Fraction(matrix[i][0], matrix[0][0])
    for j in range(5):
        matrix[i][j] -= factor * matrix[0][j]

# Step 2: Eliminate the second variable (y)
for i in range(2, 4):
    factor = Fraction(matrix[i][1], matrix[1][1])
    for j in range(1, 5):
        matrix[i][j] -= factor * matrix[1][j]

# Step 3: Eliminate the third variable (z)
factor = Fraction(matrix[3][2], matrix[2][2])
for j in range(2, 5):
    matrix[3][j] -= factor * matrix[2][j]

# Step 4: Back substitution to solve for w, z, y, x
w = Fraction(matrix[3][4], matrix[3][3])
z = Fraction(matrix[2][4] - matrix[2][3] * w, matrix[2][2])
y = Fraction(matrix[1][4] - matrix[1][3] * w - matrix[1][2] * z, matrix[1][1])
x = Fraction(matrix[0][4] - matrix[0][3] * w - matrix[0][2] * z - matrix[0][1] * y, matrix[0][0])

# Results
a = x  # Price of a sheep
b = y  # Price of a dog
c = z  # Price of a chicken
d = w  # Price of a rabbit

a, b, c, d


"""


### Explanation of the Code:
1. **Matrix Representation**: The equations are represented as an augmented matrix, where the last column contains the constants.
2. **Elimination**: The "fangcheng" method eliminates variables step by step by subtracting multiples of one row from another, similar to Gaussian elimination.
3. **Back Substitution**: After the matrix is in upper triangular form, the variables are solved starting from the last equation and substituting back.

### Final Answer:
The values of \( a \), \( b \), \( c \), and \( d \) represent the prices of a sheep, a dog, a chicken, and a rabbit, respectively.
"""


"""
"""
