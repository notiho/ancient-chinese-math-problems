"""
今有上禾三秉，中禾二秉，下禾一秉，實三十九斗；上禾二秉，中禾三秉，下禾一秉，實三十四斗；上禾一秉，中禾二秉，下禾三秉，實二十六斗。問︰上、中、下禾實一秉各幾何？
荅曰：上禾一秉， a斗 ，中禾一秉， b斗 ，下禾一秉， c斗 。
"""

"""
This is a classic system of linear equations problem. Let's solve it step by step in Python using fractions to ensure precision.

### Problem Breakdown:
We are given three equations:
1. \( 3x + 2y + z = 39 \)
2. \( 2x + 3y + z = 34 \)
3. \( x + 2y + 3z = 26 \)

Where:
- \( x \) is the amount of dou (斗) for one bundle of upper-grade grain (上禾),
- \( y \) is the amount of dou (斗) for one bundle of middle-grade grain (中禾),
- \( z \) is the amount of dou (斗) for one bundle of lower-grade grain (下禾).

We need to solve for \( x \), \( y \), and \( z \).

Here is the Python code to solve it:


"""

#----- content starts here -----

from fractions import Fraction

# Coefficients of the equations
# 3x + 2y + z = 39
# 2x + 3y + z = 34
# x + 2y + 3z = 26

# Define the equations
a1, b1, c1, d1 = 3, 2, 1, 39
a2, b2, c2, d2 = 2, 3, 1, 34
a3, b3, c3, d3 = 1, 2, 3, 26

# Solve using elimination
# Step 1: Eliminate x from the second and third equations
m1 = Fraction(a2, a1)
m2 = Fraction(a3, a1)

b2_new = b2 - m1 * b1
c2_new = c2 - m1 * c1
d2_new = d2 - m1 * d1

b3_new = b3 - m2 * b1
c3_new = c3 - m2 * c1
d3_new = d3 - m2 * d1

# Step 2: Eliminate y from the third equation
m3 = Fraction(b3_new, b2_new)

c3_final = c3_new - m3 * c2_new
d3_final = d3_new - m3 * d2_new

# Step 3: Solve for z
z = Fraction(d3_final, c3_final)

# Step 4: Solve for y
y = Fraction(d2_new - c2_new * z, b2_new)

# Step 5: Solve for x
x = Fraction(d1 - b1 * y - c1 * z, a1)

# Results
a = x  # Upper-grade grain (上禾) per bundle
b = y  # Middle-grade grain (中禾) per bundle
c = z  # Lower-grade grain (下禾) per bundle

print(f"上禾一秉, {a}斗，中禾一秉, {b}斗，下禾一秉, {c}斗。")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Step 1**: We eliminate \( x \) from the second and third equations by scaling and subtracting the first equation.
2. **Step 2**: We eliminate \( y \) from the third equation by scaling and subtracting the modified second equation.
3. **Step 3**: We solve for \( z \) from the simplified third equation.
4. **Step 4**: We back-substitute \( z \) into the second equation to solve for \( y \).
5. **Step 5**: We back-substitute \( y \) and \( z \) into the first equation to solve for \( x \).

### Output:
The solution will provide the values of \( a \), \( b \), and \( c \), which represent the amount of dou (斗) for one bundle of upper-grade, middle-grade, and lower-grade grain, respectively.
"""


"""
"""
