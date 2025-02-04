"""
今有邱田周六百四十步徑三百八十步。問：為田㡬何？
術曰：列周六百四十步半之得三百二十步又列徑三百八十步半之得一百九十步二位相乘得六萬八百步以畝法除之即得。
答曰： a頃 奇 b步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the area of a field given its perimeter (周) and diameter (徑). The solution involves dividing the perimeter and diameter by 2, multiplying the results, and then converting the area into the appropriate units of "頃" and "步".

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
周 = 640  # Perimeter in steps
徑 = 380  # Diameter in steps

# Calculations
半周 = 周 / 2  # Half of the perimeter
半徑 = 徑 / 2  # Half of the diameter
面積 = 半周 * 半徑  # Area in square steps

# Conversion to "頃" and "步"
# 1 頃 = 240 步 * 240 步 = 57600 square steps
畝法 = 57600  # Conversion factor for 1 頃 in square steps
a = 面積 // 畝法  # Integer part of the area in "頃"
b = 面積 % 畝法  # Remainder in square steps

# Results
a = Fraction(a)  # Area in "頃"
b = Fraction(b)  # Remaining area in "步"
#----- content ends here -----


"""


The variables `a` and `b` will contain the solution: `a` is the number of "頃" (integer part), and `b` is the remaining area in square steps.
"""


"""
Variable 'a' has wrong value. Expected: 253/100, Actual: 1
Variable 'b' has wrong value. Expected: 80, Actual: 3200"""
