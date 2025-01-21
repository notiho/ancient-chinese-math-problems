"""
今有五羊、四犬、三雞、二兔，直錢一千四百九十六；四羊、二犬、六雞、三兔直錢一千一百七十五；三羊、一犬、七雞、五兔，直錢九百五十八；二羊、三犬、五雞、一兔，直錢八百六十一。問︰羊、犬、雞、兔價各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：羊價 a(=177) ，犬價 b(=121) ，雞價 c(=23) ，兔價 d(=29) 。
"""

"""
The problem involves solving a system of linear equations to determine the prices of sheep, dogs, chickens, and rabbits. The ancient Chinese method described is equivalent to Gaussian elimination in modern terms. Below is the Python implementation of the solution:


"""


from fractions import Fraction

# Coefficients of the equations
# 5羊 + 4犬 + 3雞 + 2兔 = 1496
# 4羊 + 2犬 + 6雞 + 3兔 = 1175
# 3羊 + 1犬 + 7雞 + 5兔 = 958
# 2羊 + 3犬 + 5雞 + 1兔 = 861

# Initialize the augmented matrix
matrix = [
    [5, 4, 3, 2, 1496],
    [4, 2, 6, 3, 1175],
    [3, 1, 7, 5, 958],
    [2, 3, 5, 1, 861]
]

# Perform Gaussian elimination
for i in range(4):
    # Normalize the pivot row
    pivot = matrix[i][i]
    for j in range(i, 5):
        matrix[i][j] = Fraction(matrix[i][j], pivot)
    
    # Eliminate the current variable from the rows below
    for k in range(i + 1, 4):
        factor = matrix[k][i]
        for j in range(i, 5):
            matrix[k][j] -= factor * matrix[i][j]

# Back substitution
results = [0, 0, 0, 0]
for i in range(3, -1, -1):
    results[i] = matrix[i][4]
    for j in range(i + 1, 4):
        results[i] -= matrix[i][j] * results[j]

# Extract results
a = results[0]  # 羊價
b = results[1]  # 犬價
c = results[2]  # 雞價
d = results[3]  # 兔價

# Output the results
a, b, c, d  # 177, 121, 23, 29


"""


### Explanation of the Code:
1. **Matrix Representation**: The problem is represented as an augmented matrix, where the last column contains the constants (prices).
2. **Gaussian Elimination**: The matrix is row-reduced to upper triangular form by normalizing the pivot rows and eliminating variables from the rows below.
3. **Back Substitution**: Starting from the last row, the values of the variables are calculated by substituting known values into the equations.
4. **Results**: The prices of sheep, dogs, chickens, and rabbits are extracted as `a`, `b`, `c`, and `d`.

### Final Answer:
- Sheep price (*a*): 177
- Dog price (*b*): 121
- Chicken price (*c*): 23
- Rabbit price (*d*): 29
"""


"""
"""
