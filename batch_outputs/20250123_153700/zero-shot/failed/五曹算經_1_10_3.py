"""
今有田桑生中央從隅至桑一百四十七步。問：為田㡬何？
術曰：列一百四十七步以二乘之得二百九十四步以五乘之得一千四百七十步以七除之得二百一十步自相乘得四萬四千一百步以畝法除之即得。
答曰： a頃 奇 b步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the area of a field given the diagonal length and some specific operations. The answer is expressed in terms of "a" (the number of qing, a unit of area) and "b" (the number of steps, another unit of area).

Here is the Python code:


"""


from fractions import Fraction

# Given data
diagonal = 147  # in steps

# Calculations
double_diagonal = diagonal * 2
product_with_five = double_diagonal * 5
product_with_seven = product_with_five * 7
area_in_steps = Fraction(product_with_seven, 7) ** 2  # Square the result
area_in_mu = area_in_steps / 240  # 1 mu = 240 steps²

# Convert to qing and steps
a = area_in_mu // 100  # 1 qing = 100 mu
b = area_in_mu % 100  # Remaining mu in steps

# Results
a = int(a)  # Convert to integer for qing
b = Fraction(b)  # Keep b as a fraction for precision


"""


The variables `a` and `b` will hold the values of the area in qing and steps, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 183/100, Actual: 90
Variable 'b' has wrong value. Expected: 180, Actual: 15/4"""
