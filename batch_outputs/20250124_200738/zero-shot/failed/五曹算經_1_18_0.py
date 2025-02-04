"""
今有田從一百步廣四十二步中有圓池周三十步徑一十步。問：池占外為田㡬何？
術曰：列從一百步以廣四十二步乘之得四千二百步為田積又列池周三十步半之得一十五步列徑一十步半之得五步二位相乘得七十五步為池積以減田積餘四千一百二十五步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
To solve this problem, we need to calculate the area of the rectangular field, subtract the area of the circular pond, and then convert the remaining area into "畝" (mu) and "步" (bu). Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Dimensions of the rectangular field
length = 100  # in 步
width = 42  # in 步

# Dimensions of the circular pond
circumference = 30  # in 步
diameter = 10  # in 步

# Calculate the area of the rectangular field
field_area = length * width  # in square 步

# Calculate the radius of the circular pond
radius = Fraction(diameter, 2)  # in 步

# Calculate the area of the circular pond
pond_area = Fraction(22, 7) * radius * radius  # using π ≈ 22/7

# Calculate the remaining area
remaining_area = field_area - pond_area  # in square 步

# Convert the remaining area into 畝 and 步
# 1 畝 = 240 square 步
a = remaining_area // 240  # number of 畝
b = remaining_area % 240  # remaining 步

# Results
a = int(a)  # 畝
b = int(b)  # 步
#----- content ends here -----


"""


The variables `a` and `b` will contain the solution in 畝 and 步, respectively.
"""


"""
Variable 'b' has wrong value. Expected: 45, Actual: 41"""
