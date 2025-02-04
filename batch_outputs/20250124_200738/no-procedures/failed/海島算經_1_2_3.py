"""
今有南望方邑，不知大小。立兩表東、西去六丈，齊人目，以索連之。令東表與邑東南隅及東北隅參相直。當東表之北卻行五步，遙望邑西北隅，入索東端二丈二尺六寸半。又卻北行去表一十三步二尺，遙望邑西北隅，適與西表相參合。問邑方及邑去表各幾何？
答曰：邑方 a里 ；邑去表 b里 。
"""

"""
This is a classic ancient Chinese surveying problem that involves geometry and trigonometry. The problem describes a method to determine the size of a square city (邑) and its distance from a reference point using observations and measurements. Let's break it down and solve it step by step.

---

### Problem Setup:
1. Two poles (東表 and 西表) are set up 6 丈 apart (1 丈 = 10 尺).
2. A rope is stretched between the two poles.
3. Observations are made from specific points to determine the alignment of the city's corners with the poles and the rope.

---

### Variables:
- Distance between the two poles: `6 丈 = 60 尺`.
- Observations are made at two points:
  - First observation: 5 步 north of the east pole, where the rope is offset by `2 丈 2 尺 6 寸半 = 22.65 尺`.
  - Second observation: 13 步 2 尺 north of the east pole, where the alignment matches the west pole.

We need to calculate:
1. The side length of the square city (`邑方`).
2. The distance from the poles to the city (`邑去表`).

---

### Solution:

We will use the principles of similar triangles to solve this problem.


"""

#----- content starts here -----

from fractions import Fraction

# Constants
丈_to_尺 = 10  # 1 丈 = 10 尺
步_to_尺 = 6    # 1 步 = 6 尺

# Given distances
pole_distance = 6 * 丈_to_尺  # Distance between the two poles (in 尺)
offset_1 = Fraction(2 * 丈_to_尺 + 2 + Fraction(6, 10))  # Offset at first observation (in 尺)
obs_1_distance = 5 * 步_to_尺  # Distance of first observation from east pole (in 尺)
obs_2_distance = 13 * 步_to_尺 + 2  # Distance of second observation from east pole (in 尺)

# Step 1: Calculate the distance from the poles to the city (邑去表)
# Using similar triangles:
# (offset_1 / pole_distance) = (邑去表 / (obs_2_distance - obs_1_distance))
邑去表 = (offset_1 * (obs_2_distance - obs_1_distance)) / pole_distance

# Step 2: Calculate the side length of the square city (邑方)
# Using similar triangles again:
# (pole_distance / (obs_2_distance - obs_1_distance)) = (邑方 / offset_1)
邑方 = (pole_distance * offset_1) / (obs_2_distance - obs_1_distance)

# Convert results to 丈 for final answer
邑去表_in_丈 = 邑去表 / 丈_to_尺
邑方_in_丈 = 邑方 / 丈_to_尺

# Print results
邑去表_in_丈, 邑方_in_丈
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Conversion of Units**: All measurements are converted to 尺 for consistency.
2. **Similar Triangles**: The problem relies on the principle of similar triangles to relate the offsets, distances, and dimensions of the city.
3. **Final Conversion**: The results are converted back to 丈 for the final answer.

---

### Final Answer:
- The side length of the city (`邑方`) is `a 里`.
- The distance from the poles to the city (`邑去表`) is `b 里`.
"""


"""
Missing variable in output: 'a'
Missing variable in output: 'b'"""
