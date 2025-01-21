"""
今有賣牛二羊五以買十三豕有餘錢一千賣牛三豕三以買九羊錢適足賣羊六豕八以買五牛錢不足六百問牛羊豕價各幾何
術曰如方程置牛二羊五正豕一十三負餘錢數正次牛三正羊九負豕三正次牛五負羊六正豕八正不足錢負以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰牛價 a 羊價 b 豕價 c 
"""

"""
This is a classic simultaneous equations problem from ancient Chinese mathematics. The problem involves determining the prices of cows, sheep, and pigs based on three transactions. The solution uses the "fangcheng" (方程) method, which is an ancient Chinese method for solving systems of linear equations.

### Problem Restatement:
- **First transaction**: Selling 2 cows and 5 sheep can buy 13 pigs, with 1000 units of money left over.
- **Second transaction**: Selling 3 cows and 3 pigs can buy 9 sheep, with no money left over.
- **Third transaction**: Selling 6 sheep and 8 pigs can buy 5 cows, but 600 units of money are short.

We need to find the prices of a cow (`a`), a sheep (`b`), and a pig (`c`).

---

### Fangcheng Method Explanation:
The fangcheng method involves setting up a system of linear equations and solving them step by step using elimination and substitution. Here's the step-by-step breakdown:

1. **Set up the equations**:
   Let the price of a cow be `a`, the price of a sheep be `b`, and the price of a pig be `c`. From the problem:
   - \( 2a + 5b - 13c = 1000 \)  (Equation 1)
   - \( 3a - 9b + 3c = 0 \)      (Equation 2)
   - \( -5a + 6b + 8c = -600 \)  (Equation 3)

2. **Solve the system of equations**:
   Use the fangcheng method to eliminate variables step by step, ultimately solving for `a`, `b`, and `c`.

---

### Python Implementation:


"""


from fractions import Fraction

# Coefficients of the equations
# Equation 1: 2a + 5b - 13c = 1000
# Equation 2: 3a - 9b + 3c = 0
# Equation 3: -5a + 6b + 8c = -600

# Representing the system of equations as a matrix
matrix = [
    [2, 5, -13, 1000],  # Equation 1
    [3, -9, 3, 0],      # Equation 2
    [-5, 6, 8, -600]    # Equation 3
]

# Step 1: Eliminate the first variable (a) from the second and third equations
# Multiply the first row to align coefficients of 'a'
factor1 = Fraction(matrix[1][0], matrix[0][0])  # Factor to eliminate 'a' from row 2
factor2 = Fraction(matrix[2][0], matrix[0][0])  # Factor to eliminate 'a' from row 3

# Update rows 2 and 3
for i in range(4):
    matrix[1][i] -= factor1 * matrix[0][i]
    matrix[2][i] -= factor2 * matrix[0][i]

# Step 2: Eliminate the second variable (b) from the third equation
# Multiply the second row to align coefficients of 'b'
factor3 = Fraction(matrix[2][1], matrix[1][1])  # Factor to eliminate 'b' from row 3

# Update row 3
for i in range(4):
    matrix[2][i] -= factor3 * matrix[1][i]

# Step 3: Solve for 'c' (third variable)
c = Fraction(matrix[2][3], matrix[2][2])

# Step 4: Back-substitute to solve for 'b' (second variable)
b = Fraction(matrix[1][3] - matrix[1][2] * c, matrix[1][1])

# Step 5: Back-substitute to solve for 'a' (first variable)
a = Fraction(matrix[0][3] - matrix[0][2] * c - matrix[0][1] * b, matrix[0][0])

# Final results
a = float(a)  # Price of a cow
b = float(b)  # Price of a sheep
c = float(c)  # Price of a pig

print(f"牛價 a = {a}")
print(f"羊價 b = {b}")
print(f"豕價 c = {c}")


"""


---

### Explanation of the Code:
1. **Matrix Representation**: The system of equations is represented as a matrix, where each row corresponds to an equation.
2. **Elimination**: The fangcheng method eliminates variables step by step by aligning coefficients and subtracting rows.
3. **Back-Substitution**: After reducing the matrix to a triangular form, the variables are solved starting from the last equation.
4. **Fraction Handling**: The `Fraction` class is used to ensure exact arithmetic throughout the calculations.

---

### Final Answer:
The prices of the cow (`a`), sheep (`b`), and pig (`c`) will be printed as the result of the Python code.
"""


"""
"""
