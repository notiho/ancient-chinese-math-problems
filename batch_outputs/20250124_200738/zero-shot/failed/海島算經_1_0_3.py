"""
今有望海島，立兩表，齊高三丈，前後相去千步，令後表與前表參相直。從前表卻行一百二十三步，人目著地取望島峯，與表末參合。從後表卻行一百二十七步，人目著地取望島峯，亦與表末參合。問島高及去表各幾何？
術曰：以表高乘表間為實；相多為法，除之。所得加表高，即得島高。求前表去島遠近者：以前表卻行乘表間為實；相多為法。除之，得島去表數。
答曰：島高 a里 ；去表 b里 。
"""

"""
To solve the problem, let's translate the ancient Chinese math problem into Python code. We'll use the `Fraction` class to handle numbers that might not be integers.

### Problem Breakdown:
1. Two poles (or "表") are of equal height (3丈 each).
2. The distance between the two poles is 1000步.
3. Observations are made from two points:
   - From the first pole, 123步 away.
   - From the second pole, 127步 away.
4. The goal is to calculate:
   - The height of the island (`a` in 丈).
   - The distance from the front pole to the island (`b` in 步).

### Python Code:

"""

#----- content starts here -----

from fractions import Fraction

# Given data
pole_height = Fraction(3)  # Height of each pole in 丈
distance_between_poles = Fraction(1000)  # Distance between the two poles in 步
distance_from_first_pole = Fraction(123)  # Distance observer is from the first pole in 步
distance_from_second_pole = Fraction(127)  # Distance observer is from the second pole in 步

# Calculations
# Step 1: Calculate the height of the island (a)
numerator_a = pole_height * distance_between_poles  # 表高乘表間為實
denominator_a = distance_from_first_pole + distance_from_second_pole  # 相多為法
a = numerator_a / denominator_a + pole_height  # 所得加表高，即得島高

# Step 2: Calculate the distance from the front pole to the island (b)
numerator_b = distance_from_first_pole * distance_between_poles  # 前表卻行乘表間為實
denominator_b = distance_from_first_pole + distance_from_second_pole  # 相多為法
b = numerator_b / denominator_b  # 除之，得島去表數

# Results
a  # Height of the island in 丈
b  # Distance from the front pole to the island in 步
#----- content ends here -----


"""


### Explanation:
1. **Height of the Island (`a`)**:
   - Formula: \( a = \frac{\text{表高} \times \text{表間}}{\text{相多}} + \text{表高} \)
   - Numerator: Multiply the height of the pole by the distance between the poles.
   - Denominator: Sum the distances the observer is away from the poles.
   - Add the pole height to the result.

2. **Distance from the Front Pole to the Island (`b`)**:
   - Formula: \( b = \frac{\text{前表卻行} \times \text{表間}}{\text{相多}} \)
   - Numerator: Multiply the distance the observer is away from the first pole by the distance between the poles.
   - Denominator: Sum the distances the observer is away from the poles.

### Output:
- `a` will give the height of the island in 丈.
- `b` will give the distance from the front pole to the island in 步.
"""


"""
Variable 'a' has wrong value. Expected: 251/60, Actual: 15
Variable 'b' has wrong value. Expected: 205/2, Actual: 492"""
