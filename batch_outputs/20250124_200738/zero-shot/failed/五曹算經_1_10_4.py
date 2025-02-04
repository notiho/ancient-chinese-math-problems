"""
今有田桑生中央從隅至桑一百四十七步。問：為田㡬何？
術曰：列一百四十七步以二乘之得二百九十四步以五乘之得一千四百七十步以七除之得二百一十步自相乘得四萬四千一百步以畝法除之即得。
答曰： a頃 奇 b步 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves calculating the area of a field based on the given steps and the method described. The answer is expressed in terms of "頃" (qǐng, a traditional Chinese unit of area) and "步" (bù, a smaller unit of area).

1 頃 = 24000 步.

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

# Convert the area into 頃 and 步
a = area_in_bu // 24000  # Number of 頃
b = area_in_bu % 24000   # Remaining 步

# Results
a = Fraction(a)  # Convert to Fraction for consistency
b = Fraction(b)  # Convert to Fraction for consistency
#----- content ends here -----


"""


The variables `a` and `b` will contain the values of the area in terms of 頃 and 步, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 183/100, Actual: 1
Variable 'b' has wrong value. Expected: 180, Actual: 20100"""
