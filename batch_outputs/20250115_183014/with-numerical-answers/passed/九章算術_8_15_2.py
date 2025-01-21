"""
今有令一人、吏五人、從者一十人，食雞一十；令一十人、吏一人、從者五人，食雞八；令五人、吏一十人、從者一人，食雞六。問︰令、吏、從者食雞各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：令 a(=1)人 食 b(=45/122)雞 ，吏 c(=1)人 食 d(=41/122)雞 ，從者 e(=1)人 食 f(=97/122)雞 。
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method of elimination, which is similar to Gaussian elimination in modern mathematics. The problem is to determine how many chickens are consumed by a single "Ling" (令), "Li" (吏), and "Congzhe" (從者) respectively.

### Problem Setup:
We are given three equations based on the number of people and the total chickens consumed:
1. \( 1 \text{ Ling} + 5 \text{ Li} + 10 \text{ Congzhe} = 10 \text{ chickens} \)
2. \( 10 \text{ Ling} + 1 \text{ Li} + 5 \text{ Congzhe} = 8 \text{ chickens} \)
3. \( 5 \text{ Ling} + 10 \text{ Li} + 1 \text{ Congzhe} = 6 \text{ chickens} \)

We solve this system of equations using the elimination method described in the procedure.

---

### Python Code Implementation:


"""


from fractions import Fraction

# Coefficients of the equations
# Equation 1: 1 Ling + 5 Li + 10 Congzhe = 10
# Equation 2: 10 Ling + 1 Li + 5 Congzhe = 8
# Equation 3: 5 Ling + 10 Li + 1 Congzhe = 6

# Initial matrix representation of the system
# [Ling, Li, Congzhe, Total Chickens]
matrix = [
    [1, 5, 10, 10],
    [10, 1, 5, 8],
    [5, 10, 1, 6]
]

# Step 1: Eliminate the first variable (Ling) from the second and third rows
factor1 = Fraction(matrix[1][0], matrix[0][0])
factor2 = Fraction(matrix[2][0], matrix[0][0])

for i in range(4):
    matrix[1][i] -= factor1 * matrix[0][i]
    matrix[2][i] -= factor2 * matrix[0][i]

# Step 2: Eliminate the second variable (Li) from the third row
factor3 = Fraction(matrix[2][1], matrix[1][1])

for i in range(4):
    matrix[2][i] -= factor3 * matrix[1][i]

# Step 3: Back-substitution to solve for Congzhe, Li, and Ling
# Solve for Congzhe
congzhe = Fraction(matrix[2][3], matrix[2][2])

# Solve for Li
li = Fraction(matrix[1][3] - matrix[1][2] * congzhe, matrix[1][1])

# Solve for Ling
ling = Fraction(matrix[0][3] - matrix[0][1] * li - matrix[0][2] * congzhe, matrix[0][0])

# Outputs
a = 1  # Ling
b = ling  # Chickens consumed by 1 Ling
c = 1  # Li
d = li  # Chickens consumed by 1 Li
e = 1  # Congzhe
f = congzhe  # Chickens consumed by 1 Congzhe

# Results
print(f"令 a(={a})人 食 b(={b})雞")
print(f"吏 c(={c})人 食 d(={d})雞")
print(f"從者 e(={e})人 食 f(={f})雞")


"""


---

### Explanation of the Results:
1. \( \text{Ling} \): \( b = \frac{45}{122} \) chickens per person.
2. \( \text{Li} \): \( d = \frac{41}{122} \) chickens per person.
3. \( \text{Congzhe} \): \( f = \frac{97}{122} \) chickens per person.

This solution follows the elimination method described in the ancient Chinese procedure and provides the exact fractional results for the number of chickens consumed by each type of person.
"""


"""
"""
