"""
又有環田，中周六十二步、四分步之三，外周一百一十三步、二分步之一，徑十二步、三分步之二。問：為田幾何？
術曰：并中外周而半之，以徑乘之為積步。
荅曰： a畝 。
"""

"""
To solve this problem, we need to calculate the area of a circular field using the given dimensions. The formula provided in the problem is to take the average of the inner and outer circumferences, multiply it by the diameter, and then divide by 2 to get the area in "步". Finally, we convert the result into "畝".

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
inner_circumference = Fraction(62) + Fraction(3, 4)  # 中周六十二步、四分步之三
outer_circumference = Fraction(113) + Fraction(1, 2)  # 外周一百一十三步、二分步之一
diameter = Fraction(12) + Fraction(2, 3)  # 徑十二步、三分步之二

# Calculate the area in "步"
average_circumference = (inner_circumference + outer_circumference) / 2
area_in_bu = average_circumference * diameter / 2

# Convert "步" to "畝" (1 畝 = 240 步)
a = area_in_bu / 240

# Result
a  # The area in 畝
#----- content ends here -----


"""


This code calculates the area of the field in "畝" and stores the result in the variable `a`.
"""


"""
Variable 'a' has wrong value. Expected: 893/192, Actual: 893/384"""
