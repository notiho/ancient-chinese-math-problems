"""
今有鼓田两頭各廣四十步中央廣五十二步從八十五步。問：為田㡬何？
術曰：并三廣得一百三十二步以三除之得四十四步以從八十五步乘之得三千七百四十步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves a trapezoidal field where the two parallel sides are 40 steps and 52 steps wide, and the height (distance between the parallel sides) is 85 steps. The goal is to calculate the area of the field in terms of "a 畝" (mu) and "b 步" (steps).

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions of the trapezoidal field
side1 = 40  # steps
side2 = 52  # steps
height = 85  # steps

# Step 1: Calculate the average width of the trapezoid
average_width = Fraction(side1 + side2, 2)

# Step 2: Calculate the area in square steps
area_in_steps = average_width * height

# Step 3: Convert the area into 畝 (1 畝 = 240 square steps)
a = area_in_steps // 240  # Whole 畝
b = area_in_steps % 240   # Remaining steps

# The solution is stored in variables 'a' (畝) and 'b' (步)
#----- content ends here -----


"""


### Explanation:
1. The average width of the trapezoid is calculated as the sum of the two parallel sides divided by 2.
2. The area in square steps is calculated by multiplying the average width by the height.
3. The area is then converted into 畝 and 步 using the conversion factor (1 畝 = 240 square steps).

### Final Answer:
The values of `a` (畝) and `b` (步) will contain the solution.
"""


"""
Variable 'a' has wrong value. Expected: 15, Actual: 16
Variable 'b' has wrong value. Expected: 140, Actual: 70"""
