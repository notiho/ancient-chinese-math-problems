"""
今有令一人吏五人從者一十人食雞一十令一十人吏一人從者五人食雞八令五人吏一十人從者一人食雞六問令吏從者食雞各幾何
術曰如方程以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰令 a人 食 b雞 吏 c人 食 d雞 從者 e人 食 f雞 
"""

"""
This problem involves solving a system of equations using the ancient Chinese "fangcheng" (方程) method, which is equivalent to solving simultaneous linear equations. The problem describes the relationship between three groups of people (令, 吏, 從者) and the number of chickens they consume. Let's translate the problem and solution into Python code.

### Problem Description:
- Case 1: 1 令, 5 吏, and 10 從者 eat 10 chickens.
- Case 2: 10 令, 1 吏, and 5 從者 eat 8 chickens.
- Case 3: 5 令, 10 吏, and 1 從者 eat 6 chickens.

We are tasked to find how many chickens each group (令, 吏, 從者) eats per person.

### Fangcheng Procedure:
The procedure involves setting up a matrix of coefficients and solving it using elimination, similar to Gaussian elimination. Here's the Python implementation:


"""


from fractions import Fraction

# Coefficients of the equations
# Each row represents [令, 吏, 從者, total chickens]
equations = [
    [1, 5, 10, 10],  # Case 1
    [10, 1, 5, 8],   # Case 2
    [5, 10, 1, 6]    # Case 3
]

# Step 1: Normalize the first row (令 coefficient to 1)
factor = equations[0][0]
equations[0] = [Fraction(x, factor) for x in equations[0]]

# Step 2: Eliminate the 令 term from the second and third rows
for i in range(1, 3):
    factor = equations[i][0]
    equations[i] = [equations[i][j] - factor * equations[0][j] for j in range(4)]

# Step 3: Normalize the second row (吏 coefficient to 1)
factor = equations[1][1]
equations[1] = [Fraction(x, factor) for x in equations[1]]

# Step 4: Eliminate the 吏 term from the third row
factor = equations[2][1]
equations[2] = [equations[2][j] - factor * equations[1][j] for j in range(4)]

# Step 5: Normalize the third row (從者 coefficient to 1)
factor = equations[2][2]
equations[2] = [Fraction(x, factor) for x in equations[2]]

# Step 6: Back-substitute to solve for 吏 and 令
# Solve for 從者
從者 = equations[2][3]

# Solve for 吏
吏 = equations[1][3] - equations[1][2] * 從者

# Solve for 令
令 = equations[0][3] - equations[0][1] * 吏 - equations[0][2] * 從者

# Results
a = 令
b = 令 * 1  # Number of chickens eaten by 1 令
c = 吏
d = 吏 * 1  # Number of chickens eaten by 1 吏
e = 從者
f = 從者 * 1  # Number of chickens eaten by 1 從者

# Output
print(f"令 {a}人 食 {b}雞")
print(f"吏 {c}人 食 {d}雞")
print(f"從者 {e}人 食 {f}雞")


"""


### Explanation of the Code:
1. **Matrix Setup**: The coefficients of the equations are set up in a matrix form, where each row represents an equation.
2. **Normalization**: The leading coefficient of each row is normalized to 1.
3. **Elimination**: The leading term of each subsequent row is eliminated using the normalized row above it.
4. **Back-Substitution**: The values for 從者, 吏, and 令 are solved in reverse order.
5. **Results**: The solution gives the number of chickens each group eats per person.

### Answer:
The output will provide the values of `a`, `b`, `c`, `d`, `e`, and `f`, representing the number of people and the number of chickens consumed by each group.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 45/122
Variable 'c' has wrong value. Expected: 1, Actual: 41/122
Variable 'e' has wrong value. Expected: 1, Actual: 97/122"""
