"""
今有五羊、四犬、三雞、二兔，直錢一千四百九十六；四羊、二犬、六雞、三兔直錢一千一百七十五；三羊、一犬、七雞、五兔，直錢九百五十八；二羊、三犬、五雞、一兔，直錢八百六十一。問︰羊、犬、雞、兔價各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：羊價 a ，犬價 b ，雞價 c ，兔價 d 。
"""

"""
This problem is a system of linear equations, and the solution involves using the method of elimination (as described in the ancient Chinese "方程術"). Below is the Python implementation of the procedure:


"""


from fractions import Fraction

# Given equations:
# 5羊 + 4犬 + 3雞 + 2兔 = 1496
# 4羊 + 2犬 + 6雞 + 3兔 = 1175
# 3羊 + 1犬 + 7雞 + 5兔 = 958
# 2羊 + 3犬 + 5雞 + 1兔 = 861

# Coefficients of the equations
A = [
    [5, 4, 3, 2, 1496],  # First equation
    [4, 2, 6, 3, 1175],  # Second equation
    [3, 1, 7, 5, 958],   # Third equation
    [2, 3, 5, 1, 861]    # Fourth equation
]

# Step 1: Elimination process to reduce the system to upper triangular form
for i in range(4):  # Iterate over each row
    # Normalize the current row
    divisor = A[i][i]
    for j in range(i, 5):
        A[i][j] = Fraction(A[i][j], divisor)
    
    # Eliminate the current variable from the rows below
    for k in range(i + 1, 4):
        multiplier = A[k][i]
        for j in range(i, 5):
            A[k][j] -= multiplier * A[i][j]

# Step 2: Back substitution to solve for the variables
x = [0, 0, 0, 0]  # To store the solutions for 羊, 犬, 雞, 兔
for i in range(3, -1, -1):  # Start from the last row and move upwards
    x[i] = A[i][4]
    for j in range(i + 1, 4):
        x[i] -= A[i][j] * x[j]

# Assign the solutions to the respective variables
a = x[0]  # 羊價
b = x[1]  # 犬價
c = x[2]  # 雞價
d = x[3]  # 兔價

# Output the results
a, b, c, d


"""


### Explanation of the Code:
1. **Input the equations**: The coefficients of the equations are stored in a 2D list `A`, where each row represents an equation, and the last column represents the constant term.
2. **Elimination process**: The system is reduced to an upper triangular form using the elimination method described in the "方程術". This involves normalizing the pivot row and eliminating the variable from the rows below.
3. **Back substitution**: Starting from the last row, the variables are solved one by one by substituting the known values into the equations.
4. **Output the results**: The values of 羊 (a), 犬 (b), 雞 (c), and 兔 (d) are computed and returned.

### Final Answer:
The values of 羊價 (a), 犬價 (b), 雞價 (c), and 兔價 (d) will be computed as fractions or integers, depending on the input values.
"""


"""
"""
