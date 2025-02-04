"""
今有圭田廣十二步，正從二十一步。問：為田幾何？
術曰：半廣以乘正從。
荅曰： a步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem states that the area of a field (田) can be calculated by taking half of the width (廣) and multiplying it by the length (正從). Let's compute the area.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
廣 = 12  # width in steps (步)
正從 = 21  # length in steps (步)

# Calculation
a = Fraction(廣, 2) * 正從  # 半廣以乘正從

# Result
a  # area in steps (步)
#----- content ends here -----


"""


The variable `a` will store the area of the field in steps (步).
"""


"""
"""
