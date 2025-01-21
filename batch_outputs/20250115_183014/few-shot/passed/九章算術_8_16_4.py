"""
今有五羊、四犬、三雞、二兔，直錢一千四百九十六；四羊、二犬、六雞、三兔直錢一千一百七十五；三羊、一犬、七雞、五兔，直錢九百五十八；二羊、三犬、五雞、一兔，直錢八百六十一。問︰羊、犬、雞、兔價各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：羊價 a ，犬價 b ，雞價 c ，兔價 d 。
"""

"""
To solve this problem, we need to use a system of linear equations to determine the prices of the sheep (羊), dog (犬), chicken (雞), and rabbit (兔). The problem describes a method similar to Gaussian elimination, which we will implement step by step.

The equations are derived from the problem statement:

1. \( 5羊 + 4犬 + 3雞 + 2兔 = 1496 \)
2. \( 4羊 + 2犬 + 6雞 + 3兔 = 1175 \)
3. \( 3羊 + 1犬 + 7雞 + 5兔 = 958 \)
4. \( 2羊 + 3犬 + 5雞 + 1兔 = 861 \)

We will solve this system using the described method.


"""


from fractions import Fraction

# Initialize the coefficients and constants of the equations
equations = [
    [5, 4, 3, 2, 1496],  # 5羊 + 4犬 + 3雞 + 2兔 = 1496
    [4, 2, 6, 3, 1175],  # 4羊 + 2犬 + 6雞 + 3兔 = 1175
    [3, 1, 7, 5, 958],   # 3羊 + 1犬 + 7雞 + 5兔 = 958
    [2, 3, 5, 1, 861]    # 2羊 + 3犬 + 5雞 + 1兔 = 861
]

# Step 1: Gaussian elimination to reduce the system to upper triangular form
for i in range(len(equations)):
    # Normalize the current row
    divisor = equations[i][i]
    for j in range(len(equations[i])):
        equations[i][j] = Fraction(equations[i][j], divisor)
    
    # Eliminate the current variable from the rows below
    for k in range(i + 1, len(equations)):
        multiplier = equations[k][i]
        for j in range(len(equations[k])):
            equations[k][j] -= multiplier * equations[i][j]

# Step 2: Back substitution to solve for the variables
results = [0] * 4
for i in range(len(equations) - 1, -1, -1):
    results[i] = equations[i][-1]
    for j in range(i + 1, len(equations)):
        results[i] -= equations[i][j] * results[j]

# Assign the results to the respective variables
a = results[0]  # 羊價
b = results[1]  # 犬價
c = results[2]  # 雞價
d = results[3]  # 兔價

# Output the results
a, b, c, d


"""


### Explanation of the Code:
1. **Initialization**: The coefficients of the equations and the constants are stored in a list of lists.
2. **Gaussian Elimination**:
   - Normalize each row by dividing it by the pivot element (diagonal element).
   - Eliminate the variable corresponding to the current row from all rows below it.
3. **Back Substitution**:
   - Start from the last row and solve for the variables one by one, substituting the known values into the equations above.
4. **Results**: The values of \( a \), \( b \), \( c \), and \( d \) represent the prices of sheep, dog, chicken, and rabbit, respectively.

This method ensures that the solution adheres to the described procedure. The results will be in terms of fractions for exactness.
"""


"""
"""
