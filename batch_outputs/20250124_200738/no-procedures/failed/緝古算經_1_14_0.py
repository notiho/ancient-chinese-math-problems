"""
假令有句股相乘冪七百六十五分之一，弦多於句三十六十分之九。問：三事各多少？
答曰：句 a ，股 b ，弦 c 。
"""

"""
This is a classic problem involving a right triangle, where the relationship between the sides (the legs and the hypotenuse) is governed by the Pythagorean theorem. Let's break it down step by step:

### Problem Breakdown:
1. The product of the two legs (the "句" and "股") is given as \( \frac{1}{765} \).
2. The hypotenuse ("弦") is longer than one leg ("句") by \( \frac{9}{36} = \frac{1}{4} \).
3. We need to find the values of the three sides: \( \text{句} = a \), \( \text{股} = b \), and \( \text{弦} = c \).

### Solution:
Using the Pythagorean theorem:
\[
c^2 = a^2 + b^2
\]

We also know:
\[
a \cdot b = \frac{1}{765}
\]
\[
c = a + \frac{1}{4}
\]

We will solve this step by step in Python:


"""

#----- content starts here -----

from fractions import Fraction
from math import sqrt

# Given values
product_of_legs = Fraction(1, 765)  # a * b = 1/765
difference_between_c_and_a = Fraction(1, 4)  # c = a + 1/4

# Solve for a, b, and c
# Let a = x, b = product_of_legs / x, and c = a + 1/4
# Using the Pythagorean theorem: c^2 = a^2 + b^2

def solve_triangle():
    for a in range(1, 1000):  # Iterate over possible values for a
        a = Fraction(a, 1000)  # Convert to fraction for precision
        b = product_of_legs / a  # Calculate b
        c = a + difference_between_c_and_a  # Calculate c
        # Check if it satisfies the Pythagorean theorem
        if c**2 == a**2 + b**2:
            return a, b, c

# Get the solution
a, b, c = solve_triangle()

# Output the results
a, b, c
#----- content ends here -----


"""


### Explanation of the Code:
1. We iterate over possible values for \( a \) (the first leg) as fractions.
2. For each \( a \), we calculate \( b \) using the given product \( a \cdot b = \frac{1}{765} \).
3. We calculate \( c \) using the relationship \( c = a + \frac{1}{4} \).
4. We check if the Pythagorean theorem holds: \( c^2 = a^2 + b^2 \).
5. Once the condition is satisfied, we return the values of \( a \), \( b \), and \( c \).

### Final Answer:
The values of \( \text{句} = a \), \( \text{股} = b \), and \( \text{弦} = c \) will be computed by the code.
"""


"""
Code error: cannot unpack non-iterable NoneType object"""
