"""
今有望清淵，淵下有白石。偃矩岸上，令句高三尺。斜望水岸，入下股四尺五寸。望白石，入下股二尺四寸。又設重矩于上，其間相去四尺。更從句端斜望水岸，入上股四尺。以望白石，入上股二尺二寸。問水深幾何？
答曰： a丈 。
"""

"""
This problem involves a classic ancient Chinese mathematical technique for calculating the depth of water using geometric principles and measurements. Let's break it down and solve it step by step.

---

### Problem Setup:
1. A right triangle is formed using a measuring tool ("矩").
2. The height of the tool's vertical leg ("句") is 3 chi (尺).
3. Observations are made from the top of the tool to the water's edge and to a white stone at the bottom of the water.
4. Measurements are taken for the horizontal distances ("股") where the line of sight intersects the ground or water.

---

### Given Data:
1. **First setup:**
   - Height of the vertical leg: `3 chi`
   - Horizontal distance to the water's edge: `4 chi 5 cun` (4.5 chi)
   - Horizontal distance to the white stone: `2 chi 4 cun` (2.4 chi)

2. **Second setup (with a second measuring tool placed 4 chi away):**
   - Distance between the two tools: `4 chi`
   - Horizontal distance to the water's edge: `4 chi`
   - Horizontal distance to the white stone: `2 chi 2 cun` (2.2 chi)

---

### Goal:
Calculate the depth of the water (`a 丈`).

---

### Solution:

We will use the principles of similar triangles to calculate the depth of the water. Let’s translate this into Python code.


"""


from fractions import Fraction

# Convert all measurements to chi (尺)
句高 = 3  # Height of the vertical leg (句)
第一次_水岸 = Fraction(45, 10)  # First horizontal distance to the water's edge (4 chi 5 cun = 4.5 chi)
第一次_白石 = Fraction(24, 10)  # First horizontal distance to the white stone (2 chi 4 cun = 2.4 chi)

第二次_距離 = 4  # Distance between the two tools (4 chi)
第二次_水岸 = 4  # Second horizontal distance to the water's edge (4 chi)
第二次_白石 = Fraction(22, 10)  # Second horizontal distance to the white stone (2 chi 2 cun = 2.2 chi)

# Step 1: Calculate the depth of the water using similar triangles
# Let the depth of the water be "a" (in chi)
# From the first setup:
# Depth/第一次_白石 = 句高/(第一次_水岸 - 第一次_白石)
depth_first = 句高 * 第一次_白石 / (第一次_水岸 - 第一次_白石)

# From the second setup:
# Depth/第二次_白石 = 句高/(第二次_水岸 - 第二次_白石)
depth_second = 句高 * 第二次_白石 / (第二次_水岸 - 第二次_白石)

# The two calculated depths should be equal, so we verify consistency
assert depth_first == depth_second, "The two depth calculations should match!"

# Convert the depth from chi to zhang (1 zhang = 10 chi)
a = depth_first / 10

# Output the result
a


"""


---

### Explanation of the Code:
1. **Similar Triangles:** The depth of the water is proportional to the horizontal distances measured. Using the ratios of the sides of the triangles, we calculate the depth in each setup.
2. **Consistency Check:** Both setups should yield the same depth, so we verify this.
3. **Unit Conversion:** The final depth is converted from chi to zhang, as the answer is required in zhang.

---

### Final Answer:
The depth of the water is `a 丈`, where `a` is the result of the calculation above.
"""


"""
Code error: The two depth calculations should match!"""
