"""
又有圭田廣五步、二分步之一，從八步、三分步之二。問：為田幾何？
術曰：半廣以乘正從。
荅曰： a步 。
"""

"""
To solve this problem, we need to calculate the area of the field (田). The problem gives us the dimensions of the field: the width (廣) is \(5\) steps plus \( \frac{1}{2} \) step, and the length (正) is \(8\) steps plus \( \frac{2}{3} \) step. The formula for the area is:

\[
\text{Area} = \text{Width} \times \text{Length}
\]

Here is the Python code to compute the area:


"""

#----- content starts here -----

from fractions import Fraction

# Dimensions of the field
width = 5 + Fraction(1, 2)  # 5 steps + 1/2 step
length = 8 + Fraction(2, 3)  # 8 steps + 2/3 step

# Calculate the area
a = width * length

# a is the area in steps^2
#----- content ends here -----


"""


The variable `a` will contain the area of the field in square steps.
"""


"""
Variable 'a' has wrong value. Expected: 143/6, Actual: 143/3"""
