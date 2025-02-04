"""
今有邱田周六百三十九，步徑三百八十步。問：為田幾何？
術曰：半周得三百一十九步五分半徑，得一百九十步二位相乘，得六萬七百五步，以畝法除之，即得。
答曰： a頃 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the area of a circular field (邱田) given its circumference (周) and diameter (步徑). The area is then converted into a unit of measurement called "頃" (qing). Here's the Python code:


"""


from fractions import Fraction

# Given data
circumference = 639  # 周 (in 步)
diameter = 380  # 步徑 (in 步)

# Step 1: Calculate the radius
radius = Fraction(diameter, 2)  # 半徑

# Step 2: Multiply half the circumference by the radius
area_in_square_bu = Fraction(circumference, 2) * radius  # 面積 in 步^2

# Step 3: Convert the area into 畝 (1 畝 = 240 步^2)
area_in_mu = area_in_square_bu / 240

# Step 4: Convert 畝 to 頃 (1 頃 = 100 畝)
a = area_in_mu / 100  # Area in 頃

# The answer is stored in variable 'a'


"""


The variable `a` now contains the area of the field in "頃" (qing).
"""


"""
"""
