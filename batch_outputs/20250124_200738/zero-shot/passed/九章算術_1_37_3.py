"""
又有環田，中周六十二步、四分步之三，外周一百一十三步、二分步之一，徑十二步、三分步之二。問：為田幾何？
術曰：并中外周而半之，以徑乘之為積步。
荅曰： a畝 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the area of a circular field based on its dimensions. Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
middle_circumference = Fraction(62) + Fraction(3, 4)  # 中周 (62步, 4分步之3)
outer_circumference = Fraction(113) + Fraction(1, 2)  # 外周 (113步, 2分步之1)
diameter = Fraction(12) + Fraction(2, 3)              # 徑 (12步, 3分步之2)

# Calculation
average_circumference = (middle_circumference + outer_circumference) / 2  # 并中外周而半之
area = average_circumference * diameter  # 以徑乘之為積步

# Convert to 畝 (1 畝 = 240 步^2)
a = area / 240

# Answer
a  # The area in 畝
#----- content ends here -----


"""


This code calculates the area of the circular field in 畝 (`a`). The values are represented as fractions to ensure precision, and the units are properly converted.
"""


"""
"""
