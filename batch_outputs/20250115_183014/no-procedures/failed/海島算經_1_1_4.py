"""
今有望松生山上，不知高下。立兩表齊，高二丈，前後相去五十步，令後表與前表參相直。從前表卻行七步四尺，薄地遙望松末，與表端參合。又望松本，入表二尺八寸。复從後表卻行八步五尺，薄地遙望松末，亦與表端參合。問松高及山去表各幾何？
答曰：松高 a丈 ；山去表 b里 。
"""

"""
This is a classic ancient Chinese surveying problem that involves using similar triangles to calculate the height of a tree (松高) and the distance from the tree to the measurement point (山去表). Let's break it down step by step and translate it into Python code.

---

### Problem Setup:
1. Two poles (表) are erected, each 2 丈 tall.
2. The distance between the two poles is 50 步.
3. Observations are made from two positions:
   - From the front pole, stepping back 7 步 4 尺 (7.4 步), the top of the tree aligns with the top of the pole, and the base of the tree aligns with a point 2 尺 8 寸 (2.8 尺) above the ground.
   - From the back pole, stepping back 8 步 5 尺 (8.5 步), the top of the tree again aligns with the top of the pole.

We are tasked with finding:
- The height of the tree (松高, `a` 丈).
- The horizontal distance from the tree to the front pole (山去表, `b` 里).

---

### Assumptions and Conversions:
1. 1 丈 = 10 尺.
2. 1 步 = 6 尺.
3. 1 里 = 300 步.

---

### Solution:
We use similar triangles to solve for the height of the tree and the horizontal distance. Here's the Python code:


"""


from fractions import Fraction

# Constants
丈_to_尺 = 10  # 1 丈 = 10 尺
步_to_尺 = 6    # 1 步 = 6 尺
里_to_步 = 300  # 1 里 = 300 步

# Pole height
pole_height = 2 * 丈_to_尺  # 2 丈 = 20 尺

# Distances
distance_between_poles = 50 * 步_to_尺  # 50 步 = 300 尺
front_observation_distance = 7 + Fraction(4, 10)  # 7 步 4 尺 = 7.4 步
front_observation_distance_in_尺 = front_observation_distance * 步_to_尺  # Convert to 尺
front_base_offset = 2 + Fraction(8, 10)  # 2 尺 8 寸 = 2.8 尺

back_observation_distance = 8 + Fraction(5, 10)  # 8 步 5 尺 = 8.5 步
back_observation_distance_in_尺 = back_observation_distance * 步_to_尺  # Convert to 尺

# Step 1: Calculate the height of the tree (松高)
# Using similar triangles from the front observation
tree_height = pole_height * front_observation_distance_in_尺 / front_base_offset

# Step 2: Calculate the horizontal distance from the tree to the front pole (山去表)
# Using similar triangles from the back observation
tree_to_pole_distance = (tree_height * distance_between_poles) / (tree_height - pole_height)

# Convert the horizontal distance to 里
tree_to_pole_distance_in_里 = tree_to_pole_distance / (里_to_步 * 步_to_尺)

# Convert the tree height back to 丈
tree_height_in_丈 = tree_height / 丈_to_尺

# Results
a = tree_height_in_丈  # 松高 in 丈
b = tree_to_pole_distance_in_里  # 山去表 in 里

# Output the results
a, b


"""


---

### Explanation of the Code:
1. **Tree Height (松高):**
   - From the front observation, we use the ratio of the pole height to the distance from the observer to the base offset to calculate the tree height using similar triangles.

2. **Horizontal Distance (山去表):**
   - From the back observation, we use the ratio of the tree height to the difference in height between the tree and the pole to calculate the horizontal distance using similar triangles.

3. **Unit Conversions:**
   - All calculations are performed in 尺, and the final results are converted to 丈 for the tree height and 里 for the horizontal distance.

---

### Final Answer:
- 松高 `a` 丈.
- 山去表 `b` 里.
"""


"""
Variable 'a' has wrong value. Expected: 307/25, Actual: 222/7
Variable 'b' has wrong value. Expected: 23/21, Actual: 37/208"""
