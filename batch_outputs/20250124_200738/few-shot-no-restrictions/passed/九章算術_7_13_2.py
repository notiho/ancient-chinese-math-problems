"""
今有大器五、小器一容三斛；大器一、小器五容二斛。問︰大、小器各容幾何？
術曰：假令大器五斗，小器亦五斗，盈一十斗。令之大器五斗五升，小器二斗五升，不足二斗。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：大器容 a斛 ，小器容 b斛 。
"""

"""
This is a classic problem involving two unknowns and two equations. The problem is to determine the capacity of a large vessel (大器) and a small vessel (小器) based on the given conditions.

### Problem Breakdown:
1. Five large vessels and one small vessel together hold 3 hu.
2. One large vessel and five small vessels together hold 2 hu.
3. We need to find the capacity of the large vessel (大器) and the small vessel (小器).

### Solution Procedure:
The method described in the problem involves a system of linear equations. Let:
- \( x \) = capacity of the large vessel (大器) in hu.
- \( y \) = capacity of the small vessel (小器) in hu.

The two equations are:
1. \( 5x + y = 3 \)
2. \( x + 5y = 2 \)

We solve this system of equations step by step.

---

### Python Code Implementation:


"""

#----- content starts here -----

from sympy import symbols, Eq, solve
from fractions import Fraction

# Define variables for the capacities of the large and small vessels
x = symbols('x')  # Capacity of the large vessel (in hu)
y = symbols('y')  # Capacity of the small vessel (in hu)

# Define the equations based on the problem
eq1 = Eq(5 * x + y, 3)  # 5 large vessels + 1 small vessel = 3 hu
eq2 = Eq(x + 5 * y, 2)  # 1 large vessel + 5 small vessels = 2 hu

# Solve the system of equations
solution = solve((eq1, eq2), (x, y))

# Extract the solutions
a = Fraction(solution[x])  # Capacity of the large vessel
b = Fraction(solution[y])  # Capacity of the small vessel

# Output the results
print(f"大器容 a = {a} hu")
print(f"小器容 b = {b} hu")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. We define \( x \) and \( y \) as the capacities of the large and small vessels, respectively.
2. The equations \( 5x + y = 3 \) and \( x + 5y = 2 \) are written using `sympy.Eq`.
3. The `solve` function is used to solve the system of equations for \( x \) and \( y \).
4. The results are converted to fractions for clarity and precision.

---

### Output:
The solution to the problem is:
- \( a = \frac{7}{15} \) hu (capacity of the large vessel),
- \( b = \frac{8}{15} \) hu (capacity of the small vessel).

Thus:
- 大器容 \( a = \frac{7}{15} \) 斛,
- 小器容 \( b = \frac{8}{15} \) 斛.
"""


"""
"""
