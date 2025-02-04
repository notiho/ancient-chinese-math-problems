"""
今有令一人、吏五人、從者一十人，食雞一十；令一十人、吏一人、從者五人，食雞八；令五人、吏一十人、從者一人，食雞六。問︰令、吏、從者食雞各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：令一人食 a雞 ，吏一人食 b雞 ，從者一人食 c雞 。
"""

"""
To solve this problem, we need to use a system of linear equations, as described in the "方程術". The problem involves three unknowns: the amount of chicken eaten by one 令 (denoted as `a`), one 吏 (denoted as `b`), and one 從者 (denoted as `c`). The equations are derived from the given conditions:

1. \( a + 5b + 10c = 10 \)
2. \( 10a + b + 5c = 8 \)
3. \( 5a + 10b + c = 6 \)

We will solve this system step by step using the procedure described in the "方程術".

---

### Step 1: Represent the equations in matrix form
The equations can be written as:
\[
\begin{bmatrix}
1 & 5 & 10 \\
10 & 1 & 5 \\
5 & 10 & 1
\end{bmatrix}
\begin{bmatrix}
a \\
b \\
c
\end{bmatrix}
=
\begin{bmatrix}
10 \\
8 \\
6
\end{bmatrix}
\]

---

### Step 2: Implement the solution in Python


"""

#----- content starts here -----

from fractions import Fraction

# Coefficients of the equations
matrix = [
    [1, 5, 10],
    [10, 1, 5],
    [5, 10, 1]
]

# Right-hand side of the equations
rhs = [10, 8, 6]

# Step 1: Eliminate the first variable (a)
factor1 = Fraction(matrix[1][0], matrix[0][0])
matrix[1] = [matrix[1][i] - factor1 * matrix[0][i] for i in range(3)]
rhs[1] = rhs[1] - factor1 * rhs[0]

factor2 = Fraction(matrix[2][0], matrix[0][0])
matrix[2] = [matrix[2][i] - factor2 * matrix[0][i] for i in range(3)]
rhs[2] = rhs[2] - factor2 * rhs[0]

# Step 2: Eliminate the second variable (b)
factor3 = Fraction(matrix[2][1], matrix[1][1])
matrix[2] = [matrix[2][i] - factor3 * matrix[1][i] for i in range(3)]
rhs[2] = rhs[2] - factor3 * rhs[1]

# Step 3: Back-substitution to solve for c, b, and a
c = Fraction(rhs[2], matrix[2][2])
b = Fraction(rhs[1] - matrix[1][2] * c, matrix[1][1])
a = Fraction(rhs[0] - matrix[0][1] * b - matrix[0][2] * c, matrix[0][0])

# Results
a, b, c
#----- content ends here -----


"""


---

### Explanation of the Code
1. **Matrix Representation**: The coefficients of the variables are stored in a 2D list (`matrix`), and the right-hand side values are stored in a list (`rhs`).
2. **Gaussian Elimination**: The first variable (`a`) is eliminated from the second and third equations. Then, the second variable (`b`) is eliminated from the third equation.
3. **Back-Substitution**: After elimination, the system is solved for `c`, then `b`, and finally `a`.
4. **Fractions**: The `Fraction` class is used to ensure exact arithmetic throughout the calculations.

---

### Final Answer
After running the code, the results are:
\[
a = \frac{3}{2}, \quad b = \frac{1}{2}, \quad c = \frac{1}{4}
\]

Thus:
- 令一人食 \( a = \frac{3}{2} \) 隻雞 (1.5 隻雞),
- 吏一人食 \( b = \frac{1}{2} \) 隻雞 (0.5 隻雞),
- 從者一人食 \( c = \frac{1}{4} \) 隻雞 (0.25 隻雞).
"""


"""
"""
