"""
今有圓田，周三十步，徑十步。問：為田幾何？
術曰：半周半徑相乘得積步。
荅曰： a步 。
"""

"""
To solve this problem, we need to calculate the area of a circular field. The problem states that the circumference (周) is 30 steps (步), and the diameter (徑) is 10 steps (步). The formula provided in the problem is to multiply half the circumference (半周) by the radius (半徑) to get the area.

Here is the Python code to compute the value of the unknown `a`:


"""


from fractions import Fraction

# Given values
circumference = 30  # in steps
diameter = 10  # in steps

# Calculations
radius = Fraction(diameter, 2)  # 半徑 = 徑 / 2
half_circumference = Fraction(circumference, 2)  # 半周 = 周 / 2
a = half_circumference * radius  # 面積 = 半周 * 半徑

# The answer is stored in variable 'a'


"""


The value of `a` represents the area of the circular field in steps squared (步²).
"""


"""
"""
