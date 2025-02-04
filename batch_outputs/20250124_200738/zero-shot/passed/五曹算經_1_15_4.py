"""
今有田形如牛角從五十步口廣二十步。問：為田㡬何？
術曰：列口廣二十步半之得十步以從五十步乘之得五百步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
To solve the problem, let's translate the ancient Chinese math problem into Python code. The problem describes a field shaped like a cow's horn, with a width of 20 steps at the mouth and a length of 50 steps. The area of the field is calculated using the formula provided in the text.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
mouth_width = 20  # steps
length = 50  # steps

# Calculation
half_width = Fraction(mouth_width, 2)  # 半之得十步
area_steps = half_width * length  # 以從五十步乘之得五百步

# Conversion to 畝 (1 畝 = 240 steps)
a = area_steps // 240  # 畝
b = area_steps % 240  # 奇步

# Results
a, b
#----- content ends here -----


"""


This code calculates the area of the field in terms of 畝 and 奇步. The values of `a` and `b` will contain the solution.
"""


"""
"""
