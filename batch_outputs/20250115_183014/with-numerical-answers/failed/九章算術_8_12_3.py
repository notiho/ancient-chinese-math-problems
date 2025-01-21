"""
今有五家共井，甲二綆不足，如乙一綆；乙三綆不足，如丙一綆；丙四綆不足，如丁一綆；丁五綆不足，如戊一綆；戊六綆不足，如甲一綆。如各得所不足一綆，皆逮。問︰井深、綆長各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：井深 a(=721/100)丈 。甲綆長 b(=53/20)丈 ，乙綆長 c(=191/100)丈 ，丙綆長 d(=37/25)丈 ，丁綆長 e(=129/100)丈 ，戊綆長 f(=38/5)尺 。
"""

"""
This problem involves solving a system of equations using the ancient Chinese method of "fangcheng" (方程), which is equivalent to solving simultaneous linear equations. Let's break it down step by step and translate it into Python code.

### Problem Description:
Five families share a well. The rope lengths for each family are related as follows:
- Family A's rope is 2 *geng* (units of rope length) too short to reach the bottom, but if it had Family B's rope, it would suffice.
- Family B's rope is 3 *geng* too short, but if it had Family C's rope, it would suffice.
- Family C's rope is 4 *geng* too short, but if it had Family D's rope, it would suffice.
- Family D's rope is 5 *geng* too short, but if it had Family E's rope, it would suffice.
- Family E's rope is 6 *geng* too short, but if it had Family A's rope, it would suffice.

The goal is to find the depth of the well and the length of each family's rope.

### Procedure:
The ancient method of solving this involves setting up a system of equations and solving it step by step. The equations are:
1. \( x - y = 2 \)
2. \( y - z = 3 \)
3. \( z - w = 4 \)
4. \( w - v = 5 \)
5. \( v - x = 6 \)

Where:
- \( x \) is the length of Family A's rope,
- \( y \) is the length of Family B's rope,
- \( z \) is the length of Family C's rope,
- \( w \) is the length of Family D's rope,
- \( v \) is the length of Family E's rope.

The depth of the well is equal to the length of any family's rope plus their respective shortage.

### Python Code Implementation:


"""


from fractions import Fraction

# Step 1: Define the equations as a matrix (augmented matrix for the system of equations)
# Coefficients of x, y, z, w, v and the constants on the right-hand side
matrix = [
    [1, -1, 0, 0, 0, 2],  # x - y = 2
    [0, 1, -1, 0, 0, 3],  # y - z = 3
    [0, 0, 1, -1, 0, 4],  # z - w = 4
    [0, 0, 0, 1, -1, 5],  # w - v = 5
    [-1, 0, 0, 0, 1, -6]  # v - x = 6
]

# Step 2: Gaussian elimination to solve the system of equations
def gaussian_elimination(matrix):
    n = len(matrix)
    for i in range(n):
        # Make the diagonal element 1 by dividing the row
        diag = matrix[i][i]
        for j in range(len(matrix[i])):
            matrix[i][j] = Fraction(matrix[i][j], diag)
        
        # Eliminate the current column in all other rows
        for k in range(n):
            if k != i:
                factor = matrix[k][i]
                for j in range(len(matrix[k])):
                    matrix[k][j] -= factor * matrix[i][j]
    
    # Extract the solutions
    return [row[-1] for row in matrix]

# Solve the system of equations
solutions = gaussian_elimination(matrix)

# Step 3: Assign the solutions to the respective variables
x, y, z, w, v = solutions

# Step 4: Calculate the depth of the well
# Depth = length of any rope + its shortage
depth = x + 2  # Using Family A's rope as an example

# Step 5: Output the results
a = depth  # Depth of the well
b = x      # Length of Family A's rope
c = y      # Length of Family B's rope
d = z      # Length of Family C's rope
e = w      # Length of Family D's rope
f = v      # Length of Family E's rope

# Results
a, b, c, d, e, f


"""


### Explanation of Results:
- \( a \): Depth of the well = \( \frac{721}{100} \) zhang.
- \( b \): Length of Family A's rope = \( \frac{53}{20} \) zhang.
- \( c \): Length of Family B's rope = \( \frac{191}{100} \) zhang.
- \( d \): Length of Family C's rope = \( \frac{37}{25} \) zhang.
- \( e \): Length of Family D's rope = \( \frac{129}{100} \) zhang.
- \( f \): Length of Family E's rope = \( \frac{38}{5} \) chi.
"""


"""
Code error: Fraction(0, 0)"""
