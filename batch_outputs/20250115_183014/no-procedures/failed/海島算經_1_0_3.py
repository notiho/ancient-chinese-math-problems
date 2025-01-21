"""
今有望海島，立兩表，齊高三丈，前後相去千步，令後表與前表參相直。從前表卻行一百二十三步，人目著地取望島峯，與表末參合。從後表卻行一百二十七步，人目著地取望島峯，亦與表末參合。問島高及去表各幾何？
答曰：島高 a里 ；去表 b里 。
"""

"""
This is a classic ancient Chinese surveying problem involving similar triangles. Let's break it down step by step and translate it into Python code.

### Problem Explanation:
1. Two poles (or markers) are erected, each 3 zhang tall, and are spaced 1000 bu apart.
2. Observations are made from two positions:
   - From the first pole, walking back 123 bu and aligning the top of the pole with the peak of the island.
   - From the second pole, walking back 127 bu and aligning the top of the pole with the peak of the island.
3. Using these observations, we are tasked to calculate:
   - The height of the island (*a* li).
   - The distance of the island from the poles (*b* li).

---

### Assumptions:
1. 1 li = 300 bu (standard ancient Chinese unit conversion).
2. The problem uses similar triangles to calculate the height and distance.

---

### Python Code:


"""


from fractions import Fraction

# Known values
pole_height = 3  # in zhang
distance_between_poles = 1000  # in bu
first_observation_distance = 123  # in bu
second_observation_distance = 127  # in bu

# Step 1: Calculate the height of the island (a) and the distance to the island (b)
# Using similar triangles:
# Let the height of the island be H (in bu) and the distance to the island be D (in bu).

# From the first observation:
# H / (D + 123) = pole_height / 123
# H = pole_height * (D + 123) / 123

# From the second observation:
# H / (D + 1000 + 127) = pole_height / 127
# H = pole_height * (D + 1000 + 127) / 127

# Equating the two expressions for H:
# pole_height * (D + 123) / 123 = pole_height * (D + 1127) / 127
# Simplify by dividing through by pole_height:
# (D + 123) / 123 = (D + 1127) / 127

# Cross-multiply to solve for D:
# 127 * (D + 123) = 123 * (D + 1127)
# 127D + 127 * 123 = 123D + 123 * 1127
# 127D - 123D = 123 * 1127 - 127 * 123
# 4D = 123 * 1127 - 127 * 123
# D = (123 * 1127 - 127 * 123) / 4

D = Fraction(123 * 1127 - 127 * 123, 4)  # Distance to the island in bu

# Step 2: Calculate the height of the island (H)
H = pole_height * (D + first_observation_distance) / first_observation_distance  # Height in bu

# Step 3: Convert results to li (1 li = 300 bu)
a = H / 300  # Height of the island in li
b = D / 300  # Distance to the island in li

# Results
print(f"島高 a = {a} 里")
print(f"去表 b = {b} 里")


"""


---

### Explanation of the Code:
1. We use the principle of similar triangles to set up two equations for the height of the island (*H*).
2. By equating the two expressions for *H*, we solve for the distance to the island (*D*).
3. Once *D* is known, we substitute it back into one of the equations to calculate the height of the island (*H*).
4. Finally, we convert the results from bu to li.

---

### Final Answer:
After running the code, you will get the values for:
- `a`: The height of the island in li.
- `b`: The distance to the island in li.
"""


"""
Variable 'a' has wrong value. Expected: 251/60, Actual: 251/100"""
