"""
今有令一人吏五人從者一十人食雞一十令一十人吏一人從者五人食雞八令五人吏一十人從者一人食雞六問令吏從者食雞各幾何
術曰如方程以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰令 a人 食 b雞 吏 c人 食 d雞 從者 e人 食 f雞 
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese "fangcheng" (方程) method, which is equivalent to solving simultaneous equations. The problem describes the relationships between three groups of people (令, 吏, 從者) and the number of chickens they consume, and we are tasked with finding how many chickens each group consumes per person.

### Problem Setup:
- Case 1: 1 令, 5 吏, 10 從者 eat 10 chickens.
- Case 2: 10 令, 1 吏, 5 從者 eat 8 chickens.
- Case 3: 5 令, 10 吏, 1 從者 eat 6 chickens.

We need to solve for the number of chickens consumed per person for each group:  
令 = `a` chickens per person, 吏 = `c` chickens per person, 從者 = `e` chickens per person.

---

### Fangcheng Procedure:
The procedure involves setting up a matrix of coefficients and solving it step by step using elimination and substitution. Below is the Python implementation of the procedure.


"""


from fractions import Fraction

# Coefficients from the problem
# Case 1: 1令 + 5吏 + 10從者 = 10
# Case 2: 10令 + 1吏 + 5從者 = 8
# Case 3: 5令 + 10吏 + 1從者 = 6

# Initial matrix setup
matrix = [
    [1, 5, 10, 10],  # Row 1: Coefficients for 令, 吏, 從者, and total chickens
    [10, 1, 5, 8],   # Row 2
    [5, 10, 1, 6]    # Row 3
]

# Step 1: Normalize the first row (make the coefficient of 令 in the first row 1)
factor = matrix[0][0]
matrix[0] = [Fraction(x, factor) for x in matrix[0]]

# Step 2: Eliminate the 令 term from the second and third rows
for i in range(1, 3):
    factor = matrix[i][0]
    matrix[i] = [matrix[i][j] - factor * matrix[0][j] for j in range(4)]

# Step 3: Normalize the second row (make the coefficient of 吏 in the second row 1)
factor = matrix[1][1]
matrix[1] = [Fraction(x, factor) for x in matrix[1]]

# Step 4: Eliminate the 吏 term from the third row
factor = matrix[2][1]
matrix[2] = [matrix[2][j] - factor * matrix[1][j] for j in range(4)]

# Step 5: Normalize the third row (make the coefficient of 從者 in the third row 1)
factor = matrix[2][2]
matrix[2] = [Fraction(x, factor) for x in matrix[2]]

# Step 6: Back-substitute to solve for 吏 and 令
# Solve for 從者 (e)
e = matrix[2][3]

# Solve for 吏 (c)
c = matrix[1][3] - matrix[1][2] * e

# Solve for 令 (a)
a = matrix[0][3] - matrix[0][1] * c - matrix[0][2] * e

# Results
b = a  # Chickens eaten by 令
d = c  # Chickens eaten by 吏
f = e  # Chickens eaten by 從者

# Output results
a, b, c, d, e, f


"""


---

### Explanation of the Code:
1. **Matrix Setup**: The coefficients of the equations are placed in a matrix, where each row represents an equation, and the last column represents the total number of chickens.
2. **Row Normalization**: Each row is normalized to make the leading coefficient 1.
3. **Elimination**: Terms are eliminated from subsequent rows to simplify the system into an upper triangular form.
4. **Back-Substitution**: The values of `e`, `c`, and `a` are calculated by substituting known values back into the equations.
5. **Results**: The values of `a`, `b`, `c`, `d`, `e`, and `f` are the solutions to the problem.

---

### Final Answer:
- 令: `a` people eat `b` chickens.
- 吏: `c` people eat `d` chickens.
- 從者: `e` people eat `f` chickens.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 45/122
Variable 'c' has wrong value. Expected: 1, Actual: 41/122
Variable 'e' has wrong value. Expected: 1, Actual: 97/122"""
