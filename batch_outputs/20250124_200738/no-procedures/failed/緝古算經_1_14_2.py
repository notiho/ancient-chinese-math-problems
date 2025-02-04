"""
假令有句股相乘冪七百六十五分之一，弦多於句三十六十分之九。問：三事各多少？
答曰：句 a ，股 b ，弦 c 。
"""

"""
This problem involves a right triangle where the product of the two legs (the "ju" and "gu") is given, and the hypotenuse ("xian") is related to one of the legs. Let's solve it step by step.

---

### Problem:
- The product of the two legs (ju and gu) is \( \frac{1}{765} \).
- The hypotenuse (xian) is \( \frac{9}{36} = \frac{1}{4} \) greater than one of the legs (ju).
- Find the values of ju (\(a\)), gu (\(b\)), and xian (\(c\)).

---

### Solution in Python:


"""

#----- content starts here -----

from fractions import Fraction
from math import sqrt

# Given values
product_of_legs = Fraction(1, 765)  # ju * gu = 1/765
xian_difference = Fraction(9, 36)   # xian - ju = 1/4

# Let ju = x, gu = y, and xian = z
# From the problem:
# 1. x * y = 1/765
# 2. z = x + 1/4
# 3. x^2 + y^2 = z^2 (Pythagorean theorem)

# Solve for y in terms of x using equation 1:
# y = (1/765) / x
def solve_triangle():
    for ju in range(1, 1000):  # Iterate over possible values for ju
        x = Fraction(1, ju)  # ju
        y = product_of_legs / x  # gu
        z = x + xian_difference  # xian

        # Check if the Pythagorean theorem holds
        if x**2 + y**2 == z**2:
            return x, y, z

# Solve for ju, gu, and xian
a, b, c = solve_triangle()

# Output the results
a, b, c
#----- content ends here -----


"""


---

### Explanation:
1. The product of the legs is used to express one leg in terms of the other.
2. The relationship between the hypotenuse and one leg is used to express the hypotenuse in terms of one leg.
3. The Pythagorean theorem is used to solve for the three sides of the triangle.

The solution will provide the values of \(a\) (ju), \(b\) (gu), and \(c\) (xian).
"""


"""
Code error: cannot unpack non-iterable NoneType object"""
