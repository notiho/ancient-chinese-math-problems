"""
今有望海島，立兩表，齊高三丈，前後相去千步，令後表與前表參相直。從前表卻行一百二十三步，人目著地取望島峯，與表末參合。從後表卻行一百二十七步，人目著地取望島峯，亦與表末參合。問島高及去表各幾何？
答曰：島高 a里 ；去表 b里 。
"""

"""
This is a classic ancient Chinese surveying problem involving similar triangles to calculate the height of an island and its distance from the observation point. Let's break it down and solve it step by step.

---

### Problem Breakdown:
1. Two poles (or markers) are erected, each 3 zhang tall.
2. The distance between the two poles is 1000 bu.
3. Observations are made from two points:
   - From the front pole, the observer walks back 123 bu and aligns their line of sight with the top of the pole and the peak of the island.
   - From the rear pole, the observer walks back 127 bu and aligns their line of sight with the top of the pole and the peak of the island.

We are tasked with finding:
- The height of the island (*a*, in li).
- The distance of the island from the poles (*b*, in li).

---

### Assumptions:
1. 1 li = 300 bu (standard ancient Chinese unit conversion).
2. The problem involves similar triangles formed by the poles, the observer's line of sight, and the island.

---

### Solution:
We will use the principle of similar triangles to solve for the height of the island and its distance.

---


"""


from fractions import Fraction

# Known values
pole_height = 3  # zhang
distance_between_poles = 1000  # bu
front_observer_distance = 123  # bu
rear_observer_distance = 127  # bu

# Step 1: Calculate the height of the island (a)
# Using similar triangles:
# (island_height / distance_to_island) = (pole_height / distance_from_observer_to_pole)

# Let the distance to the island from the front pole be x (in bu).
# From the front observer:
# (pole_height / (x + front_observer_distance)) = (island_height / x)

# From the rear observer:
# (pole_height / (x + distance_between_poles + rear_observer_distance)) = (island_height / x)

# Rearrange both equations to express island_height in terms of x:
# From front observer: island_height = pole_height * x / (x + front_observer_distance)
# From rear observer: island_height = pole_height * x / (x + distance_between_poles + rear_observer_distance)

# Equate the two expressions for island_height:
# (pole_height * x / (x + front_observer_distance)) = (pole_height * x / (x + distance_between_poles + rear_observer_distance))

# Simplify:
# (x / (x + front_observer_distance)) = (x / (x + distance_between_poles + rear_observer_distance))

# Cross-multiply:
# (x + distance_between_poles + rear_observer_distance) = (x + front_observer_distance)

# Solve for x:
x = Fraction(distance_between_poles + rear_observer_distance - front_observer_distance, 1)

# Step 2: Calculate the height of the island (a)
island_height = Fraction(pole_height * x, x + front_observer_distance)

# Step 3: Convert height and distance to li
a = Fraction(island_height, 300)  # Convert height to li
b = Fraction(x, 300)  # Convert distance to li

# Output results
a, b


"""


---

### Explanation of the Code:
1. We use the principle of similar triangles to set up two equations for the height of the island (`island_height`) based on the observations from the front and rear poles.
2. By equating the two expressions for `island_height`, we solve for the distance to the island (`x`).
3. Once `x` is found, we substitute it back into the equation for `island_height`.
4. Finally, we convert the results from bu to li (1 li = 300 bu).

---

### Final Answer:
- The height of the island is `a` li.
- The distance to the island is `b` li.
"""


"""
Variable 'a' has wrong value. Expected: 251/60, Actual: 251/28175
Variable 'b' has wrong value. Expected: 205/2, Actual: 251/75"""
