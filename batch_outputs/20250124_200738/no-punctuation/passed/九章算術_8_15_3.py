"""
今有令一人吏五人從者一十人食雞一十令一十人吏一人從者五人食雞八令五人吏一十人從者一人食雞六問令吏從者食雞各幾何
術曰如方程以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰令一人食 a雞 吏一人食 b雞 從者一人食 c雞 
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese "fangcheng" (方程) method, which is equivalent to solving simultaneous equations. The problem can be translated into a system of equations based on the given data:

### Problem Setup:
- Let `令` (L) represent the amount of chicken eaten by one "令" person.
- Let `吏` (O) represent the amount of chicken eaten by one "吏" person.
- Let `從者` (C) represent the amount of chicken eaten by one "從者" person.

The problem gives us the following equations based on the groups and their total chicken consumption:
1. \( 1L + 5O + 10C = 10 \)
2. \( 10L + 1O + 5C = 8 \)
3. \( 5L + 10O + 1C = 6 \)

We will solve this system of equations using the "fangcheng" method, which is essentially Gaussian elimination.

---

### Fangcheng Method Implementation in Python:


"""

#----- content starts here -----

from fractions import Fraction

# Coefficients of the equations
# Each row represents [L coefficient, O coefficient, C coefficient, total]
matrix = [
    [1, 5, 10, 10],  # 1L + 5O + 10C = 10
    [10, 1, 5, 8],   # 10L + 1O + 5C = 8
    [5, 10, 1, 6]    # 5L + 10O + 1C = 6
]

# Step 1: Normalize the first row (make the leading coefficient 1)
factor = matrix[0][0]
matrix[0] = [Fraction(x, factor) for x in matrix[0]]

# Step 2: Eliminate the first variable (L) from the second and third rows
for i in range(1, 3):
    factor = matrix[i][0]
    matrix[i] = [matrix[i][j] - factor * matrix[0][j] for j in range(4)]

# Step 3: Normalize the second row (make the leading coefficient of O 1)
factor = matrix[1][1]
matrix[1] = [Fraction(x, factor) for x in matrix[1]]

# Step 4: Eliminate the second variable (O) from the first and third rows
for i in [0, 2]:
    factor = matrix[i][1]
    matrix[i] = [matrix[i][j] - factor * matrix[1][j] for j in range(4)]

# Step 5: Normalize the third row (make the leading coefficient of C 1)
factor = matrix[2][2]
matrix[2] = [Fraction(x, factor) for x in matrix[2]]

# Step 6: Eliminate the third variable (C) from the first and second rows
for i in [0, 1]:
    factor = matrix[i][2]
    matrix[i] = [matrix[i][j] - factor * matrix[2][j] for j in range(4)]

# The solution is now in the last column of the matrix
a = matrix[0][3]  # L (令)
b = matrix[1][3]  # O (吏)
c = matrix[2][3]  # C (從者)

# Output the results
a, b, c
#----- content ends here -----


"""


---

### Explanation of the Steps:
1. **Normalize the first row**: Divide the first row by the coefficient of the first variable (L) to make it 1.
2. **Eliminate L from other rows**: Subtract multiples of the first row from the second and third rows to eliminate the L variable from those rows.
3. **Normalize the second row**: Divide the second row by the coefficient of the second variable (O) to make it 1.
4. **Eliminate O from other rows**: Subtract multiples of the second row from the first and third rows to eliminate the O variable from those rows.
5. **Normalize the third row**: Divide the third row by the coefficient of the third variable (C) to make it 1.
6. **Eliminate C from other rows**: Subtract multiples of the third row from the first and second rows to eliminate the C variable from those rows.
7. **Extract the solution**: The last column of the matrix now contains the values of L, O, and C.

---

### Final Answer:
After running the above code, the solution will be:
- \( a \): Amount of chicken eaten by one "令" person.
- \( b \): Amount of chicken eaten by one "吏" person.
- \( c \): Amount of chicken eaten by one "從者" person.
"""


"""
"""
