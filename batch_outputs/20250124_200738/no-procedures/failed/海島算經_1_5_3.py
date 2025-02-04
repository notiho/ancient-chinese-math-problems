"""
今有東南望波口，立兩表南、北相去九丈，以索薄地連之。當北表之西卻行去表六丈，薄地遙望波口南岸，入索北端四丈二寸。以望北岸，入前所望表里一丈二尺。又卻後行去表一十三丈五尺。薄地遙望波口南岸，與南表參合。問波口廣幾何？
答曰： a里 。
"""

"""
This is a classic ancient Chinese surveying problem involving geometry and trigonometry. The problem describes a scenario where measurements are taken using poles, ropes, and observations to calculate the width of a river (波口廣). Let's break it down step by step and translate it into Python code.

---

### Problem Breakdown:
1. Two poles (南表 and 北表) are placed 9 丈 apart.
2. Observations are made from different positions:
   - From 6 丈 west of the 北表, the rope (索) intersects the northern end of the 波口 at 4 丈 2 寸 (4.2 丈).
   - From the same position, the rope intersects the southern end of the 波口 at 1 丈 2 尺 (1.2 丈) inside the 南表.
3. Moving further back to 13 丈 5 尺 (13.5 丈) west of the 北表, the rope intersects the southern end of the 波口 at the 南表.
4. The goal is to calculate the width of the 波口 (river mouth).

---

### Assumptions:
1. 1 丈 = 10 尺 = 100 寸.
2. The problem involves similar triangles to calculate the width of the river.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Measurements
南北表距離 = 9  # Distance between 南表 and 北表 in 丈
第一次觀測距離 = 6  # Distance west of 北表 for the first observation in 丈
第一次北端入索 = Fraction(42, 10)  # Rope intersection at northern end in 丈 (4 丈 2 寸 = 4.2 丈)
第一次南端入索 = Fraction(12, 10)  # Rope intersection at southern end in 丈 (1 丈 2 尺 = 1.2 丈)
第二次觀測距離 = Fraction(135, 10)  # Distance west of 北表 for the second observation in 丈 (13 丈 5 尺 = 13.5 丈)

# Step 1: Calculate the width of the river (波口廣) using similar triangles
# Let 波口廣 = a (the width of the river in 丈)

# From the first observation:
# Northern triangle: (波口廣 / 第一次北端入索) = (南北表距離 / 第一次觀測距離)
a_north = (第一次北端入索 * 南北表距離) / 第一次觀測距離

# Southern triangle: (波口廣 / 第一次南端入索) = (南北表距離 / 第一次觀測距離)
a_south = (第一次南端入索 * 南北表距離) / 第一次觀測距離

# From the second observation:
# Southern triangle: (波口廣 / 南北表距離) = (南北表距離 / 第二次觀測距離)
a_second = (南北表距離 * 南北表距離) / 第二次觀測距離

# The width of the river (波口廣) is the difference between the northern and southern intersections
a = a_north - a_south

# Convert to li (1 里 = 300 丈)
a_in_li = a / 300

# Output the result
print(f"波口廣 = {a} 丈 = {a_in_li} 里")
#----- content ends here -----


"""


---

### Explanation:
1. The problem uses **similar triangles** to calculate the width of the river.
2. The first observation gives two triangles (northern and southern), which are used to calculate the northern and southern parts of the river width.
3. The second observation confirms the southern part of the river width.
4. The total width of the river is the difference between the northern and southern parts.

---

### Final Answer:
The width of the river (波口廣) is `a` 丈, which can also be expressed in 里 (`a_in_li`).
"""


"""
Variable 'a' has wrong value. Expected: 5/3, Actual: 9/2"""
