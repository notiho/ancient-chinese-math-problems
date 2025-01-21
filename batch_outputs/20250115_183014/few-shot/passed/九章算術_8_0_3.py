"""
今有上禾三秉，中禾二秉，下禾一秉，實三十九斗；上禾二秉，中禾三秉，下禾一秉，實三十四斗；上禾一秉，中禾二秉，下禾三秉，實二十六斗。問︰上、中、下禾實一秉各幾何？
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾 a秉 ， b斗 ，中禾 c秉 ， d斗 ，下禾 e秉 ， f斗 。
"""

"""
This problem involves solving a system of linear equations using ancient Chinese methods, which resemble Gaussian elimination. Let's break it down step by step and translate it into Python code.

### Problem Setup:
We are given three equations:
1. \( 3x + 2y + z = 39 \)
2. \( 2x + 3y + z = 34 \)
3. \( x + 2y + 3z = 26 \)

Where:
- \( x \) is the amount of dou per秉 for the upper grain (上禾),
- \( y \) is the amount of dou per秉 for the middle grain (中禾),
- \( z \) is the amount of dou per秉 for the lower grain (下禾).

We need to solve for \( x \), \( y \), and \( z \).

---

### Procedure:
The ancient method involves systematically eliminating variables to solve for each unknown. Here's the Python implementation:


"""


from fractions import Fraction

# Coefficients and constants from the equations
# 3x + 2y + z = 39
# 2x + 3y + z = 34
# x + 2y + 3z = 26
coefficients = [
    [3, 2, 1, 39],  # Equation 1
    [2, 3, 1, 34],  # Equation 2
    [1, 2, 3, 26]   # Equation 3
]

# Step 1: Eliminate the first variable (x) from the second and third equations
factor1 = Fraction(coefficients[1][0], coefficients[0][0])  # Factor to eliminate x from equation 2
for i in range(4):
    coefficients[1][i] -= factor1 * coefficients[0][i]

factor2 = Fraction(coefficients[2][0], coefficients[0][0])  # Factor to eliminate x from equation 3
for i in range(4):
    coefficients[2][i] -= factor2 * coefficients[0][i]

# Step 2: Eliminate the second variable (y) from the third equation
factor3 = Fraction(coefficients[2][1], coefficients[1][1])  # Factor to eliminate y from equation 3
for i in range(4):
    coefficients[2][i] -= factor3 * coefficients[1][i]

# Step 3: Solve for z (the third variable)
z = Fraction(coefficients[2][3], coefficients[2][2])

# Step 4: Solve for y (the second variable)
y = Fraction(coefficients[1][3] - coefficients[1][2] * z, coefficients[1][1])

# Step 5: Solve for x (the first variable)
x = Fraction(coefficients[0][3] - coefficients[0][2] * z - coefficients[0][1] * y, coefficients[0][0])

# Results
a, b = 1, x  # 上禾: 1秉, x斗
c, d = 1, y  # 中禾: 1秉, y斗
e, f = 1, z  # 下禾: 1秉, z斗

print(f"上禾 {a}秉, {b}斗")
print(f"中禾 {c}秉, {d}斗")
print(f"下禾 {e}秉, {f}斗")


"""


---

### Explanation:
1. **Step 1:** Eliminate \( x \) from the second and third equations by subtracting appropriate multiples of the first equation.
2. **Step 2:** Eliminate \( y \) from the third equation by subtracting an appropriate multiple of the second equation.
3. **Step 3:** Solve for \( z \) using the simplified third equation.
4. **Step 4:** Back-substitute \( z \) into the second equation to solve for \( y \).
5. **Step 5:** Back-substitute \( y \) and \( z \) into the first equation to solve for \( x \).

---

### Final Answer:
The output will provide the values of \( x \), \( y \), and \( z \), which represent the amount of dou per秉 for the upper, middle, and lower grains, respectively.
"""


"""
"""
