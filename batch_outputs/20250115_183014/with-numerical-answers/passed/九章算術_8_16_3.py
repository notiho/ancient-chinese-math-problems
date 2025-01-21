"""
今有五羊、四犬、三雞、二兔，直錢一千四百九十六；四羊、二犬、六雞、三兔直錢一千一百七十五；三羊、一犬、七雞、五兔，直錢九百五十八；二羊、三犬、五雞、一兔，直錢八百六十一。問︰羊、犬、雞、兔價各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：羊價 a(=177) ，犬價 b(=121) ，雞價 c(=23) ，兔價 d(=29) 。
"""

"""
The problem involves solving a system of linear equations to determine the prices of sheep, dogs, chickens, and rabbits. The ancient Chinese method described here is equivalent to solving simultaneous linear equations using elimination techniques.

Here is the Python implementation of the problem using the described method:


"""


from fractions import Fraction

# Given equations:
# 5羊 + 4犬 + 3雞 + 2兔 = 1496
# 4羊 + 2犬 + 6雞 + 3兔 = 1175
# 3羊 + 1犬 + 7雞 + 5兔 = 958
# 2羊 + 3犬 + 5雞 + 1兔 = 861

# Coefficients of the equations
A = [
    [5, 4, 3, 2],  # Coefficients for the first equation
    [4, 2, 6, 3],  # Coefficients for the second equation
    [3, 1, 7, 5],  # Coefficients for the third equation
    [2, 3, 5, 1],  # Coefficients for the fourth equation
]

# Constants on the right-hand side
B = [1496, 1175, 958, 861]

# Step 1: Convert the system into an upper triangular matrix
for i in range(len(A)):
    # Normalize the current row
    divisor = A[i][i]
    for j in range(i, len(A[i])):
        A[i][j] = Fraction(A[i][j], divisor)
    B[i] = Fraction(B[i], divisor)

    # Eliminate the current variable from the rows below
    for k in range(i + 1, len(A)):
        multiplier = A[k][i]
        for j in range(i, len(A[k])):
            A[k][j] -= multiplier * A[i][j]
        B[k] -= multiplier * B[i]

# Step 2: Back-substitution to solve for the variables
n = len(A)
X = [0] * n  # Solution vector
for i in range(n - 1, -1, -1):
    X[i] = B[i]
    for j in range(i + 1, n):
        X[i] -= A[i][j] * X[j]

# The solution
a, b, c, d = X  # a = price of sheep, b = price of dog, c = price of chicken, d = price of rabbit

# Results
print(f"羊價 a = {a} (177)")
print(f"犬價 b = {b} (121)")
print(f"雞價 c = {c} (23)")
print(f"兔價 d = {d} (29)")


"""


### Explanation of the Code:
1. **Matrix Representation**: The coefficients of the variables (sheep, dog, chicken, rabbit) are stored in a matrix `A`, and the constants on the right-hand side are stored in a list `B`.

2. **Gaussian Elimination**: The system of equations is converted into an upper triangular matrix using elimination. Each row is normalized by dividing by the pivot element, and then the rows below are updated to eliminate the current variable.

3. **Back-Substitution**: Starting from the last row, the solution for each variable is calculated by substituting the known values of the variables from the rows below.

4. **Fraction Handling**: The `Fraction` class is used to ensure exact arithmetic throughout the calculations, as described in the ancient Chinese method.

### Results:
- 羊價 (price of sheep) `a = 177`
- 犬價 (price of dog) `b = 121`
- 雞價 (price of chicken) `c = 23`
- 兔價 (price of rabbit) `d = 29`
"""


"""
"""
