"""
又有宛田，下周九十九步，徑五十一步。問：為田幾何？
術曰：以徑乘周，四而一。
荅曰： a畝 。
"""

"""
To solve this problem, we need to calculate the area of a circular field (田). The problem states that the circumference (周) is 99 steps and the diameter (徑) is 51 steps. The formula provided in the problem is:

**Area = (Diameter × Circumference) ÷ 4**

The result is expressed in "畝" (a traditional Chinese unit of area). Here's the Python code to compute the area:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
diameter = 51  # 徑 in steps
circumference = 99  # 周 in steps

# Formula for the area
a = Fraction(diameter * circumference, 4)

# The area in 畝
print(f"The area of the field is {a} 畝.")
#----- content ends here -----


"""


This will calculate the value of `a` in terms of 畝. The variable `a` represents the area of the field.
"""


"""
Variable 'a' has wrong value. Expected: 1683/320, Actual: 5049/4"""
