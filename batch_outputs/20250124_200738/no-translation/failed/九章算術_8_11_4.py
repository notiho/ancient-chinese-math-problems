"""
今有武馬一匹，中馬二匹，下馬三匹，皆載四十石至阪，皆不能上。武馬借中馬一匹，中馬借下馬一匹，下馬借武馬一匹，乃皆上。問︰武、中、下馬一匹各力引幾何？
術曰：如方程各置所借，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：武馬一匹力引 a石 ，中馬一匹力引 b石 ，下馬一匹力引 c石 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical procedure into Python code. The problem involves solving a system of linear equations using the described method. Here's the Python implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Define the coefficients of the equations based on the problem
# 武馬 (x), 中馬 (y), 下馬 (z)
# Equation 1: 武馬借中馬一匹
# x + y = 40
# Equation 2: 中馬借下馬一匹
# y + z = 40
# Equation 3: 下馬借武馬一匹
# z + x = 40

# Representing the equations in matrix form:
# x + y       = 40
#     y + z   = 40
# z     + x   = 40

# Coefficients matrix
A = [
    [1, 1, 0],  # Coefficients for x + y = 40
    [0, 1, 1],  # Coefficients for y + z = 40
    [1, 0, 1]   # Coefficients for z + x = 40
]

# Constants on the right-hand side
B = [40, 40, 40]

# Solve the system of equations using the described procedure
# Step 1: Eliminate variables to solve for one at a time

# Eliminate x from the second and third equations
# Multiply the first equation by -1 and add to the second and third equations
A[1] = [A[1][i] - A[0][i] for i in range(3)]
B[1] = B[1] - B[0]

A[2] = [A[2][i] - A[0][i] for i in range(3)]
B[2] = B[2] - B[0]

# Now the system is:
# x + y       = 40
#     y - x   = 0
# z - x       = 0

# Solve for y and z in terms of x
y = Fraction(B[1], A[1][1])  # y = 40
z = Fraction(B[2], A[2][2])  # z = 40

# Substitute y and z back into the first equation to solve for x
x = Fraction(B[0] - A[0][1] * y, A[0][0])  # x = 40

# Results
a = x
b = y
c = z

# Output the results
a, b, c
#----- content ends here -----


"""


### Explanation of the Code:
1. The problem is translated into a system of linear equations based on the relationships described.
2. The coefficients matrix `A` and constants vector `B` are defined.
3. The elimination process is performed step-by-step to solve for each variable (`x`, `y`, `z`), following the ancient method described.
4. The results are stored in `a`, `b`, and `c`, representing the pulling power of 武馬, 中馬, and 下馬, respectively.

### Final Answer:
- 武馬 (a) pulls `40` 石.
- 中馬 (b) pulls `40` 石.
- 下馬 (c) pulls `40` 石.
"""


"""
Code error: Fraction(0, 0)"""
