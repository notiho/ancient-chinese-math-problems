"""
今有鼓田两頭各廣四十步中央廣五十二步從八十五步。問：為田㡬何？
術曰：并三廣得一百三十二步以三除之得四十四步以從八十五步乘之得三千七百四十步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem describes a trapezoidal field with two parallel sides of 40 steps and 52 steps, a height of 85 steps, and asks for the area in terms of "畝" (mu) and remaining "步" (steps).

Here is the Python code:


"""


from fractions import Fraction

# Dimensions of the trapezoidal field
short_side = 40  # steps
long_side = 52   # steps
height = 85      # steps

# Calculate the average width
average_width = Fraction(short_side + long_side, 2)

# Calculate the area in square steps
area_steps = average_width * height

# Conversion factor: 240 square steps = 1 畝
mu_conversion = 240

# Calculate the area in 畝 and remaining steps
a = area_steps // mu_conversion  # Whole 畝
b = area_steps % mu_conversion   # Remaining steps

# Output the results
a, b


"""


### Explanation:
1. The average width of the trapezoid is calculated as the average of the two parallel sides: `(40 + 52) / 2`.
2. The area in square steps is then calculated as `average_width * height`.
3. Since 1 畝 equals 240 square steps, we divide the total area by 240 to find the whole number of 畝 (`a`) and the remainder in steps (`b`).

### Solution:
The variables `a` and `b` will contain the number of 畝 and remaining steps, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 15, Actual: 16
Variable 'b' has wrong value. Expected: 140, Actual: 70"""
