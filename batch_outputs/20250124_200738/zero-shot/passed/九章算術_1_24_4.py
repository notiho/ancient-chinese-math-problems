"""
今有圭田廣十二步，正從二十一步。問：為田幾何？
術曰：半廣以乘正從。
荅曰： a步 。
"""

"""
To solve this problem, we need to calculate the area of the field (田). The problem states that the width (廣) is 12 steps (步), and the length (正從) is 21 steps (步). The formula provided is to take half of the width and multiply it by the length.

Here is the Python code to compute the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
廣 = 12  # width in steps
正從 = 21  # length in steps

# Compute the area
a = Fraction(廣, 2) * 正從  # 半廣以乘正從

# The result is stored in variable 'a'
#----- content ends here -----


"""


The variable `a` will contain the area of the field in steps squared (步²).
"""


"""
"""
