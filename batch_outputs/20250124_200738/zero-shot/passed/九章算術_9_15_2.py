"""
今有句八步，股十五步。問︰句中容圓，徑幾何？
術曰：八步為句，十五步為股，為之求弦。三位并之為法，以句乘股，倍之為實。實如法得徑一步。
荅曰： a步 。
"""

"""
To solve this problem, we are dealing with a right triangle where the lengths of the two legs are given (句 = 8 steps, 股 = 15 steps). We are tasked with finding the diameter of the circle that can be inscribed in this triangle. The solution involves calculating the hypotenuse (弦) and then determining the diameter of the inscribed circle.

Here is the Python code to compute the answer:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
句 = Fraction(8)  # 8 steps
股 = Fraction(15)  # 15 steps

# Calculate the hypotenuse (弦) using the Pythagorean theorem
弦 = (句**2 + 股**2)**0.5

# Calculate the area of the triangle
area = (句 * 股) / 2

# Calculate the semi-perimeter of the triangle
semi_perimeter = (句 + 股 + 弦) / 2

# Calculate the radius of the inscribed circle
radius = area / semi_perimeter

# The diameter of the inscribed circle is twice the radius
a = radius * 2

# Output the result
a  # Diameter of the inscribed circle in steps
#----- content ends here -----


"""


The variable `a` will contain the diameter of the inscribed circle in steps.
"""


"""
"""
