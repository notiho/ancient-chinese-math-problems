"""
今有五羊、四犬、三雞、二兔，直錢一千四百九十六；四羊、二犬、六雞、三兔直錢一千一百七十五；三羊、一犬、七雞、五兔，直錢九百五十八；二羊、三犬、五雞、一兔，直錢八百六十一。問︰羊、犬、雞、兔價各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：羊價 a ，犬價 b ，雞價 c ，兔價 d 。
"""

"""
This problem is a classic system of linear equations, where the prices of sheep (羊), dogs (犬), chickens (雞), and rabbits (兔) are unknowns. The ancient Chinese method described here is equivalent to solving a system of linear equations using Gaussian elimination. Let's translate the problem and solution into Python code step by step.


"""

#----- content starts here -----

from fractions import Fraction

# Define the coefficients of the equations
# Each row represents the coefficients of the variables (羊, 犬, 雞, 兔) and the total price
equations = [
    [5, 4, 3, 2, 1496],  # 5羊 + 4犬 + 3雞 + 2兔 = 1496
    [4, 2, 6, 3, 1175],  # 4羊 + 2犬 + 6雞 + 3兔 = 1175
    [3, 1, 7, 5, 958],   # 3羊 + 1犬 + 7雞 + 5兔 = 958
    [2, 3, 5, 1, 861]    # 2羊 + 3犬 + 5雞 + 1兔 = 861
]

# Perform Gaussian elimination
# Step 1: Normalize the first row
for i in range(1, len(equations)):
    factor = Fraction(equations[i][0], equations[0][0])
    for j in range(len(equations[0])):
        equations[i][j] -= factor * equations[0][j]

# Step 2: Normalize the second row
for i in range(2, len(equations)):
    factor = Fraction(equations[i][1], equations[1][1])
    for j in range(1, len(equations[0])):
        equations[i][j] -= factor * equations[1][j]

# Step 3: Normalize the third row
factor = Fraction(equations[3][2], equations[2][2])
for j in range(2, len(equations[0])):
    equations[3][j] -= factor * equations[2][j]

# Back substitution to solve for the variables
d = Fraction(equations[3][4], equations[3][3])
c = Fraction(equations[2][4] - equations[2][3] * d, equations[2][2])
b = Fraction(equations[1][4] - equations[1][2] * c - equations[1][3] * d, equations[1][1])
a = Fraction(equations[0][4] - equations[0][1] * b - equations[0][2] * c - equations[0][3] * d, equations[0][0])

# Output the results
print(f"羊價 a = {a}")
print(f"犬價 b = {b}")
print(f"雞價 c = {c}")
print(f"兔價 d = {d}")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Input the equations**: Each row in the `equations` list represents one of the given equations, with the last element being the total price.
2. **Gaussian elimination**: The process systematically eliminates variables from the equations to reduce the system to an upper triangular form.
3. **Back substitution**: Once the system is in triangular form, the values of the variables are calculated starting from the last equation and substituting back into the previous equations.
4. **Fractions**: The `Fraction` class is used to ensure exact arithmetic, as the problem may involve non-integer solutions.

### Output:
The solution will provide the prices of sheep (`a`), dogs (`b`), chickens (`c`), and rabbits (`d`) in terms of exact fractions or integers.
"""


"""
"""
