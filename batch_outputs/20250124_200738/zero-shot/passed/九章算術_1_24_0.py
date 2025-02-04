"""
今有圭田廣十二步，正從二十一步。問：為田幾何？
術曰：半廣以乘正從。
荅曰： a步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem states that the area of a rectangular field can be calculated by taking half of the width (廣) and multiplying it by the length (正從). The width is given as 12 steps (步), and the length is given as 21 steps (步). We need to compute the area of the field.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
廣 = 12  # width in steps
正從 = 21  # length in steps

# Calculation
a = Fraction(廣, 2) * 正從  # 半廣以乘正從

# The area of the field in steps²
a  # This is the answer
#----- content ends here -----


"""


The variable `a` will contain the area of the field in steps².
"""


"""
"""
