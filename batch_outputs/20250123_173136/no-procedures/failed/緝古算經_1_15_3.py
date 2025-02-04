"""
假令有句股相乘冪四千三十六五分之□，股少於弦六五分之一。問：弦多少？。
答曰：弦 a 。
"""

"""
This is a classic problem in ancient Chinese mathematics involving a right triangle. The problem states:

- The product of the legs (the "ju" and "gu") of a right triangle is \( 4036 \frac{1}{5} \) (or \( \frac{20181}{5} \)).
- The shorter leg ("gu") is less than the hypotenuse ("xian") by \( \frac{1}{6} \) of the hypotenuse.
- Question: What is the length of the hypotenuse?

We will solve this step by step using Python.

---

### Python Code:


"""


from fractions import Fraction

# Given values
product_of_legs = Fraction(20181, 5)  # The product of the two legs (ju * gu)
difference_ratio = Fraction(1, 6)     # The shorter leg (gu) is less than the hypotenuse by 1/6 of the hypotenuse

# Let the hypotenuse (xian) be "a"
# Let the shorter leg (gu) be "b"
# Let the longer leg (ju) be "c"

# From the problem, we know:
# b = a - (a / 6) = (5/6) * a
# c = product_of_legs / b = product_of_legs / ((5/6) * a)

# Using the Pythagorean theorem:
# a^2 = b^2 + c^2
# Substituting b and c:
# a^2 = ((5/6) * a)^2 + (product_of_legs / ((5/6) * a))^2

# Simplify the equation:
# a^2 = (25/36) * a^2 + (product_of_legs^2 / ((5/6) * a)^2)

# Solve for "a" (the hypotenuse)

# Step 1: Define the equation
def find_hypotenuse():
    for a in range(1, 10000):  # Iterate over possible integer values of the hypotenuse
        a = Fraction(a)
        b = (5 / 6) * a
        c = product_of_legs / b
        if a**2 == b**2 + c**2:
            return a

# Step 2: Solve for the hypotenuse
a = find_hypotenuse()

# Output the result
a


"""


---

### Explanation:

1. **Define Variables**:
   - The hypotenuse is denoted as \( a \).
   - The shorter leg \( b \) is \( \frac{5}{6} \) of the hypotenuse.
   - The longer leg \( c \) is calculated as \( \frac{\text{product of legs}}{b} \).

2. **Pythagorean Theorem**:
   - Using the Pythagorean theorem \( a^2 = b^2 + c^2 \), substitute \( b \) and \( c \) in terms of \( a \).

3. **Iterative Solution**:
   - Since the problem involves fractions, we iterate over possible integer values of \( a \) (the hypotenuse) and check if the equation holds.

4. **Output**:
   - The solution gives the hypotenuse \( a \) as a fraction or integer.

Let me know if you'd like me to compute the exact numerical result!
"""


"""
Variable 'a' has wrong value. Expected: 1147/10, Actual: None"""
