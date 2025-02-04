"""
今有五羊、四犬、三雞、二兔，直錢一千四百九十六；四羊、二犬、六雞、三兔直錢一千一百七十五；三羊、一犬、七雞、五兔，直錢九百五十八；二羊、三犬、五雞、一兔，直錢八百六十一。問︰羊、犬、雞、兔價各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：羊價 a ，犬價 b ，雞價 c ，兔價 d 。
"""

"""
This problem is a classic system of linear equations problem, where we are tasked with solving for the prices of sheep (羊), dogs (犬), chickens (雞), and rabbits (兔) based on the given equations. Let's translate the problem into Python code and solve it using linear algebra.

### Problem Setup
We are given the following equations:
1. \( 5a + 4b + 3c + 2d = 1496 \)
2. \( 4a + 2b + 6c + 3d = 1175 \)
3. \( 3a + 1b + 7c + 5d = 958 \)
4. \( 2a + 3b + 5c + 1d = 861 \)

Where:
- \( a \) is the price of a sheep (羊價),
- \( b \) is the price of a dog (犬價),
- \( c \) is the price of a chicken (雞價),
- \( d \) is the price of a rabbit (兔價).

We will solve this system of equations using Python's `numpy` library.

---

### Python Code


"""

#----- content starts here -----

import numpy as np
from fractions import Fraction

# Coefficients of the equations
coefficients = np.array([
    [5, 4, 3, 2],  # Coefficients for the first equation
    [4, 2, 6, 3],  # Coefficients for the second equation
    [3, 1, 7, 5],  # Coefficients for the third equation
    [2, 3, 5, 1]   # Coefficients for the fourth equation
])

# Constants on the right-hand side of the equations
constants = np.array([1496, 1175, 958, 861])

# Solve the system of equations
solution = np.linalg.solve(coefficients, constants)

# Convert the solution to fractions for exact values
solution_as_fractions = [Fraction(x).limit_denominator() for x in solution]

# Extract the values
a, b, c, d = solution_as_fractions

# Print the results
print(f"羊價 (price of a sheep): {a}")
print(f"犬價 (price of a dog): {b}")
print(f"雞價 (price of a chicken): {c}")
print(f"兔價 (price of a rabbit): {d}")
#----- content ends here -----


"""


---

### Explanation of the Code
1. **Matrix Representation**: The coefficients of the variables \( a, b, c, d \) are represented as a 4x4 matrix, and the constants on the right-hand side are represented as a 1D array.
2. **Solving the System**: We use `numpy.linalg.solve` to solve the system of linear equations.
3. **Exact Fractions**: To ensure exact results, we convert the floating-point solutions to fractions using Python's `Fraction` class.
4. **Output**: The solution is printed as the prices of sheep, dogs, chickens, and rabbits.

---

### Output
The output will display the exact prices of the animals in terms of fractions:
```
羊價 (price of a sheep): a
犬價 (price of a dog): b
雞價 (price of a chicken): c
兔價 (price of a rabbit): d
```

Replace `a`, `b`, `c`, and `d` with the computed values.
"""


"""
"""
