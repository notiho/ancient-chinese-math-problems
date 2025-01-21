"""
今有五家共井，甲二綆不足，如乙一綆；乙三綆不足，如丙一綆；丙四綆不足，如丁一綆；丁五綆不足，如戊一綆；戊六綆不足，如甲一綆。如各得所不足一綆，皆逮。問︰井深、綆長各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：井深 a丈 。甲綆長 b丈 ，乙綆長 c丈 ，丙綆長 d丈 ，丁綆長 e丈 ，戊綆長 f尺 。
"""

"""
This problem is a classic example of a system of linear equations, where the relationships between the rope lengths and the depth of the well are expressed in terms of deficiencies. The solution involves solving these equations using the ancient Chinese "正負術" (positive-negative method), which is equivalent to Gaussian elimination in modern terms. Below is the Python implementation of the procedure:


"""


from fractions import Fraction

# Define the equations based on the problem:
# Let the depth of the well be `井深 = a` (in zhang), and the rope lengths for each family be:
# 甲綆長 = b (in zhang), 乙綆長 = c (in zhang), 丙綆長 = d (in zhang), 丁綆長 = e (in zhang), 戊綆長 = f (in zhang).
# The relationships are:
# 1. a = b + 2
# 2. a = c + 3
# 3. a = d + 4
# 4. a = e + 5
# 5. a = f + 6
# 6. b = f + 1

# Step 1: Represent the system of equations in matrix form:
# Coefficients matrix (A) and constants vector (B):
# A = [[1, -1,  0,  0,  0,  0],  # a - b = 2
#      [1,  0, -1,  0,  0,  0],  # a - c = 3
#      [1,  0,  0, -1,  0,  0],  # a - d = 4
#      [1,  0,  0,  0, -1,  0],  # a - e = 5
#      [1,  0,  0,  0,  0, -1],  # a - f = 6
#      [0,  1,  0,  0,  0, -1]]  # b - f = 1
# B = [2, 3, 4, 5, 6, 1]

# Step 2: Solve the system using Gaussian elimination (正負術).

# Initialize the augmented matrix (A|B)
matrix = [
    [1, -1,  0,  0,  0,  0, 2],  # a - b = 2
    [1,  0, -1,  0,  0,  0, 3],  # a - c = 3
    [1,  0,  0, -1,  0,  0, 4],  # a - d = 4
    [1,  0,  0,  0, -1,  0, 5],  # a - e = 5
    [1,  0,  0,  0,  0, -1, 6],  # a - f = 6
    [0,  1,  0,  0,  0, -1, 1]   # b - f = 1
]

# Function to perform Gaussian elimination
def gaussian_elimination(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Forward elimination
    for i in range(rows):
        # Normalize the pivot row
        pivot = matrix[i][i]
        for j in range(cols):
            matrix[i][j] = Fraction(matrix[i][j], pivot)
        
        # Eliminate below
        for k in range(i + 1, rows):
            factor = matrix[k][i]
            for j in range(cols):
                matrix[k][j] -= factor * matrix[i][j]

    # Back substitution
    for i in range(rows - 1, -1, -1):
        for k in range(i - 1, -1, -1):
            factor = matrix[k][i]
            for j in range(cols):
                matrix[k][j] -= factor * matrix[i][j]

    # Extract solutions
    return [matrix[i][-1] for i in range(rows)]

# Solve the system
solutions = gaussian_elimination(matrix)

# Extract the results
井深 = solutions[0]
甲綆長 = solutions[1]
乙綆長 = solutions[2]
丙綆長 = solutions[3]
丁綆長 = solutions[4]
戊綆長 = solutions[5]

# Convert 井深 to 丈 and 綆長 to 尺 where necessary
a = 井深  # 井深 in 丈
b = 甲綆長  # 甲綆長 in 丈
c = 乙綆長  # 乙綆長 in 丈
d = 丙綆長  # 丙綆長 in 丈
e = 丁綆長  # 丁綆長 in 丈
f = 戊綆長 * 10  # 戊綆長 in 尺

# Output the results
a, b, c, d, e, f


"""


### Explanation of the Code:
1. **Matrix Representation**: The system of equations is represented as an augmented matrix `(A|B)`.
2. **Gaussian Elimination**: The `gaussian_elimination` function performs forward elimination to create an upper triangular matrix and then back substitution to solve for the variables.
3. **Conversion**: The depth of the well (`井深`) is expressed in zhang, and the rope lengths are expressed in zhang, except for `戊綆長`, which is converted to chi (1 zhang = 10 chi).
4. **Output**: The results are stored in variables `a`, `b`, `c`, `d`, `e`, and `f`.

### Final Answer:
- 井深 `a` 丈
- 甲綆長 `b` 丈
- 乙綆長 `c` 丈
- 丙綆長 `d` 丈
- 丁綆長 `e` 丈
- 戊綆長 `f` 尺
"""


"""
Code error: Fraction(0, 0)"""
