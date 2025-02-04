"""
又有宛田，下周九十九步，徑五十一步。問：為田幾何？
術曰：以徑乘周，四而一。
荅曰： a畝 。
"""

"""
This ancient Chinese math problem is about calculating the area of a circular field. The problem states that the circumference ("周") is 99 steps, and the diameter ("徑") is 51 steps. The formula provided is to multiply the diameter by the circumference and then divide by 4 to calculate the area.

Here is the Python code to solve this problem:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
circumference = 99  # 周 (steps)
diameter = 51       # 徑 (steps)

# Formula: (diameter * circumference) / 4
a = Fraction(diameter * circumference, 4)  # Area in 畝 (mu)

# Result
a  # The area in 畝
#----- content ends here -----


"""


The variable `a` will store the area of the field in 畝 (mu).
"""


"""
Variable 'a' has wrong value. Expected: 1683/320, Actual: 5049/4"""
