"""
今有東南望波口，立兩表南、北相去九丈，以索薄地連之。當北表之西卻行去表六丈，薄地遙望波口南岸，入索北端四丈二寸。以望北岸，入前所望表里一丈二尺。又卻後行去表一十三丈五尺。薄地遙望波口南岸，與南表參合。問波口廣幾何？
答曰： a里 。
"""

"""
This is a classic ancient Chinese surveying problem involving geometry and trigonometry to calculate the width of a river (波口廣). The problem involves setting up poles, measuring distances, and using the observations to determine the width of the river. Let's break it down and solve it step by step.

---

### Problem Breakdown:
1. Two poles are placed south and north, 9 丈 apart.
2. A rope is stretched across the ground between the two poles.
3. Observations are made from different positions west of the northern pole, measuring how far the rope is "entered" (intersects) when sighting the riverbanks.

---

### Variables:
- Distance between the two poles: `9 丈`
- First observation:
  - Observer moves west of the northern pole: `6 丈`
  - Rope enters the northern end: `4 丈 2 寸` = \(4 + \frac{2}{10} = 4.2 丈\)
  - Rope enters the southern end: `1 丈 2 尺` = \(1 + \frac{2}{10} = 1.2 丈\)
- Second observation:
  - Observer moves further west of the northern pole: `13 丈 5 尺` = \(13 + \frac{5}{10} = 13.5 丈\)
  - Rope aligns with the southern pole.

---

### Goal:
Calculate the width of the river (波口廣), denoted as \(a\), in 里 (1 里 = 300 丈).

---

### Solution:

We will use proportions and geometry to calculate the width of the river. The key is to recognize that the observations form similar triangles.

---

### Python Code:


"""


from fractions import Fraction

# Given data
distance_between_poles = 9  # 丈
first_observer_distance = 6  # 丈
first_rope_north_entry = Fraction(42, 10)  # 4 丈 2 寸 = 4.2 丈
first_rope_south_entry = Fraction(12, 10)  # 1 丈 2 尺 = 1.2 丈
second_observer_distance = Fraction(135, 10)  # 13 丈 5 尺 = 13.5 丈

# Step 1: Calculate the width of the river using similar triangles
# Let the width of the river be `a` (in 丈)

# From the first observation:
# Triangle formed by the northern pole, the observer, and the northern riverbank
# Width of the river (a) is proportional to the distances:
# a / (first_rope_north_entry) = (first_observer_distance) / (distance_between_poles)

a_north = (first_rope_north_entry * first_observer_distance) / distance_between_poles

# From the second observation:
# Triangle formed by the southern pole, the observer, and the southern riverbank
# a / (distance_between_poles) = (second_observer_distance) / (distance_between_poles)

a_south = (second_observer_distance * first_rope_south_entry) 

# Final width of the river (a)
a = a_north + a_south

# Convert to 里 (1 里 = 300 丈)
a_in_li = a / 300

# Output the result
a_in_li


"""


---

### Explanation of the Code:
1. **First Observation**: Using the proportions of the triangle formed by the northern pole, the observer, and the northern riverbank, we calculate the partial width of the river.
2. **Second Observation**: Using the proportions of the triangle formed by the southern pole, the observer, and the southern riverbank, we calculate the remaining width of the river.
3. **Combine Results**: Add the two partial widths to get the total width of the river.
4. **Convert to 里**: Since the result is in 丈, we divide by 300 to convert it to 里.

---

### Final Answer:
The width of the river is \(a\) 里.
"""


"""
Variable 'a' has wrong value. Expected: 5/3, Actual: 19"""
