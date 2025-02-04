"""
今有環田外周三十步內周一十二步徑三步。問：為田㡬何？
術曰：并內外周得四十二步半之得二十一步以徑三步乘之即得。
答曰： a步 。
"""

"""
To solve this problem, we need to compute the area of the ring-shaped field (環田). The problem gives us the outer circumference (外周), inner circumference (內周), and the diameter (徑). Here's the Python code to calculate the area:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
outer_circumference = Fraction(30)  # 外周三十步
inner_circumference = Fraction(12)  # 內周一十二步
diameter = Fraction(3)  # 徑三步

# Step 1: Add the outer and inner circumferences
total_circumference = outer_circumference + inner_circumference

# Step 2: Divide the total circumference by 2 to get the average circumference
average_circumference = total_circumference / 2

# Step 3: Multiply the average circumference by the diameter to get the area
a = average_circumference * diameter

# The area of the ring-shaped field is stored in variable 'a'
#----- content ends here -----


"""


The solution is stored in the variable `a` as a Fraction representing the area in square steps (步²).
"""


"""
"""
