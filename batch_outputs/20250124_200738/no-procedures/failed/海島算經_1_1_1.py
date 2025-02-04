"""
今有望松生山上，不知高下。立兩表齊，高二丈，前後相去五十步，令後表與前表參相直。從前表卻行七步四尺，薄地遙望松末，與表端參合。又望松本，入表二尺八寸。复從後表卻行八步五尺，薄地遙望松末，亦與表端參合。問松高及山去表各幾何？
答曰：松高 a丈 ；山去表 b里 。
"""

"""
This is a classic ancient Chinese surveying problem involving similar triangles. The goal is to calculate the height of the pine tree (松高) and the distance from the base of the mountain to the reference point (山去表). Let's break it down step by step and translate it into Python code.

---

### Problem Breakdown:
1. Two poles (表) are erected, each 2 丈 tall.
2. The distance between the two poles is 50 步.
3. Observations are made from two positions:
   - From the first pole, stepping back 7 步 4 尺, the top of the pine tree aligns with the top of the pole, and the base of the pine tree aligns 2 尺 8 寸 inside the pole.
   - From the second pole, stepping back 8 步 5 尺, the top of the pine tree aligns with the top of the pole.

We need to calculate:
- The height of the pine tree (松高, `a`).
- The distance from the base of the mountain to the first pole (山去表, `b`).

---

### Assumptions:
1 丈 = 10 尺  
1 步 = 6 尺  
1 里 = 300 步  

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Constants
pole_height = 2 * 10  # 2 丈 = 20 尺
distance_between_poles = 50 * 6  # 50 步 = 300 尺

# Observations
obs1_back = 7 * 6 + 4  # 7 步 4 尺 = 46 尺
obs1_base_offset = 2 + Fraction(8, 10)  # 2 尺 8 寸 = 2.8 尺
obs2_back = 8 * 6 + 5  # 8 步 5 尺 = 53 尺

# Step 1: Calculate the height of the pine tree (松高, a)
# Using similar triangles for the first observation:
# (松高 - pole_height) / (distance_to_tree + obs1_base_offset) = pole_height / obs1_back
# Let distance_to_tree = x
# (松高 - 20) / (x + 2.8) = 20 / 46
# 松高 = 20 + (20 / 46) * (x + 2.8)

# Using similar triangles for the second observation:
# (松高 - pole_height) / (distance_to_tree + distance_between_poles) = pole_height / obs2_back
# (松高 - 20) / (x + 300) = 20 / 53
# 松高 = 20 + (20 / 53) * (x + 300)

# Solve for x (distance_to_tree) by equating the two expressions for 松高:
# 20 + (20 / 46) * (x + 2.8) = 20 + (20 / 53) * (x + 300)

# Simplify:
# (20 / 46) * (x + 2.8) = (20 / 53) * (x + 300)
# (10 / 23) * (x + 2.8) = (20 / 53) * (x + 300)

# Expand:
# (10 / 23) * x + (10 / 23) * 2.8 = (20 / 53) * x + (20 / 53) * 300

# Combine like terms:
# (10 / 23) * x - (20 / 53) * x = (20 / 53) * 300 - (10 / 23) * 2.8

# Solve for x:
left_coefficient = Fraction(10, 23) - Fraction(20, 53)
right_constant = (Fraction(20, 53) * 300) - (Fraction(10, 23) * Fraction(28, 10))
distance_to_tree = right_constant / left_coefficient

# Step 2: Calculate 松高 (a)
松高 = 20 + (Fraction(20, 46) * (distance_to_tree + Fraction(28, 10)))

# Step 3: Convert distance_to_tree to 里 (b)
山去表 = distance_to_tree / (300)  # Convert 尺 to 里

# Results
a = 松高 / 10  # Convert 尺 to 丈
b = 山去表

print(f"松高 a = {a} 丈")
print(f"山去表 b = {b} 里")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Step 1:** We use the principle of similar triangles to set up two equations for the height of the pine tree (松高) based on the two observations.
2. **Step 2:** By equating the two expressions for 松高, we solve for the distance from the first pole to the base of the mountain (distance_to_tree).
3. **Step 3:** Once we have the distance, we substitute it back into one of the equations to calculate 松高.
4. **Step 4:** Convert the results into the appropriate units (丈 for height and 里 for distance).

---

### Final Answer:
The height of the pine tree (松高) is `a 丈`, and the distance from the base of the mountain to the first pole (山去表) is `b 里`.
"""


"""
Variable 'a' has wrong value. Expected: 307/25, Actual: 3042/35
Variable 'b' has wrong value. Expected: 23/21, Actual: 34129/5250"""
