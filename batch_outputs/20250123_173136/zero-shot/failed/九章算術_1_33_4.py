"""
又有宛田，下周九十九步，徑五十一步。問：為田幾何？
術曰：以徑乘周，四而一。
荅曰： a畝 。
"""

"""
To solve this problem, we need to calculate the area of a circular field (田). The problem states that the circumference (周) is 99 steps and the diameter (徑) is 51 steps. The formula provided is to multiply the diameter by the circumference and then divide the result by 4.

Here is the Python code to compute the area:


"""


from fractions import Fraction

# Given values
circumference = 99  # 周 (steps)
diameter = 51       # 徑 (steps)

# Formula: (diameter * circumference) / 4
a = Fraction(diameter * circumference, 4)

# The area of the field in 畝
a  # Output in 畝


"""


The variable `a` will contain the area of the field in 畝.
"""


"""
Variable 'a' has wrong value. Expected: 1683/320, Actual: 5049/4"""
