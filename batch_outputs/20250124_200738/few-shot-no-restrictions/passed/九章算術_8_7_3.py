"""
今有賣牛二、羊五，以買十三豕，有餘錢一千。賣牛三、豕三，以買九羊，錢適足。賣羊六、豕八，以買五牛，錢不足六百。問︰牛、羊、豕價各幾何？
術曰：如方程，置牛二、羊五正，豕一十三負，餘錢數正；次牛三正，羊九負，豕三正；次牛五負，羊六正，豕八正，不足錢負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：牛價 a ，羊價 b ，豕價 c 。
"""

"""
This is a classic system of linear equations problem from ancient Chinese mathematics. The problem involves determining the prices of cows, sheep, and pigs based on three transactions. Let's solve it step by step using Python and linear algebra.

The problem can be expressed as a system of three equations:

1. \( 2x + 5y - 13z = 1000 \)  
2. \( 3x - 9y + 3z = 0 \)  
3. \( -5x + 6y + 8z = -600 \)  

Where:
- \( x \): price of a cow
- \( y \): price of a sheep
- \( z \): price of a pig

We will solve this system using Python's `numpy` library for linear algebra.

---

### Python Code


"""

#----- content starts here -----

import numpy as np
from fractions import Fraction

# Coefficients of the equations
A = np.array([
    [2, 5, -13],  # Coefficients of the first equation
    [3, -9, 3],   # Coefficients of the second equation
    [-5, 6, 8]    # Coefficients of the third equation
])

# Constants on the right-hand side
B = np.array([1000, 0, -600])

# Solve the system of equations
solution = np.linalg.solve(A, B)

# Convert the solution to fractions for exact values
solution_as_fractions = [Fraction(x).limit_denominator() for x in solution]

# Extract the values
a, b, c = solution_as_fractions

# Print the results
print(f"牛價 (price of a cow): {a}")
print(f"羊價 (price of a sheep): {b}")
print(f"豕價 (price of a pig): {c}")
#----- content ends here -----


"""


---

### Explanation of the Code

1. **Matrix Representation**:  
   The system of equations is represented in matrix form as \( A \cdot X = B \), where:
   - \( A \) is the matrix of coefficients.
   - \( X \) is the vector of unknowns (\( x, y, z \)).
   - \( B \) is the vector of constants on the right-hand side.

2. **Solving the System**:  
   The `np.linalg.solve` function is used to solve the system of linear equations.

3. **Exact Fractions**:  
   Since the problem originates from ancient mathematics, it is likely that the solution involves exact fractions. The `Fraction` class is used to convert the results into fractions for precision.

4. **Output**:  
   The solution is printed as the prices of cows, sheep, and pigs.

---

### Output

After running the code, the output will be:

```
牛價 (price of a cow): a
羊價 (price of a sheep): b
豕價 (price of a pig): c
```

Where \( a \), \( b \), and \( c \) are the exact prices of the cow, sheep, and pig, respectively.
"""


"""
"""
