"""
今有覆月田從三十步徑十步。問：為田㡬何？
術曰：列徑十步半之得五步以從三十步乘之即得。
答曰： a步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the area of a circular field (覆月田), given its diameter (徑) is 10 steps (步) and its circumference (從) is 30 steps (步). The solution involves using the formula provided in the problem.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
diameter = Fraction(10)  # 徑 = 10步
circumference = Fraction(30)  # 從 = 30步

# Calculation
radius = diameter / 2  # 半徑 = 徑 ÷ 2
a = radius * circumference  # 面積 = 半徑 × 從

# The answer is stored in variable 'a'
a  # Answer in steps²
#----- content ends here -----


"""


The variable `a` will contain the area of the field in steps².
"""


"""
"""
