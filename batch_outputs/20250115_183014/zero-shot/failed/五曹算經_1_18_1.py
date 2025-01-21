"""
今有田從一百步廣四十二步中有圓池周三十步徑一十步。問：池占外為田㡬何？
術曰：列從一百步以廣四十二步乘之得四千二百步為田積又列池周三十步半之得一十五步列徑一十步半之得五步二位相乘得七十五步為池積以減田積餘四千一百二十五步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
To solve this problem, we need to calculate the area of the field, subtract the area of the circular pond, and then convert the remaining area into "畝" and "步". Here's the Python code:


"""


from fractions import Fraction

# Dimensions of the field
length = 100  # in steps
width = 42  # in steps

# Dimensions of the circular pond
circumference = 30  # in steps
diameter = 10  # in steps

# Calculate the area of the field
field_area = length * width  # in square steps

# Calculate the radius of the pond
radius = Fraction(diameter, 2)  # in steps

# Calculate the area of the pond
pond_area = Fraction(22, 7) * radius * radius  # using π ≈ 22/7

# Calculate the remaining area
remaining_area = field_area - pond_area  # in square steps

# Convert the remaining area into 畝 and 步
# 1 畝 = 240 步
a = remaining_area // 240  # number of 畝
b = remaining_area % 240  # remaining 步

# Results
a = int(a)
b = Fraction(b)

# The answer is stored in variables a (畝) and b (步)


"""


### Explanation:
1. The field's area is calculated as `length * width`.
2. The pond's area is calculated using the formula for the area of a circle, \( \pi r^2 \), with \( \pi \approx \frac{22}{7} \).
3. The remaining area is the field's area minus the pond's area.
4. The remaining area is converted into "畝" and "步" using the conversion \( 1 \text{ 畝 } = 240 \text{ 步} \).

Let me know if you need further clarification!
"""


"""
Variable 'b' has wrong value. Expected: 45, Actual: 290/7"""
