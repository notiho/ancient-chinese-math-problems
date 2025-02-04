"""
今有望海島，立兩表，齊高三丈，前後相去千步，令後表與前表參相直。從前表卻行一百二十三步，人目著地取望島峯，與表末參合。從後表卻行一百二十七步，人目著地取望島峯，亦與表末參合。問島高及去表各幾何？
答曰：島高 a里 ；去表 b里 。
"""

"""
This is a classic ancient Chinese surveying problem that involves using similar triangles to calculate the height of an island and its distance from the observation points. Let's break it down step by step and translate it into Python code.

### Problem Breakdown:
1. Two poles (or markers) are erected, each 3 zhang tall.
2. The distance between the two poles is 1000 bu.
3. Observations are made from two points:
   - From the first pole, the observer walks back 123 bu and aligns their sight with the top of the pole and the peak of the island.
   - From the second pole, the observer walks back 127 bu and aligns their sight with the top of the pole and the peak of the island.
4. Using these observations, we calculate:
   - The height of the island (`a` in li).
   - The distance from the poles to the island (`b` in li).

---

### Assumptions and Conversions:
- 1 li = 300 bu.
- Use similar triangles to solve the problem.

---

### Python Code:


"""


from fractions import Fraction

# Constants
pole_height = 3  # height of the poles in zhang
distance_between_poles = 1000  # distance between the two poles in bu
first_observer_distance = 123  # distance observer walks back from the first pole in bu
second_observer_distance = 127  # distance observer walks back from the second pole in bu

# Step 1: Calculate the height of the island (a) using similar triangles
# Let the height of the island be H (in bu), and the distance from the poles to the island be D (in bu).
# Using similar triangles, we set up the equations:
# H / (D - first_observer_distance) = pole_height / first_observer_distance
# H / (D - distance_between_poles - second_observer_distance) = pole_height / second_observer_distance

# Solve for H and D:
# From the first equation: H = pole_height * (D - first_observer_distance) / first_observer_distance
# Substitute H into the second equation:
# pole_height * (D - first_observer_distance) / first_observer_distance
# = pole_height * (D - distance_between_poles - second_observer_distance) / second_observer_distance

# Simplify:
# (D - first_observer_distance) / first_observer_distance
# = (D - distance_between_poles - second_observer_distance) / second_observer_distance

# Cross-multiply and solve for D:
numerator_1 = Fraction(1, first_observer_distance)
numerator_2 = Fraction(1, second_observer_distance)

# Equation: (D - 123) / 123 = (D - 1000 - 127) / 127
# Rearrange to solve for D:
D = Fraction(
    distance_between_poles * numerator_1 + numerator_2,
    numerator_1,
)

# Step 2: Calculate the height of the island (H)
H = pole_height * (D - first_observer_distance) * numerator_1

# Step 3: Convert results to li
a = H / 300  # height of the island in li
b = D / 300  # distance to the island in li

# Output results
a, b


"""


---

### Explanation of the Code:
1. **Similar Triangles**: The key to solving this problem is recognizing that the triangles formed by the observer's line of sight, the pole, and the island are similar. This allows us to set up proportional relationships.
2. **Fractions**: The `Fraction` class is used to ensure exact arithmetic, avoiding floating-point errors.
3. **Conversion to Li**: Since the problem asks for the results in li, we convert from bu to li using the conversion factor (1 li = 300 bu).

---

### Final Answer:
- `a`: Height of the island in li.
- `b`: Distance from the poles to the island in li.
"""


"""
Variable 'a' has wrong value. Expected: 251/60, Actual: 55751/781050
Variable 'b' has wrong value. Expected: 205/2, Actual: 127123/38100"""
