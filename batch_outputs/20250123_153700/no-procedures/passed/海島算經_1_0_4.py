"""
今有望海島，立兩表，齊高三丈，前後相去千步，令後表與前表參相直。從前表卻行一百二十三步，人目著地取望島峯，與表末參合。從後表卻行一百二十七步，人目著地取望島峯，亦與表末參合。問島高及去表各幾何？
答曰：島高 a里 ；去表 b里 。
"""

"""
This is a classic ancient Chinese surveying problem involving similar triangles to calculate the height of an island and its distance from the observation points. Let's solve it step by step using Python.

---

### Problem Breakdown:
- Two poles (front and rear) are of equal height: 3 zhang.
- The distance between the two poles is 1000 bu.
- Observations are made from two points:
  - From the front pole, walking back 123 bu.
  - From the rear pole, walking back 127 bu.
- At both observation points, the line of sight to the island's peak aligns with the top of the poles.

We need to calculate:
1. The height of the island (`a` in li).
2. The distance of the island from the poles (`b` in li).

---

### Assumptions and Conversions:
1. 1 zhang = 10 chi.
2. 1 li = 1800 chi.
3. Use similar triangles to calculate the height and distance.

---

### Python Code:


"""


from fractions import Fraction

# Constants
pole_height = 3 * 10  # 3 zhang = 30 chi
distance_between_poles = 1000  # in bu
bu_to_chi = 6  # 1 bu = 6 chi
li_to_chi = 1800  # 1 li = 1800 chi

# Convert distances to chi
distance_between_poles_chi = distance_between_poles * bu_to_chi
front_observation_distance = 123 * bu_to_chi
rear_observation_distance = 127 * bu_to_chi

# Using similar triangles to calculate the height and distance
# Let the height of the island be H and the distance from the front pole to the island be D.

# From the front observation point:
# H / (D + front_observation_distance) = pole_height / front_observation_distance
# => H = pole_height * (D + front_observation_distance) / front_observation_distance

# From the rear observation point:
# H / (D + distance_between_poles_chi + rear_observation_distance) = pole_height / rear_observation_distance
# => H = pole_height * (D + distance_between_poles_chi + rear_observation_distance) / rear_observation_distance

# Equating the two expressions for H:
# pole_height * (D + front_observation_distance) / front_observation_distance =
# pole_height * (D + distance_between_poles_chi + rear_observation_distance) / rear_observation_distance

# Simplify:
# (D + front_observation_distance) / front_observation_distance =
# (D + distance_between_poles_chi + rear_observation_distance) / rear_observation_distance

# Cross-multiply and solve for D:
# (D + front_observation_distance) * rear_observation_distance =
# (D + distance_between_poles_chi + rear_observation_distance) * front_observation_distance

# Expand:
# D * rear_observation_distance + front_observation_distance * rear_observation_distance =
# D * front_observation_distance + distance_between_poles_chi * front_observation_distance +
# rear_observation_distance * front_observation_distance

# Group terms with D:
# D * (rear_observation_distance - front_observation_distance) =
# distance_between_poles_chi * front_observation_distance +
# rear_observation_distance * front_observation_distance -
# front_observation_distance * rear_observation_distance

# Simplify:
D = Fraction(
    distance_between_poles_chi * front_observation_distance,
    rear_observation_distance - front_observation_distance
)

# Calculate H using the first equation:
H = pole_height * (D + front_observation_distance) / front_observation_distance

# Convert results to li
a = Fraction(H, li_to_chi)  # Island height in li
b = Fraction(D, li_to_chi)  # Distance to the island in li

# Output results
a, b


"""


---

### Explanation of the Code:
1. **Similar Triangles**: The relationship between the height of the pole, the height of the island, and the distances is derived using similar triangles.
2. **Equations**: Two equations are derived based on the observations from the front and rear points. These are then solved to find `D` (distance to the island) and `H` (height of the island).
3. **Fractions**: The `Fraction` class is used to ensure exact arithmetic without floating-point errors.
4. **Unit Conversion**: All distances are converted to chi for consistency, and the final results are converted to li.

---

### Final Answer:
- `a`: The height of the island in li.
- `b`: The distance of the island from the poles in li.
"""


"""
"""
