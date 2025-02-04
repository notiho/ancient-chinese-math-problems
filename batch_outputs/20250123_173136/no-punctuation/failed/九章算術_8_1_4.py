"""
今有上禾七秉損實一斗益之下禾二秉而實一十斗下禾八秉益實一斗與上禾二秉而實一十斗問上下禾實一秉各幾何
術曰如方程損之曰益益之曰損損實一斗者其實過一十斗也益實一斗者其實不滿一十斗也
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰上禾一秉實 a斗 下禾一秉實 b斗 
"""

"""
This is a classic problem involving simultaneous equations, solved using the ancient Chinese method of "fangcheng" (方程), which is equivalent to solving systems of linear equations. Let's translate the problem and procedure into Python code step by step.

### Problem Breakdown:
- There are two types of grain: "upper grain" (上禾) and "lower grain" (下禾).
- The relationships between the grains and their quantities are given:
  1. 7 bundles of upper grain lose 1 dou, and 2 bundles of lower grain gain 1 dou, resulting in 10 dou.
  2. 8 bundles of lower grain gain 1 dou, and 2 bundles of upper grain result in 10 dou.
- The goal is to find the amount of grain (in dou) per bundle for both upper grain and lower grain.

### Procedure:
The procedure involves setting up and solving a system of linear equations using the ancient "fangcheng" method. Here's the Python implementation:


"""


from fractions import Fraction

# Define the coefficients of the equations based on the problem statement
# Equation 1: 7 bundles of upper grain lose 1 dou, 2 bundles of lower grain gain 1 dou, total = 10 dou
# Equation 2: 8 bundles of lower grain gain 1 dou, 2 bundles of upper grain total = 10 dou

# Coefficients for the equations
# Equation 1: 7x - 2y = 10
# Equation 2: 2x + 8y = 10

# Step 1: Represent the equations in matrix form
# Coefficients matrix
A = [
    [7, -2],  # Coefficients of x (upper grain) and y (lower grain) in equation 1
    [2, 8]    # Coefficients of x (upper grain) and y (lower grain) in equation 2
]

# Constants on the right-hand side of the equations
B = [10, 10]

# Step 2: Solve using the fangcheng method (Gaussian elimination)

# Normalize the first row
factor = A[0][0]
A[0] = [Fraction(A[0][i], factor) for i in range(2)]
B[0] = Fraction(B[0], factor)

# Eliminate the first variable (x) from the second row
factor = A[1][0]
A[1] = [A[1][i] - factor * A[0][i] for i in range(2)]
B[1] = B[1] - factor * B[0]

# Normalize the second row
factor = A[1][1]
A[1] = [Fraction(A[1][i], factor) for i in range(2)]
B[1] = Fraction(B[1], factor)

# Back-substitute to solve for the first variable (x)
B[0] = B[0] - A[0][1] * B[1]

# The solutions are:
a = B[0]  # Upper grain (x)
b = B[1]  # Lower grain (y)

# Output the results
a, b


"""


### Explanation of the Code:
1. **Matrix Representation**: The equations are represented in matrix form for easier manipulation.
2. **Gaussian Elimination**: The fangcheng method is essentially Gaussian elimination:
   - Normalize the first row.
   - Eliminate the first variable from the second row.
   - Normalize the second row.
   - Back-substitute to find the solution.
3. **Fraction Handling**: The `Fraction` class is used to ensure exact arithmetic, as the problem involves ratios.

### Answer:
The solution will give:
- `a` = the amount of grain (in dou) per bundle of upper grain.
- `b` = the amount of grain (in dou) per bundle of lower grain.
"""


"""
Variable 'a' has wrong value. Expected: 35/26, Actual: 5/3
Variable 'b' has wrong value. Expected: 41/52, Actual: 5/6"""
