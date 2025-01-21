"""
今有上禾三秉，中禾二秉，下禾一秉，實三十九斗；上禾二秉，中禾三秉，下禾一秉，實三十四斗；上禾一秉，中禾二秉，下禾三秉，實二十六斗。問︰上、中、下禾實一秉各幾何？
荅曰：上禾 a秉 ， b斗 ，中禾 c秉 ， d斗 ，下禾 e秉 ， f斗 。
"""

"""
This is a classic system of linear equations problem from ancient Chinese mathematics. Let's solve it step by step using Python and fractions to ensure precision.

### Problem:
We are given the following equations:
1. \( 3x + 2y + z = 39 \)
2. \( 2x + 3y + z = 34 \)
3. \( x + 2y + 3z = 26 \)

Where:
- \( x \) is the yield of one bundle of upper-grade grain (上禾),
- \( y \) is the yield of one bundle of middle-grade grain (中禾),
- \( z \) is the yield of one bundle of lower-grade grain (下禾).

We need to solve for \( x \), \( y \), and \( z \).

---

### Python Code:


"""


from fractions import Fraction

# Coefficients of the equations
# 3x + 2y + z = 39
# 2x + 3y + z = 34
# x + 2y + 3z = 26

# Step 1: Represent the equations
a1, b1, c1, d1 = 3, 2, 1, 39  # Equation 1
a2, b2, c2, d2 = 2, 3, 1, 34  # Equation 2
a3, b3, c3, d3 = 1, 2, 3, 26  # Equation 3

# Step 2: Eliminate one variable (z) using the first two equations
# Multiply equations to align coefficients of z
eq1_mult = a1 * c2 - a2 * c1  # Coefficient for x
eq2_mult = b1 * c2 - b2 * c1  # Coefficient for y
eq3_mult = d1 * c2 - d2 * c1  # Resultant constant

# Step 3: Eliminate z using the second and third equations
eq4_mult = a2 * c3 - a3 * c2  # Coefficient for x
eq5_mult = b2 * c3 - b3 * c2  # Coefficient for y
eq6_mult = d2 * c3 - d3 * c2  # Resultant constant

# Step 4: Solve for y by eliminating x
y_numerator = eq3_mult * eq4_mult - eq1_mult * eq6_mult
y_denominator = eq2_mult * eq4_mult - eq1_mult * eq5_mult
y = Fraction(y_numerator, y_denominator)

# Step 5: Solve for x using one of the reduced equations
x_numerator = eq3_mult - eq2_mult * y
x_denominator = eq1_mult
x = Fraction(x_numerator, x_denominator)

# Step 6: Solve for z using one of the original equations
z_numerator = d1 - a1 * x - b1 * y
z_denominator = c1
z = Fraction(z_numerator, z_denominator)

# Results
a, b = x.numerator, x.denominator  # Upper-grade grain
c, d = y.numerator, y.denominator  # Middle-grade grain
e, f = z.numerator, z.denominator  # Lower-grade grain

print(f"上禾 {a}秉 ， {b}斗 ，中禾 {c}秉 ， {d}斗 ，下禾 {e}秉 ， {f}斗 。")


"""


---

### Explanation:
1. The system of equations is solved using elimination and substitution.
2. Fractions are used to ensure precision in calculations.
3. The final results are expressed as fractions for each type of grain yield.

Let me know if you'd like me to run through the solution step-by-step!
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 37
Variable 'b' has wrong value. Expected: 37/4, Actual: 4
Variable 'c' has wrong value. Expected: 1, Actual: 17
Variable 'd' has wrong value. Expected: 17/4, Actual: 4
Variable 'e' has wrong value. Expected: 1, Actual: 11
Variable 'f' has wrong value. Expected: 11/4, Actual: 4"""
