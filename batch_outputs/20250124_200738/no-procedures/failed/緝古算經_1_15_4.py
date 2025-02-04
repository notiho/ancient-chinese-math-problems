"""
假令有句股相乘冪四千三十六五分之□，股少於弦六五分之一。問：弦多少？。
答曰：弦 a 。
"""

"""
This is a classic problem involving the Pythagorean theorem. The problem states that the product of the two legs (the "句" and "股") of a right triangle is given, and the difference between the hypotenuse ("弦") and one of the legs is also given. We are tasked with finding the hypotenuse.

Let's break it down step by step:

---

### Problem:
- The product of the two legs of the triangle is \( 4036 \frac{1}{5} = \frac{20181}{5} \).
- The difference between the hypotenuse and one of the legs is \( \frac{1}{5} \).
- Find the hypotenuse.

---

### Solution in Python:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
product_of_legs = Fraction(20181, 5)  # 4036 1/5 as a fraction
difference_between_hypotenuse_and_leg = Fraction(1, 5)  # 1/5

# Let the hypotenuse be "c", one leg be "b", and the other leg be "a".
# From the problem:
# c = b + 1/5
# a * b = 4036 1/5

# Substitute c = b + 1/5 into the Pythagorean theorem:
# c^2 = a^2 + b^2
# (b + 1/5)^2 = a^2 + b^2
# Expand:
# b^2 + 2(b)(1/5) + (1/5)^2 = a^2 + b^2
# Simplify:
# 2(b)(1/5) + (1/5)^2 = a^2
# a^2 = (2/5)b + 1/25

# From the product of the legs:
# a * b = 4036 1/5
# a = (4036 1/5) / b
# a = (20181 / 5) / b

# Substitute a into a^2:
# [(20181 / 5) / b]^2 = (2/5)b + 1/25
# Solve for b.

# Step 1: Express a^2 in terms of b
a_squared = lambda b: (Fraction(20181, 5) / b) ** 2

# Step 2: Express the right-hand side of the equation
rhs = lambda b: (Fraction(2, 5) * b) + Fraction(1, 25)

# Step 3: Solve for b where a^2 = rhs
from math import isclose

b = Fraction(1)  # Start with an initial guess for b
while True:
    if isclose(float(a_squared(b)), float(rhs(b)), rel_tol=1e-9):
        break
    b += Fraction(1, 1000)  # Increment b in small steps

# Step 4: Calculate c (the hypotenuse)
c = b + Fraction(1, 5)

# Final answer
a = c
print(f"The hypotenuse (弦) is: {a}")
#----- content ends here -----


"""


---

### Explanation:
1. The problem uses the Pythagorean theorem and the relationship between the hypotenuse and one of the legs.
2. We substitute the given conditions into the equations and solve for the unknowns.
3. The solution involves iteratively solving for \( b \) (one of the legs) and then calculating \( c \) (the hypotenuse).

Let me know if you'd like further clarification!
"""


"""
Timed out"""
