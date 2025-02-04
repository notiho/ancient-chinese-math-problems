"""
今有腰鼓田從八十二步两頭各廣三十步中央廣十二步。問：為田㡬何？
術曰：并三廣得七十二步以三除之得二十四步以從八十二步乘之得一千九百六十八步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem describes a trapezoidal field with two parallel sides (bases) of lengths 30 steps and 12 steps, and a height of 82 steps. The goal is to calculate the area of the field in terms of "畝" (mu) and remaining "步" (steps).

Here is the Python code:


"""


from fractions import Fraction

# Given dimensions
base1 = 30  # steps
base2 = 12  # steps
height = 82  # steps

# Step 1: Calculate the average width of the trapezoid
average_width = Fraction(base1 + base2, 2)

# Step 2: Calculate the area in square steps
area_steps = average_width * height

# Step 3: Convert the area into 畝 and 步
# 1 畝 = 240 步
mu = area_steps // 240  # Integer part (畝)
remaining_steps = area_steps % 240  # Remainder (步)

# Assign the results to variables
a = mu
b = remaining_steps

# Results
a, b


"""


### Explanation:
1. The formula for the area of a trapezoid is:
   \[
   \text{Area} = \frac{\text{Base1} + \text{Base2}}{2} \times \text{Height}
   \]
   This is implemented in Step 1 and Step 2.

2. The area is then converted into "畝" and "步". Since 1 畝 = 240 步, we use integer division (`//`) to find the number of 畝 and the modulo operator (`%`) to find the remaining 步.

### Output:
The variables `a` and `b` will contain the number of 畝 and 步, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 8, Actual: 7
Variable 'b' has wrong value. Expected: 48, Actual: 42"""
