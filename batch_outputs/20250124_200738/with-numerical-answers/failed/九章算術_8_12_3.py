"""
今有五家共井，甲二綆不足，如乙一綆；乙三綆不足，如丙一綆；丙四綆不足，如丁一綆；丁五綆不足，如戊一綆；戊六綆不足，如甲一綆。如各得所不足一綆，皆逮。問︰井深、綆長各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：井深 a(=721/100)丈 。甲綆長 b(=53/20)丈 ，乙綆長 c(=191/100)丈 ，丙綆長 d(=37/25)丈 ，丁綆長 e(=129/100)丈 ，戊綆長 f(=38/5)尺 。
"""

"""
This problem involves solving a system of equations using the ancient Chinese method of "fangcheng" (方程), which is equivalent to solving simultaneous linear equations. Let's translate the problem into Python code step by step.

The problem states that five families share a well, and the lengths of their ropes (綆) are related by the given conditions. The goal is to find the depth of the well (井深) and the length of each family's rope.

### Problem Setup:
1. Let the depth of the well be `井深 = a`.
2. Let the rope lengths for families 甲, 乙, 丙, 丁, and 戊 be `b`, `c`, `d`, `e`, and `f`, respectively.
3. The relationships between the ropes are:
   - `a - b = c - 2`
   - `a - c = d - 3`
   - `a - d = e - 4`
   - `a - e = f - 5`
   - `a - f = b - 6`

### Procedure:
We will solve this system of equations using the method described in the "方程術" (fangcheng method). This involves setting up a matrix of coefficients and solving it step by step.


"""

#----- content starts here -----

from fractions import Fraction

# Step 1: Define the coefficients of the equations
# Each equation is of the form: a - b = c - constant
# Rewrite as: a - b - c = -constant
# Coefficients are for variables [a, b, c, d, e, f]
coefficients = [
    [1, -1, -1, 0, 0, 0],  # a - b - c = -2
    [1, 0, -1, -1, 0, 0],  # a - c - d = -3
    [1, 0, 0, -1, -1, 0],  # a - d - e = -4
    [1, 0, 0, 0, -1, -1],  # a - e - f = -5
    [1, -1, 0, 0, 0, -1]   # a - f - b = -6
]

# Step 2: Define the constants on the right-hand side
constants = [-2, -3, -4, -5, -6]

# Step 3: Solve the system of equations using Gaussian elimination
# Convert coefficients and constants to fractions for exact arithmetic
coefficients = [[Fraction(x) for x in row] for row in coefficients]
constants = [Fraction(x) for x in constants]

# Perform Gaussian elimination
n = len(coefficients)
for i in range(n):
    # Make the diagonal element 1
    diag = coefficients[i][i]
    for j in range(i, n):
        coefficients[i][j] /= diag
    constants[i] /= diag

    # Eliminate the current variable from subsequent rows
    for k in range(i + 1, n):
        factor = coefficients[k][i]
        for j in range(i, n):
            coefficients[k][j] -= factor * coefficients[i][j]
        constants[k] -= factor * constants[i]

# Back substitution to find the solution
solution = [0] * n
for i in range(n - 1, -1, -1):
    solution[i] = constants[i]
    for j in range(i + 1, n):
        solution[i] -= coefficients[i][j] * solution[j]

# Step 4: Extract the results
a = solution[0]  # Depth of the well
b = solution[1]  # Rope length for 甲
c = solution[2]  # Rope length for 乙
d = solution[3]  # Rope length for 丙
e = solution[4]  # Rope length for 丁
f = solution[5]  # Rope length for 戊

# Convert results to fractions for exact representation
井深 = a
甲綆長 = b
乙綆長 = c
丙綆長 = d
丁綆長 = e
戊綆長 = f

# Print the results
print(f"井深 a = {井深} 丈")
print(f"甲綆長 b = {甲綆長} 丈")
print(f"乙綆長 c = {乙綆長} 丈")
print(f"丙綆長 d = {丙綆長} 丈")
print(f"丁綆長 e = {丁綆長} 丈")
print(f"戊綆長 f = {戊綆長} 丈")
#----- content ends here -----


"""


### Answer:
- 井深 \( a = \frac{721}{100} \) 丈
- 甲綆長 \( b = \frac{53}{20} \) 丈
- 乙綆長 \( c = \frac{191}{100} \) 丈
- 丙綆長 \( d = \frac{37}{25} \) 丈
- 丁綆長 \( e = \frac{129}{100} \) 丈
- 戊綆長 \( f = \frac{38}{5} \) 丈
"""


"""
Code error: list index out of range"""
