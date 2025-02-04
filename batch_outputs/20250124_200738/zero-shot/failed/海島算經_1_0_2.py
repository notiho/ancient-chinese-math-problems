"""
今有望海島，立兩表，齊高三丈，前後相去千步，令後表與前表參相直。從前表卻行一百二十三步，人目著地取望島峯，與表末參合。從後表卻行一百二十七步，人目著地取望島峯，亦與表末參合。問島高及去表各幾何？
術曰：以表高乘表間為實；相多為法，除之。所得加表高，即得島高。求前表去島遠近者：以前表卻行乘表間為實；相多為法。除之，得島去表數。
答曰：島高 a里 ；去表 b里 。
"""

"""
To solve the problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the height of the island (`a`) and the distance from the island to the front pole (`b`). We'll use the `Fraction` class to ensure precise calculations.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
pole_height = Fraction(3)  # height of the poles in 丈
distance_between_poles = Fraction(1000)  # distance between the two poles in 步
front_pole_retreat = Fraction(123)  # steps retreated from the front pole
back_pole_retreat = Fraction(127)  # steps retreated from the back pole

# Calculations
# Step 1: Calculate the height of the island (a)
numerator_a = pole_height * distance_between_poles  # 表高乘表間為實
denominator_a = back_pole_retreat - front_pole_retreat  # 相多為法
a = numerator_a / denominator_a + pole_height  # 所得加表高，即得島高

# Step 2: Calculate the distance from the island to the front pole (b)
numerator_b = front_pole_retreat * distance_between_poles  # 前表卻行乘表間為實
denominator_b = back_pole_retreat - front_pole_retreat  # 相多為法
b = numerator_b / denominator_b  # 除之，得島去表數

# Results
a  # Island height in 丈
b  # Distance from the island to the front pole in 步
#----- content ends here -----


"""


### Explanation of the Code:
1. **Given Data**:
   - The height of the poles is `3 丈`.
   - The distance between the two poles is `1000 步`.
   - The retreat distances are `123 步` and `127 步` for the front and back poles, respectively.

2. **Height of the Island (`a`)**:
   - Multiply the pole height by the distance between the poles to get the numerator.
   - Subtract the retreat distances to get the denominator.
   - Divide the numerator by the denominator and add the pole height to get the island height.

3. **Distance to the Front Pole (`b`)**:
   - Multiply the retreat distance from the front pole by the distance between the poles to get the numerator.
   - Use the same denominator as above.
   - Divide the numerator by the denominator to get the distance from the island to the front pole.

### Results:
- `a` is the height of the island in 丈.
- `b` is the distance from the island to the front pole in 步.
"""


"""
Variable 'a' has wrong value. Expected: 251/60, Actual: 753
Variable 'b' has wrong value. Expected: 205/2, Actual: 30750"""
