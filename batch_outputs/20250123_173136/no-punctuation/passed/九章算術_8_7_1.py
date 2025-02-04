"""
今有賣牛二羊五以買十三豕有餘錢一千賣牛三豕三以買九羊錢適足賣羊六豕八以買五牛錢不足六百問牛羊豕價各幾何
術曰如方程置牛二羊五正豕一十三負餘錢數正次牛三正羊九負豕三正次牛五負羊六正豕八正不足錢負以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰牛價 a 羊價 b 豕價 c 
"""

"""
This is a classic simultaneous equations problem from ancient Chinese mathematics, solved using the "fangcheng" (method of solving systems of linear equations). Let's translate the problem and solution into Python code.

### Problem:
We are given three transactions involving cows, sheep, and pigs:
1. Selling 2 cows and 5 sheep to buy 13 pigs, with 1000 coins left over.
2. Selling 3 cows and 3 pigs to buy 9 sheep, with no money left over.
3. Selling 6 sheep and 8 pigs to buy 5 cows, but falling short by 600 coins.

We need to determine the price of a cow (`a`), a sheep (`b`), and a pig (`c`).

### Procedure:
The "fangcheng" method involves setting up a system of linear equations and solving it step by step. The equations are derived as follows:
1. \( 2a + 5b - 13c = 1000 \)
2. \( 3a - 9b + 3c = 0 \)
3. \( -5a + 6b + 8c = -600 \)

The solution involves systematically eliminating variables using the described procedure.

### Python Code:


"""


from fractions import Fraction

# Coefficients of the equations
# Equation 1: 2a + 5b - 13c = 1000
# Equation 2: 3a - 9b + 3c = 0
# Equation 3: -5a + 6b + 8c = -600

# Representing the system of equations as a matrix
matrix = [
    [2, 5, -13, 1000],  # Coefficients of a, b, c, and the constant term
    [3, -9, 3, 0],
    [-5, 6, 8, -600]
]

# Step 1: Eliminate the first variable (a) from the second and third equations
factor1 = Fraction(matrix[1][0], matrix[0][0])  # Factor to eliminate a from equation 2
factor2 = Fraction(matrix[2][0], matrix[0][0])  # Factor to eliminate a from equation 3

# Update equation 2
matrix[1] = [
    matrix[1][i] - factor1 * matrix[0][i] for i in range(4)
]

# Update equation 3
matrix[2] = [
    matrix[2][i] - factor2 * matrix[0][i] for i in range(4)
]

# Step 2: Eliminate the second variable (b) from the third equation
factor3 = Fraction(matrix[2][1], matrix[1][1])  # Factor to eliminate b from equation 3

# Update equation 3
matrix[2] = [
    matrix[2][i] - factor3 * matrix[1][i] for i in range(4)
]

# Step 3: Solve for c (third variable)
c = Fraction(matrix[2][3], matrix[2][2])

# Step 4: Back-substitute to solve for b (second variable)
b = Fraction(matrix[1][3] - matrix[1][2] * c, matrix[1][1])

# Step 5: Back-substitute to solve for a (first variable)
a = Fraction(matrix[0][3] - matrix[0][2] * c - matrix[0][1] * b, matrix[0][0])

# Final results
a = float(a)
b = float(b)
c = float(c)

print(f"牛價 a = {a}")
print(f"羊價 b = {b}")
print(f"豕價 c = {c}")


"""


### Explanation of the Code:
1. **Matrix Representation**: The system of equations is represented as a matrix, where each row corresponds to an equation, and each column corresponds to a variable or the constant term.
2. **Elimination**: The first variable (`a`) is eliminated from the second and third equations using appropriate factors. Then, the second variable (`b`) is eliminated from the third equation.
3. **Back-Substitution**: After reducing the system to a single equation in one variable (`c`), the value of `c` is determined. This value is substituted back into the previous equations to find `b` and `a`.
4. **Fractions**: The `Fraction` class is used to ensure exact arithmetic throughout the calculations.

### Output:
The code will output the prices of a cow (`a`), a sheep (`b`), and a pig (`c`) in terms of coins.
"""


"""
"""
