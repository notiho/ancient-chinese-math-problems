"""
今有南望方邑，不知大小。立兩表東、西去六丈，齊人目，以索連之。令東表與邑東南隅及東北隅參相直。當東表之北卻行五步，遙望邑西北隅，入索東端二丈二尺六寸半。又卻北行去表一十三步二尺，遙望邑西北隅，適與西表相參合。問邑方及邑去表各幾何？
答曰：邑方 a里 ；邑去表 b里 。
"""

"""
This is a classic ancient Chinese surveying problem involving geometry and trigonometry. The problem describes a method to calculate the size of a square city (邑) and its distance from the observation point using measurements and sightlines.

Let's break it down and solve it step by step.

---

### Problem Setup:
1. Two poles (東表 and 西表) are placed 6 丈 apart.
2. Observations are made using a rope (索) and sightlines to the corners of the square city (邑).
3. Measurements are taken:
   - At a point 5 步 north of the eastern pole, the rope intersects the sightline to the city’s northwest corner at a distance of 2 丈 2 尺 6 寸 5 分 (2.265 丈) from the eastern pole.
   - At a point 13 步 2 尺 north of the eastern pole, the sightline to the city’s northwest corner aligns with the western pole.

We need to calculate:
- The side length of the square city (邑方, denoted as `a`).
- The distance from the poles to the city (邑去表, denoted as `b`).

---

### Assumptions and Conversions:
1. 1 丈 = 10 尺, 1 尺 = 10 寸, 1 寸 = 10 分.
2. 1 里 = 180 丈.
3. Use the given measurements and geometric relationships to solve for `a` and `b`.

---

### Solution in Python:


"""


from fractions import Fraction

# Given data
pole_distance = 6  # Distance between the two poles in 丈
rope_intersection = Fraction(2, 1) + Fraction(2, 10) + Fraction(6, 100) + Fraction(5, 1000)  # 2 丈 2 尺 6 寸 5 分 = 2.265 丈
first_observation_distance = 5  # Distance north of the eastern pole for the first observation in 步
second_observation_distance = Fraction(13, 1) + Fraction(2, 10)  # Distance north of the eastern pole for the second observation in 步

# Conversion factors
步_to_丈 = Fraction(5, 3)  # 1 步 = 5/3 丈
first_observation_distance = first_observation_distance * 步_to_丈
second_observation_distance = second_observation_distance * 步_to_丈

# Step 1: Calculate the distance from the poles to the city (b)
# Using similar triangles:
# (second_observation_distance - first_observation_distance) / pole_distance = rope_intersection / b
b = rope_intersection * pole_distance / (second_observation_distance - first_observation_distance)

# Step 2: Calculate the side length of the city (a)
# Using similar triangles:
# a / b = pole_distance / (second_observation_distance - first_observation_distance)
a = pole_distance * b / (second_observation_distance - first_observation_distance)

# Convert results to 里
丈_to_里 = Fraction(1, 180)
a_in_里 = a * 丈_to_里
b_in_里 = b * 丈_to_里

# Results
a_in_里, b_in_里


"""


---

### Explanation of the Code:
1. **Input Data**: The given measurements are converted into consistent units (丈).
2. **Geometric Relationships**: Using the principle of similar triangles, we derive formulas for `b` (distance to the city) and `a` (side length of the city).
3. **Conversion to 里**: The results are converted from 丈 to 里 for the final answer.

---

### Final Answer:
- The side length of the city (邑方) is `a_in_里` 里.
- The distance from the poles to the city (邑去表) is `b_in_里` 里.
"""


"""
Variable 'a' has wrong value. Expected: 151/48, Actual: 36693/84050
Variable 'b' has wrong value. Expected: 83/20, Actual: 4077/4100"""
