"""
今有田桑生中央從隅至桑一百四十七步。問：為田㡬何？
術曰：列一百四十七步以二乘之得二百九十四步以五乘之得一千四百七十步以七除之得二百一十步自相乘得四萬四千一百步以畝法除之即得。
答曰： a頃 奇 b步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the area of a field based on the given steps and the method described.

Here is the Python code:


"""


from fractions import Fraction

# Given data
steps = 147

# Calculations
double_steps = steps * 2
five_times_steps = double_steps * 5
seven_division = Fraction(five_times_steps, 7)
area_in_steps = seven_division ** 2

# Conversion to 畝 (1 畝 = 240 步²)
area_in_mu = area_in_steps / 240

# Extracting the integer part (頃) and the fractional part (步)
a = area_in_mu.numerator // area_in_mu.denominator  # Integer part (頃)
b = area_in_mu - a  # Fractional part in 畝
b = b * 240  # Convert fractional part to 步

# Final values
a = Fraction(a)  # Convert to Fraction for consistency
b = Fraction(b)

# Results
a, b


"""


This code calculates the area of the field in terms of "頃" (a unit of area) and "步" (a smaller unit of area). The results are stored in variables `a` (for "頃") and `b` (for "步").
"""


"""
Variable 'a' has wrong value. Expected: 183/100, Actual: 183"""
