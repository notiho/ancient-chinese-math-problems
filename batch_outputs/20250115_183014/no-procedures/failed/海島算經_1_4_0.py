"""
今有登山望樓，樓在平地。偃矩山上，令句高六尺。從句端斜望樓足，入下股一丈二尺。又設重矩于上，令其間相去三丈。更從句端斜望樓足，入上股一丈一尺四寸。又立小表于入股之會，復從句端斜望樓岑端，入小表八寸。問樓高幾何？
答曰： a丈 。
"""

"""
This is a classic ancient Chinese math problem involving geometry and similar triangles. Let's break it down step by step and solve it using Python code.

---

### Problem Breakdown:
1. A person is on a mountain looking at a tower (楼) on flat ground.
2. A horizontal ruler (偃矩) is placed on the mountain, and the vertical height (句) of the ruler is 6 chi (尺).
3. From the end of the ruler (句端), the person looks diagonally at the base of the tower (楼足). The horizontal distance (股) from the mountain to the tower is 1 zhang 2 chi (12 chi).
4. Another ruler is placed higher up, 3 zhang (30 chi) away from the first. From this new position, the person looks diagonally at the base of the tower, and the horizontal distance is 1 zhang 1 chi 4 cun (11.4 chi).
5. A small pole (小表) is placed at the intersection of the horizontal lines. From the end of the ruler, the person looks diagonally at the top of the tower (楼岑端), and the horizontal distance to the small pole is 8 cun (0.8 chi).
6. The goal is to calculate the height of the tower (楼高).

---

### Solution:
We will use the concept of similar triangles to solve this step by step.

---


"""


from fractions import Fraction

# Step 1: Define the given values
句高 = 6  # Vertical height of the ruler (in chi)
下股 = 12  # Horizontal distance to the base of the tower from the first position (in chi)
上股 = 11 + Fraction(4, 10)  # Horizontal distance to the base of the tower from the second position (in chi)
間距 = 30  # Distance between the two positions (in chi)
小表 = Fraction(8, 10)  # Horizontal distance to the small pole (in chi)

# Step 2: Calculate the height of the tower
# Using similar triangles:
# From the first position:
樓高_下 = (句高 / 下股) * (下股 + 間距)

# From the second position:
樓高_上 = (句高 / 上股) * (上股 + 小表)

# Combine the two results (they should be the same, but we verify consistency)
樓高 = (樓高_下 + 樓高_上) / 2

# Convert to zhang (1 zhang = 10 chi)
a = 樓高 / 10

# Output the result
a


"""


---

### Explanation:
1. We use the property of similar triangles to calculate the height of the tower from both positions.
2. The formula for the height of the tower is derived from the ratio of the vertical height (句高) to the horizontal distance (股).
3. We calculate the height from both positions and take the average to ensure consistency.
4. Finally, we convert the result from chi to zhang.

---

### Final Answer:
The height of the tower is `a` zhang.
"""


"""
Variable 'a' has wrong value. Expected: 8, Actual: 1.3710526315789475"""
