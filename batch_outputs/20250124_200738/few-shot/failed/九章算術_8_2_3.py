"""
今有上禾二秉，中禾三秉，下禾四秉，實皆不滿斗。上取中，中取下，下取上各一秉而實滿斗。問︰上、中、下禾實一秉各幾何？
術曰：如方程，各置所取，以正負術入之。正負術曰：同名相除，異名相益，正無入負之，負無入正之。其異名相除，同名相益，正無入正之，負無入負之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a斗 ，中禾一秉實 b斗 ，下禾一秉實 c斗 。
"""

"""
This problem involves solving a system of equations using ancient Chinese mathematical methods, specifically the "正負術" (positive and negative method) and "方程術" (method of equations). Below is the Python implementation of the solution:


"""

#----- content starts here -----

from fractions import Fraction

# 上禾二秉，中禾三秉，下禾四秉
上禾秉數 = 2
中禾秉數 = 3
下禾秉數 = 4

# 上取中，中取下，下取上各一秉而實滿斗
# This gives us the system of equations:
# 上禾 + 中禾 = 1
# 中禾 + 下禾 = 1
# 下禾 + 上禾 = 1

# Using 方程術 to solve the system of equations:
# Step 1: Represent the equations in terms of coefficients and constants
# 上禾 + 中禾 - 1 = 0
# 中禾 + 下禾 - 1 = 0
# 下禾 + 上禾 - 1 = 0

# Coefficients matrix (A) and constants vector (B)
A = [
    [1, 1, 0],  # 上禾 + 中禾 = 1
    [0, 1, 1],  # 中禾 + 下禾 = 1
    [1, 0, 1]   # 下禾 + 上禾 = 1
]
B = [1, 1, 1]

# Step 2: Solve the system of equations using elimination
# Using ancient Chinese methods, we eliminate variables step by step

# Eliminate 上禾 from the second and third equations
factor1 = Fraction(A[1][0], A[0][0])  # Factor to eliminate 上禾 from the second equation
A[1] = [A[1][i] - factor1 * A[0][i] for i in range(3)]
B[1] = B[1] - factor1 * B[0]

factor2 = Fraction(A[2][0], A[0][0])  # Factor to eliminate 上禾 from the third equation
A[2] = [A[2][i] - factor2 * A[0][i] for i in range(3)]
B[2] = B[2] - factor2 * B[0]

# Eliminate 中禾 from the third equation
factor3 = Fraction(A[2][1], A[1][1])  # Factor to eliminate 中禾 from the third equation
A[2] = [A[2][i] - factor3 * A[1][i] for i in range(3)]
B[2] = B[2] - factor3 * B[1]

# Step 3: Back-substitute to find the values of 上禾, 中禾, 下禾
下禾 = Fraction(B[2], A[2][2])
中禾 = Fraction(B[1] - A[1][2] * 下禾, A[1][1])
上禾 = Fraction(B[0] - A[0][1] * 中禾 - A[0][2] * 下禾, A[0][0])

# Results
a = 上禾
b = 中禾
c = 下禾

# Output the results
a, b, c
#----- content ends here -----


"""


### Explanation of the Code:
1. **System of Equations**:
   - The problem gives three equations based on the relationships between the different types of grain:
     - `上禾 + 中禾 = 1`
     - `中禾 + 下禾 = 1`
     - `下禾 + 上禾 = 1`

2. **Matrix Representation**:
   - The coefficients of the variables (`上禾`, `中禾`, `下禾`) are stored in a matrix `A`.
   - The constants on the right-hand side of the equations are stored in a vector `B`.

3. **Elimination**:
   - Using the ancient Chinese elimination method (similar to Gaussian elimination), variables are eliminated step by step to simplify the equations.

4. **Back-Substitution**:
   - After elimination, the values of the variables are calculated by substituting back into the simplified equations.

5. **Result**:
   - The values of `上禾`, `中禾`, and `下禾` are stored in `a`, `b`, and `c`, respectively, representing the amount of grain in dou for each秉.

### Final Answer:
- 上禾一秉實 `a` 斗
- 中禾一秉實 `b` 斗
- 下禾一秉實 `c` 斗
"""


"""
Variable 'a' has wrong value. Expected: 9/25, Actual: 1/2
Variable 'b' has wrong value. Expected: 7/25, Actual: 1/2
Variable 'c' has wrong value. Expected: 4/25, Actual: 1/2"""
