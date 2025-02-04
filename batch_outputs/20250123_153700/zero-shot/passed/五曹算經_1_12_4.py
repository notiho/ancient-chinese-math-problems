"""
今有箕田一頭廣八十六步一頭廣四十步從九十步。問：為田㡬何？
術曰：并二廣得一百二十六步半之得六十三步以從九十步乘之得五千六百七十步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
To solve the problem, let's translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given values
wide1 = 86  # one side of the field in steps
wide2 = 40  # the other side of the field in steps
length = 90  # the length of the field in steps

# Calculation
average_width = Fraction(wide1 + wide2, 2)  # average width
area_in_steps = average_width * length  # total area in steps
area_in_mu = area_in_steps // 240  # 1 mu = 240 steps
remaining_steps = area_in_steps % 240  # remaining steps after converting to mu

# Assigning the answers
a = area_in_mu  # number of mu
b = remaining_steps  # remaining steps

# Results
a, b


"""


This code calculates the area of the field in "mu" (畝) and remaining "steps" (步). The results are stored in variables `a` (畝) and `b` (步).
"""


"""
"""
