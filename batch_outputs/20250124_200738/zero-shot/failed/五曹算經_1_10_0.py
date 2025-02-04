"""
今有田桑生中央從隅至桑一百四十七步。問：為田㡬何？
術曰：列一百四十七步以二乘之得二百九十四步以五乘之得一千四百七十步以七除之得二百一十步自相乘得四萬四千一百步以畝法除之即得。
答曰： a頃 奇 b步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the area of a field based on the given steps and the method described. The answer is expressed in terms of "頃" (qing) and "步" (bu), which are traditional Chinese units of area.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
steps = 147

# Calculations
double_steps = steps * 2
five_times_double_steps = double_steps * 5
seven_division = Fraction(five_times_double_steps, 7)
area_in_bu = seven_division ** 2

# Conversion to "頃" and "步"
# 1 頃 = 10000 步
a = area_in_bu // 10000  # Number of "頃"
b = area_in_bu % 10000   # Remaining "步"

# Results
a = int(a)  # Convert to integer for "頃"
b = int(b)  # Convert to integer for "步"
#----- content ends here -----


"""


After running this code, the variables `a` and `b` will contain the values of the area in "頃" and "步," respectively.
"""


"""
Variable 'a' has wrong value. Expected: 183/100, Actual: 4
Variable 'b' has wrong value. Expected: 180, Actual: 4100"""
