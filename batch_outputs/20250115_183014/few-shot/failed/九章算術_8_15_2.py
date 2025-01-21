"""
今有令一人、吏五人、從者一十人，食雞一十；令一十人、吏一人、從者五人，食雞八；令五人、吏一十人、從者一人，食雞六。問︰令、吏、從者食雞各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：令 a人 食 b雞 ，吏 c人 食 d雞 ，從者 e人 食 f雞 。
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method of elimination, which is similar to Gaussian elimination. Let's break it down and solve it step by step.

### Problem Setup:
We are tasked with determining how many chickens are eaten by each type of person: the "令" (official), the "吏" (clerk), and the "從者" (attendant). The given equations are:

1. \( 1 \cdot \text{令} + 5 \cdot \text{吏} + 10 \cdot \text{從者} = 10 \) (Equation 1)
2. \( 10 \cdot \text{令} + 1 \cdot \text{吏} + 5 \cdot \text{從者} = 8 \) (Equation 2)
3. \( 5 \cdot \text{令} + 10 \cdot \text{吏} + 1 \cdot \text{從者} = 6 \) (Equation 3)

We will solve this system of equations using the elimination method described in the "方程術" (method of solving simultaneous equations).

---

### Step-by-Step Solution in Python:


"""


from fractions import Fraction

# Coefficients of the equations
# Equation 1: 1令 + 5吏 + 10從者 = 10
# Equation 2: 10令 + 1吏 + 5從者 = 8
# Equation 3: 5令 + 10吏 + 1從者 = 6

# Representing the system of equations as a matrix
# Each row is [令, 吏, 從者, constant]
matrix = [
    [1, 5, 10, 10],
    [10, 1, 5, 8],
    [5, 10, 1, 6]
]

# Step 1: Normalize the first row by dividing by the coefficient of 令 in the first row
factor = matrix[0][0]
matrix[0] = [Fraction(x, factor) for x in matrix[0]]

# Step 2: Eliminate 令 from the second and third rows
for i in range(1, 3):
    factor = matrix[i][0]
    matrix[i] = [matrix[i][j] - factor * matrix[0][j] for j in range(4)]

# Step 3: Normalize the second row by dividing by the coefficient of 吏 in the second row
factor = matrix[1][1]
matrix[1] = [Fraction(x, factor) for x in matrix[1]]

# Step 4: Eliminate 吏 from the third row
factor = matrix[2][1]
matrix[2] = [matrix[2][j] - factor * matrix[1][j] for j in range(4)]

# Step 5: Normalize the third row by dividing by the coefficient of 從者 in the third row
factor = matrix[2][2]
matrix[2] = [Fraction(x, factor) for x in matrix[2]]

# Step 6: Back-substitute to solve for 吏 and 令
# Solve for 從者
從者 = matrix[2][3]

# Solve for 吏
吏 = matrix[1][3] - matrix[1][2] * 從者

# Solve for 令
令 = matrix[0][3] - matrix[0][1] * 吏 - matrix[0][2] * 從者

# Results
a = 令
b = a * 1  # Chickens eaten by 令
c = 吏
d = c * 1  # Chickens eaten by 吏
e = 從者
f = e * 1  # Chickens eaten by 從者

# Output the results
a, b, c, d, e, f


"""


---

### Explanation of the Code:
1. **Matrix Representation**: The system of equations is represented as a matrix where each row corresponds to an equation, and the last column represents the constants.
2. **Row Operations**: The elimination method is applied step by step to reduce the matrix to row echelon form.
3. **Back-Substitution**: Once the matrix is in row echelon form, the values of \( \text{從者} \), \( \text{吏} \), and \( \text{令} \) are determined through back-substitution.
4. **Results**: The values of \( \text{令} \), \( \text{吏} \), and \( \text{從者} \) are then used to calculate the number of chickens each eats.

---

### Final Answer:
The solution will provide the values of \( a \), \( b \), \( c \), \( d \), \( e \), and \( f \), which represent the number of people and the number of chickens eaten by each type of person.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 45/122
Variable 'c' has wrong value. Expected: 1, Actual: 41/122
Variable 'e' has wrong value. Expected: 1, Actual: 97/122"""
