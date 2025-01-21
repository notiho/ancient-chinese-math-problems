"""
今有上禾三秉，中禾二秉，下禾一秉，實三十九斗；上禾二秉，中禾三秉，下禾一秉，實三十四斗；上禾一秉，中禾二秉，下禾三秉，實二十六斗。問︰上、中、下禾實一秉各幾何？
荅曰：上禾 a秉 ， b斗 ，中禾 c秉 ， d斗 ，下禾 e秉 ， f斗 。
"""

"""
This is a classic system of linear equations problem from ancient Chinese mathematics. Let's solve it step by step.

### Problem Explanation:
We are given three types of grain bundles: upper grain (上禾), middle grain (中禾), and lower grain (下禾). The total amount of grain (in dou) for different combinations of these bundles is provided:

1. 3 upper bundles, 2 middle bundles, and 1 lower bundle yield 39 dou.
2. 2 upper bundles, 3 middle bundles, and 1 lower bundle yield 34 dou.
3. 1 upper bundle, 2 middle bundles, and 3 lower bundles yield 26 dou.

We need to find how much grain (in dou) is in one bundle of each type of grain.

---

### Solution in Python:


"""


from fractions import Fraction

# Define the equations:
# Let x = grain in one upper bundle (上禾)
# Let y = grain in one middle bundle (中禾)
# Let z = grain in one lower bundle (下禾)

# Equation 1: 3x + 2y + z = 39
# Equation 2: 2x + 3y + z = 34
# Equation 3: x + 2y + 3z = 26

# Solve the system of equations using substitution/elimination:

# Step 1: Eliminate z from the first two equations
# Subtract Equation 2 from Equation 1
# (3x + 2y + z) - (2x + 3y + z) = 39 - 34
eq1_minus_eq2 = (3 - 2, 2 - 3, 1 - 1, 39 - 34)  # (x, y, z, constant)
# Result: x - y = 5

# Step 2: Eliminate z from the second and third equations
# Subtract Equation 3 from Equation 2
# (2x + 3y + z) - (x + 2y + 3z) = 34 - 26
eq2_minus_eq3 = (2 - 1, 3 - 2, 1 - 3, 34 - 26)  # (x, y, z, constant)
# Result: x + y - 2z = 8

# Step 3: Solve the two-variable system (x - y = 5 and x + y - 2z = 8)
# From x - y = 5, we get x = y + 5
# Substitute x = y + 5 into x + y - 2z = 8
# (y + 5) + y - 2z = 8
# 2y - 2z = 3
# Simplify: y - z = 3/2

# Step 4: Solve for y and z
# From y - z = 3/2, we get z = y - 3/2
# Substitute z = y - 3/2 into Equation 3: x + 2y + 3z = 26
# Substitute x = y + 5 and z = y - 3/2:
# (y + 5) + 2y + 3(y - 3/2) = 26
# y + 5 + 2y + 3y - 9/2 = 26
# 6y + 5 - 9/2 = 26
# 6y - 9/2 = 21
# Multiply through by 2 to eliminate the fraction:
# 12y - 9 = 42
# 12y = 51
# y = 51/12 = 17/4

# Step 5: Solve for x and z
# x = y + 5 = 17/4 + 20/4 = 37/4
# z = y - 3/2 = 17/4 - 6/4 = 11/4

# Final results:
a, b = 1, Fraction(37, 4)  # Upper grain: 37/4 dou
c, d = 1, Fraction(17, 4)  # Middle grain: 17/4 dou
e, f = 1, Fraction(11, 4)  # Lower grain: 11/4 dou

# Print results
print(f"上禾: {a}秉, {b}斗")
print(f"中禾: {c}秉, {d}斗")
print(f"下禾: {e}秉, {f}斗")


"""


---

### Final Answer:
- 上禾: \( a = 1 \) 秉, \( b = \frac{37}{4} \) 斗
- 中禾: \( c = 1 \) 秉, \( d = \frac{17}{4} \) 斗
- 下禾: \( e = 1 \) 秉, \( f = \frac{11}{4} \) 斗
"""


"""
"""
