"""
今有上禾六秉，損實一斗八升，當下禾一十秉。下禾十五秉，損實五升，當上禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾六秉正，下禾一十秉負，損實一斗八升正。次置上禾五秉負，下禾一十五秉正，損實五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a秉 實 b升 ，下禾 c秉 實 d升 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical procedure into Python code step by step. The problem involves solving a system of linear equations using the described method, which is essentially Gaussian elimination.

---

### Problem Setup:
We are solving for the "實" (yield per unit) of 上禾 (upper grain) and 下禾 (lower grain). The equations are derived from the problem statement:

1. \( 6 \cdot 上禾 - 10 \cdot 下禾 = 1斗8升 \)  
   (1斗8升 = \( 10 + 8 = 18升 \))  
   \( 6 \cdot 上禾 - 10 \cdot 下禾 = 18 \)

2. \( -5 \cdot 上禾 + 15 \cdot 下禾 = 5升 \)  
   \( -5 \cdot 上禾 + 15 \cdot 下禾 = 5 \)

---

### Procedure in Python:


"""


from fractions import Fraction

# Coefficients and constants from the equations
# Equation 1: 6 * 上禾 - 10 * 下禾 = 18
# Equation 2: -5 * 上禾 + 15 * 下禾 = 5

# Initialize the coefficients and constants
coefficients = [
    [6, -10, 18],  # First equation
    [-5, 15, 5]    # Second equation
]

# Step 1: Normalize the first row (divide by the leading coefficient)
leading_coefficient_1 = coefficients[0][0]
coefficients[0] = [Fraction(x, leading_coefficient_1) for x in coefficients[0]]

# Step 2: Eliminate the first variable from the second row
factor = coefficients[1][0] / coefficients[0][0]
coefficients[1] = [
    coefficients[1][i] - factor * coefficients[0][i]
    for i in range(len(coefficients[0]))
]

# Step 3: Solve for 下禾 (lower grain yield)
下禾 = coefficients[1][2] / coefficients[1][1]

# Step 4: Back-substitute to solve for 上禾 (upper grain yield)
上禾 = (coefficients[0][2] - coefficients[0][1] * 下禾) / coefficients[0][0]

# Results
a = 上禾.numerator  # Upper grain yield numerator
b = 上禾.denominator  # Upper grain yield denominator
c = 下禾.numerator  # Lower grain yield numerator
d = 下禾.denominator  # Lower grain yield denominator

# Output the results
print(f"上禾實: {a}/{b} 升")
print(f"下禾實: {c}/{d} 升")


"""


---

### Explanation of the Code:
1. **Equation Setup**: The two equations are represented as rows in a matrix, where each row contains the coefficients of the variables and the constant term.
2. **Gaussian Elimination**: The method described in the problem is essentially Gaussian elimination:
   - Normalize the first row.
   - Eliminate the first variable from the second row.
   - Solve for the second variable (下禾).
   - Back-substitute to solve for the first variable (上禾).
3. **Fraction Handling**: The `Fraction` class is used to ensure exact arithmetic with fractions, as required by the problem.

---

### Final Answer:
The results for \( a, b, c, d \) will be printed in fractional form, representing the yield per unit for both 上禾 and 下禾.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 8
Variable 'b' has wrong value. Expected: 8, Actual: 1
Variable 'c' has wrong value. Expected: 1, Actual: 3
Variable 'd' has wrong value. Expected: 3, Actual: 1"""
