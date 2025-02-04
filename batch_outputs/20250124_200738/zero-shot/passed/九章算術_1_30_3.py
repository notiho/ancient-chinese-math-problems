"""
今有圓田，周三十步，徑十步。問：為田幾何？
術曰：半周半徑相乘得積步。
荅曰： a步 。
"""

"""
To solve this problem, we need to calculate the area of a circular field. The problem provides the circumference (周) as 30 steps (步) and the diameter (徑) as 10 steps (步). The formula given in the problem states that the area is calculated by multiplying half the circumference (半周) by half the diameter (半徑).

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
circumference = 30  # 周 (steps)
diameter = 10       # 徑 (steps)

# Calculations
half_circumference = Fraction(circumference, 2)  # 半周
half_diameter = Fraction(diameter, 2)           # 半徑

# Area calculation
a = half_circumference * half_diameter  # Area in steps²

# Result
a  # This is the area of the circular field in steps²
#----- content ends here -----


"""


The variable `a` will contain the area of the circular field in steps².
"""


"""
"""
