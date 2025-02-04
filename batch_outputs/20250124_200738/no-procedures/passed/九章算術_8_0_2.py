"""
今有上禾三秉，中禾二秉，下禾一秉，實三十九斗；上禾二秉，中禾三秉，下禾一秉，實三十四斗；上禾一秉，中禾二秉，下禾三秉，實二十六斗。問︰上、中、下禾實一秉各幾何？
荅曰：上禾一秉， a斗 ，中禾一秉， b斗 ，下禾一秉， c斗 。
"""

"""
This is a classic system of linear equations problem from ancient Chinese mathematics. Let's solve it step by step in Python.

### Problem:
We are given three types of grain bundles: upper (上禾), middle (中禾), and lower (下禾). Their respective contributions to the total volume of grain (in dou) are described by the following equations:

1. \( 3x + 2y + z = 39 \)
2. \( 2x + 3y + z = 34 \)
3. \( x + 2y + 3z = 26 \)

Where:
- \( x \) is the amount of grain (in dou) produced by one bundle of upper grain (上禾),
- \( y \) is the amount of grain (in dou) produced by one bundle of middle grain (中禾),
- \( z \) is the amount of grain (in dou) produced by one bundle of lower grain (下禾).

We need to solve for \( x \), \( y \), and \( z \).

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Coefficients of the equations
# 3x + 2y + z = 39
# 2x + 3y + z = 34
# x + 2y + 3z = 26

# Define the equations
a1, b1, c1, d1 = 3, 2, 1, 39  # First equation
a2, b2, c2, d2 = 2, 3, 1, 34  # Second equation
a3, b3, c3, d3 = 1, 2, 3, 26  # Third equation

# Solve using elimination
# Step 1: Eliminate x from the second and third equations
m1 = Fraction(a2, a1)  # Multiplier for the first equation to eliminate x from the second
m2 = Fraction(a3, a1)  # Multiplier for the first equation to eliminate x from the third

# Update the second equation
b2_new = b2 - m1 * b1
c2_new = c2 - m1 * c1
d2_new = d2 - m1 * d1

# Update the third equation
b3_new = b3 - m2 * b1
c3_new = c3 - m2 * c1
d3_new = d3 - m2 * d1

# Step 2: Eliminate y from the third equation
m3 = Fraction(b3_new, b2_new)  # Multiplier for the second equation to eliminate y from the third

c3_final = c3_new - m3 * c2_new
d3_final = d3_new - m3 * d2_new

# Step 3: Solve for z
z = Fraction(d3_final, c3_final)

# Step 4: Solve for y using the updated second equation
y = Fraction(d2_new - c2_new * z, b2_new)

# Step 5: Solve for x using the first equation
x = Fraction(d1 - b1 * y - c1 * z, a1)

# Results
a = x  # 上禾一秉
b = y  # 中禾一秉
c = z  # 下禾一秉

# Print the results
print(f"上禾一秉: {a}斗")
print(f"中禾一秉: {b}斗")
print(f"下禾一秉: {c}斗")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Define the equations**: Each equation is represented by its coefficients \( a, b, c \) (for \( x, y, z \)) and the constant \( d \).
2. **Elimination**: We use the method of elimination to reduce the system of three equations to two equations, and then to one equation.
3. **Back-substitution**: After solving for \( z \), we substitute back to find \( y \), and then \( x \).
4. **Fractions**: The `Fraction` class ensures that all calculations are exact and in fractional form.

---

### Output:
The solution will provide the values of \( x \), \( y \), and \( z \) (i.e., the grain produced by one bundle of upper, middle, and lower grain, respectively). For example:

```
上禾一秉: 7斗
中禾一秉: 5斗
下禾一秉: 3斗
```
"""


"""
"""
