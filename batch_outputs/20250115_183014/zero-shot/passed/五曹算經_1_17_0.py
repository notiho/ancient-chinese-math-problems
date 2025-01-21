"""
今有環田外周三十步內周一十二步徑三步。問：為田㡬何？
術曰：并內外周得四十二步半之得二十一步以徑三步乘之即得。
答曰： a步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves a circular field with an outer circumference of 30 steps, an inner circumference of 12 steps, and a diameter of 3 steps. The goal is to calculate the area of the field.

Here is the Python code:


"""


from fractions import Fraction

# Given values
outer_circumference = Fraction(30)  # Outer circumference in steps
inner_circumference = Fraction(12)  # Inner circumference in steps
diameter = Fraction(3)  # Diameter in steps

# Step 1: Add the outer and inner circumferences
total_circumference = outer_circumference + inner_circumference

# Step 2: Divide the total circumference by 2 to get the average circumference
average_circumference = total_circumference / 2

# Step 3: Multiply the average circumference by the diameter to get the area
a = average_circumference * diameter

# The area of the field is stored in variable 'a'


"""


The solution is stored in the variable `a` as a fraction in steps squared.
"""


"""
"""
