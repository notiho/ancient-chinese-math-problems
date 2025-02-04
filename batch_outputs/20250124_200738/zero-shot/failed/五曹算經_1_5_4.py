"""
今有鼓田两頭各廣四十步中央廣五十二步從八十五步。問：為田㡬何？
術曰：并三廣得一百三十二步以三除之得四十四步以從八十五步乘之得三千七百四十步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem describes a trapezoidal field where the two parallel sides are 40 steps and 52 steps wide, and the height (distance between the parallel sides) is 85 steps. The goal is to calculate the area of the field in terms of "畝" (a traditional Chinese unit of area) and "步" (steps).

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
side1 = 40  # width of one parallel side in steps
side2 = 52  # width of the other parallel side in steps
height = 85  # distance between the parallel sides in steps
mu_conversion = 240  # 1 畝 = 240 square steps

# Step 1: Calculate the average width of the trapezoid
average_width = Fraction(side1 + side2, 2)

# Step 2: Calculate the area in square steps
area_steps = average_width * height

# Step 3: Convert the area into 畝 and remaining steps
a = area_steps // mu_conversion  # Whole 畝
b = area_steps % mu_conversion  # Remaining steps

# The results are stored in variables a (畝) and b (步)
#----- content ends here -----


"""


### Explanation of the Code:
1. **Average Width**: The average width of the trapezoid is calculated as the sum of the two parallel sides divided by 2.
2. **Area in Steps**: The area of the trapezoid is calculated as the average width multiplied by the height.
3. **Conversion to 畝 and 步**: The area in square steps is converted into 畝 (whole units) and remaining 步 (steps) using integer division (`//`) and modulo (`%`).

### Final Answer:
The variables `a` and `b` contain the solution:
- `a` is the number of 畝.
- `b` is the remaining number of 步.
"""


"""
Variable 'a' has wrong value. Expected: 15, Actual: 16
Variable 'b' has wrong value. Expected: 140, Actual: 70"""
