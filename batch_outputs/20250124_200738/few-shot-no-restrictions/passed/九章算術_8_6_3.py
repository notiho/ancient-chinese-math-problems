"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
術曰：如方程。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：牛一，直金 a兩 ，羊一，直金 b兩 。
"""

"""
This problem involves solving a system of linear equations to determine the value of a cow and a sheep in terms of gold taels. The ancient Chinese method described is equivalent to solving simultaneous equations, which can be done using modern algebra or matrix methods. Let's translate this into Python code:

### Problem:
- 5 cows and 2 sheep are worth 10 taels of gold.
- 2 cows and 5 sheep are worth 8 taels of gold.
- Question: What is the value of one cow and one sheep?

### Solution:
We will solve the system of equations:
1. \( 5x + 2y = 10 \)
2. \( 2x + 5y = 8 \)

Where:
- \( x \) is the value of one cow in taels.
- \( y \) is the value of one sheep in taels.

We will use Python to solve this system of equations.

---


"""

#----- content starts here -----

from fractions import Fraction

# Coefficients of the equations
# Equation 1: 5x + 2y = 10
# Equation 2: 2x + 5y = 8

# Representing the equations as matrices
# Ax = B
A = [
    [5, 2],  # Coefficients of x and y in the first equation
    [2, 5]   # Coefficients of x and y in the second equation
]
B = [10, 8]  # Constants on the right-hand side

# Solving the system of equations using substitution/elimination
# Step 1: Eliminate one variable (y) by multiplying equations and subtracting
# Multiply the first equation by 5 and the second equation by 2 to align the coefficients of y
A1 = [5 * A[0][0], 5 * A[0][1]]  # [25x, 10y]
A2 = [2 * A[1][0], 2 * A[1][1]]  # [4x, 10y]
B1 = 5 * B[0]  # 50
B2 = 2 * B[1]  # 16

# Subtract the second equation from the first to eliminate y
# (25x - 4x) = (50 - 16)
x_coefficient = A1[0] - A2[0]  # 21x
x_value = B1 - B2  # 34
x = Fraction(x_value, x_coefficient)  # x = 34 / 21

# Step 2: Solve for y using one of the original equations
# Substitute x into the first equation: 5x + 2y = 10
y_value = B[0] - (A[0][0] * x)  # 10 - 5x
y = Fraction(y_value, A[0][1])  # y = (10 - 5x) / 2

# Results
a = x  # Value of one cow
b = y  # Value of one sheep

print(f"牛一，直金 {a} 兩，羊一，直金 {b} 兩。")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. The system of equations is represented as matrices \( A \) (coefficients) and \( B \) (constants).
2. The elimination method is used to solve for \( x \) (value of a cow) by aligning and subtracting the equations to eliminate \( y \).
3. Once \( x \) is found, it is substituted back into one of the original equations to solve for \( y \) (value of a sheep).
4. The results are expressed as fractions using Python's `Fraction` class for exact values.

---

### Answer:
The output will give the exact values of \( a \) (value of one cow) and \( b \) (value of one sheep) in taels of gold.
"""


"""
"""
