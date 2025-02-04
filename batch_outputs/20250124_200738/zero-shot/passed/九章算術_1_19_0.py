"""
又有田廣九分步之七，從十一分步之九。問：為田幾何？
乘分術曰：母相乘為法，子相乘為實，實如法而一。
荅曰： a步 。
"""

"""
To solve this problem, we need to calculate the area of the field (田). The problem states that the field's dimensions are given as fractions of steps (步). Specifically:

- The width of the field is \( \frac{7}{9} \) of a step.
- The length of the field is \( \frac{9}{11} \) of a step.

The area of the field is calculated by multiplying the width by the length. Using the "乘分術" (multiplication of fractions), the rule is:

1. Multiply the numerators (子) of the fractions to get the numerator of the result.
2. Multiply the denominators (母) of the fractions to get the denominator of the result.
3. Simplify the fraction if necessary.

Here is the Python code to compute the area:


"""

#----- content starts here -----

from fractions import Fraction

# Dimensions of the field
width = Fraction(7, 9)  # 7/9 of a step
length = Fraction(9, 11)  # 9/11 of a step

# Calculate the area
a = width * length  # Area in square steps

# The result is stored in the variable 'a'
#----- content ends here -----


"""


The variable `a` now contains the area of the field in square steps as a `Fraction`.
"""


"""
"""
