"""
今有望松生山上，不知高下。立兩表齊，高二丈，前後相去五十步，令後表與前表參相直。從前表卻行七步四尺，薄地遙望松末，與表端參合。又望松本，入表二尺八寸。复從後表卻行八步五尺，薄地遙望松末，亦與表端參合。問松高及山去表各幾何？
答曰：松高 a丈 ；山去表 b里 。
"""

"""
This is a classic ancient Chinese surveying problem involving similar triangles to calculate the height of a tree (松高) and the distance from the tree to the observation point (山去表). Let's break it down step by step and translate it into Python code.

### Problem Breakdown:
1. Two poles (表) of height 2 丈 are placed in a straight line, 50 步 apart.
2. Observations are made from two points:
   - From the first pole, stepping back 7 步 4 尺, the top of the tree aligns with the top of the pole, and the base of the tree aligns with a point 2 尺 8 寸 inside the pole.
   - From the second pole, stepping back 8 步 5 尺, the top of the tree aligns with the top of the pole.

3. Using similar triangles, we calculate:
   - The height of the tree (松高, `a`).
   - The horizontal distance from the tree to the first pole (山去表, `b`).

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Constants
表高 = 2  # Height of the pole in 丈
前後距離 = 50  # Distance between the two poles in 步

# First observation
前表退步 = 7 + Fraction(4, 10)  # 7 步 4 尺
前表入地 = 2 + Fraction(8, 10)  # 2 尺 8 寸

# Second observation
後表退步 = 8 + Fraction(5, 10)  # 8 步 5 尺

# Using similar triangles for the first observation:
# 松高 / (山去表 - 前表入地) = 表高 / 前表退步
# => 松高 = 表高 * (山去表 - 前表入地) / 前表退步

# Using similar triangles for the second observation:
# 松高 / 山去表 = 表高 / 後表退步
# => 松高 = 表高 * 山去表 / 後表退步

# Solve for 山去表 (distance to the tree):
# From the two equations:
# 表高 * (山去表 - 前表入地) / 前表退步 = 表高 * 山去表 / 後表退步
# Simplify:
# (山去表 - 前表入地) / 前表退步 = 山去表 / 後表退步
# => 後表退步 * (山去表 - 前表入地) = 前表退步 * 山去表
# => 後表退步 * 山去表 - 後表退步 * 前表入地 = 前表退步 * 山去表
# => 山去表 * (後表退步 - 前表退步) = 後表退步 * 前表入地
# => 山去表 = (後表退步 * 前表入地) / (後表退步 - 前表退步)

山去表 = (後表退步 * 前表入地) / (後表退步 - 前表退步)

# Calculate 松高 (tree height):
松高 = 表高 * 山去表 / 後表退步

# Convert 山去表 from 步 to 里 (1 里 = 300 步)
山去表_里 = 山去表 / 300

# Results
a = 松高  # Tree height in 丈
b = 山去表_里  # Distance to the tree in 里

# Output results
print(f"松高: {a} 丈")
print(f"山去表: {b} 里")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Input Values**: The heights, distances, and observations are converted into fractions to ensure precision.
2. **Similar Triangles**: The relationships between the heights and distances are derived using the properties of similar triangles.
3. **Solve for Distance**: The distance to the tree (山去表) is calculated by solving the system of equations derived from the two observations.
4. **Calculate Tree Height**: Once the distance is known, the height of the tree (松高) is calculated using one of the triangle relationships.
5. **Unit Conversion**: The distance is converted from 步 to 里 for the final answer.

---

### Example Output:
If you run the code, it will calculate the height of the tree (`a`) in 丈 and the distance to the tree (`b`) in 里.
"""


"""
Variable 'a' has wrong value. Expected: 307/25, Actual: 56/11
Variable 'b' has wrong value. Expected: 23/21, Actual: 119/1650"""
