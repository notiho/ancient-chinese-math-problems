"""
今有上禾三秉，中禾二秉，下禾一秉，實三十九斗；上禾二秉，中禾三秉，下禾一秉，實三十四斗；上禾一秉，中禾二秉，下禾三秉，實二十六斗。問︰上、中、下禾實一秉各幾何？
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾 a秉 ， b斗 ，中禾 c秉 ， d斗 ，下禾 e秉 ， f斗 。
"""

"""
To solve this problem, we will use the method described in the "方程術" (system of equations). The problem involves three equations with three unknowns, representing the yield of each type of grain (上禾, 中禾, 下禾). Let's encode the solution step by step.

### Problem setup:
We have the following equations:
1. \( 3x + 2y + z = 39 \)
2. \( 2x + 3y + z = 34 \)
3. \( x + 2y + 3z = 26 \)

Where:
- \( x \) is the yield of one 秉 of 上禾,
- \( y \) is the yield of one 秉 of 中禾,
- \( z \) is the yield of one 秉 of 下禾.

We will solve for \( x \), \( y \), and \( z \) using the elimination method described in the procedure.

---


"""


from fractions import Fraction

# Step 1: Represent the equations as a system
# Equation 1: 3x + 2y + z = 39
# Equation 2: 2x + 3y + z = 34
# Equation 3: x + 2y + 3z = 26

# Coefficients of the equations
A = [[3, 2, 1],  # Coefficients of x, y, z in Equation 1
     [2, 3, 1],  # Coefficients of x, y, z in Equation 2
     [1, 2, 3]]  # Coefficients of x, y, z in Equation 3

# Constants on the right-hand side
B = [39, 34, 26]

# Step 2: Eliminate variables to solve for z
# Multiply Equation 1 by 2 and Equation 2 by 3 to align coefficients of x
E1 = [2 * A[0][0], 2 * A[0][1], 2 * A[0][2], 2 * B[0]]  # 2 * (3x + 2y + z = 39)
E2 = [3 * A[1][0], 3 * A[1][1], 3 * A[1][2], 3 * B[1]]  # 3 * (2x + 3y + z = 34)

# Subtract E2 from E1 to eliminate x
E3 = [E1[0] - E2[0], E1[1] - E2[1], E1[2] - E2[2], E1[3] - E2[3]]  # Resulting equation: y and z only

# Multiply Equation 2 by 1 and Equation 3 by 2 to align coefficients of x
E4 = [A[1][0], A[1][1], A[1][2], B[1]]       # 1 * (2x + 3y + z = 34)
E5 = [2 * A[2][0], 2 * A[2][1], 2 * A[2][2], 2 * B[2]]  # 2 * (x + 2y + 3z = 26)

# Subtract E5 from E4 to eliminate x
E6 = [E4[0] - E5[0], E4[1] - E5[1], E4[2] - E5[2], E4[3] - E5[3]]  # Resulting equation: y and z only

# Step 3: Eliminate y to solve for z
# Multiply E3 and E6 to align coefficients of y
E7 = [E3[1] * E6[0], E3[1] * E6[1], E3[1] * E6[2], E3[1] * E6[3]]  # Scale E6 by E3[1]
E8 = [E6[1] * E3[0], E6[1] * E3[1], E6[1] * E3[2], E6[1] * E3[3]]  # Scale E3 by E6[1]

# Subtract E8 from E7 to eliminate y
E9 = [E7[0] - E8[0], E7[1] - E8[1], E7[2] - E8[2], E7[3] - E8[3]]  # Resulting equation: z only

# Solve for z
z = Fraction(E9[3], E9[2])

# Step 4: Back-substitute to solve for y
y = Fraction(E3[3] - E3[2] * z, E3[1])

# Step 5: Back-substitute to solve for x
x = Fraction(B[0] - A[0][1] * y - A[0][2] * z, A[0][0])

# Results
a, b = 1, x  # 上禾: 1秉, x斗
c, d = 1, y  # 中禾: 1秉, y斗
e, f = 1, z  # 下禾: 1秉, z斗

# Output
a, b, c, d, e, f


"""
 

This Python code follows the procedure step by step to solve the system of equations and find the yield of each type of grain. The results are expressed as fractions to ensure accuracy.
"""


"""
"""
