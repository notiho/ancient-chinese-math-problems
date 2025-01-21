"""
今有圭田從三十步一頭廣二十四步一頭無步。問：為田㡬何？
術曰：列一頭廣二十四步半之得一十二步以從三十步乘之得三百六十步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
To solve this problem, we need to compute the area of a trapezoidal field (圭田). The field has one side (head) with a width of 24 steps, the other side with a width of 0 steps, and a length of 30 steps. The area is then converted into "畝" (Chinese unit of area) and "步" (steps).

Here is the Python code to compute the solution:


"""


from fractions import Fraction

# Given dimensions
length = 30  # in steps
width1 = 24  # in steps
width2 = 0   # in steps

# Compute the average width
average_width = Fraction(width1 + width2, 2)

# Compute the area in square steps
area_in_steps = length * average_width

# Conversion factor: 1 畝 = 240 square steps
area_in_mu = area_in_steps // 240  # integer part (畝)
remaining_steps = area_in_steps % 240  # remainder (步)

# Assign the results to variables
a = area_in_mu
b = remaining_steps

# Output the results
a, b


"""


### Explanation:
1. The average width of the trapezoid is calculated as `(width1 + width2) / 2`.
2. The area in square steps is computed as `length * average_width`.
3. The area is then converted into "畝" and "步" using the conversion factor `1 畝 = 240 square steps`.
4. The integer part of the division gives the number of "畝" (`a`), and the remainder gives the number of "步" (`b`).

### Results:
The variables `a` and `b` will contain the solution:
- `a` is the number of 畝.
- `b` is the number of 步.
"""


"""
"""
