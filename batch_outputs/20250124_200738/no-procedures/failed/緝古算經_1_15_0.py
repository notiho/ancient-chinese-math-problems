"""
假令有句股相乘冪四千三十六五分之□，股少於弦六五分之一。問：弦多少？。
答曰：弦 a 。
"""

"""
This is a classic problem involving the Pythagorean theorem. The problem states that the product of the two legs (the "句" and "股") of a right triangle is given, and the difference between the hypotenuse ("弦") and one of the legs is also given. The goal is to find the hypotenuse.

Let's break it down step by step and solve it.

---

### Problem:
- The product of the two legs (句股相乘) is \( 4036 \frac{1}{5} \), or \( \frac{20181}{5} \).
- The shorter leg (股) is \( \frac{1}{5} \) less than the hypotenuse (弦).
- Find the hypotenuse (弦).

---

### Solution in Python:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
product_of_legs = Fraction(20181, 5)  # 4036 1/5 as a fraction
difference_between_hypotenuse_and_leg = Fraction(1, 5)  # 股少於弦 1/5

# Let the hypotenuse (弦) be x
# Then the shorter leg (股) is x - 1/5
# Let the longer leg (句) be y
# From the problem, we know 股 * 句 = 4036 1/5
# 股 = x - 1/5, so:
# (x - 1/5) * y = 4036 1/5
# y = (4036 1/5) / (x - 1/5)

# Using the Pythagorean theorem:
# 股^2 + 句^2 = 弦^2
# (x - 1/5)^2 + y^2 = x^2

# Substitute y = (4036 1/5) / (x - 1/5) into the equation:
# (x - 1/5)^2 + [(4036 1/5) / (x - 1/5)]^2 = x^2

# Solve for x (弦)

# Step 1: Define the equation
def find_hypotenuse():
    for x in range(100, 200):  # Hypotenuse must be a reasonable positive value
        x = Fraction(x)
        shorter_leg = x - difference_between_hypotenuse_and_leg
        if shorter_leg <= 0:
            continue
        longer_leg = product_of_legs / shorter_leg
        if shorter_leg**2 + longer_leg**2 == x**2:
            return x

# Step 2: Solve for the hypotenuse
a = find_hypotenuse()
a
#----- content ends here -----


"""


---

### Explanation:
1. We use the relationship between the legs and the hypotenuse derived from the Pythagorean theorem.
2. The shorter leg is expressed in terms of the hypotenuse, and the longer leg is calculated from the given product of the legs.
3. We solve for the hypotenuse \( x \) by iterating over possible values and checking which satisfies the equation.

---

### Final Answer:
The hypotenuse \( a \) is the value returned by the function.
"""


"""
Variable 'a' has wrong value. Expected: 1147/10, Actual: None"""
