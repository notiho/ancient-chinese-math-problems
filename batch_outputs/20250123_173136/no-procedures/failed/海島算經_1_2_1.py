"""
今有南望方邑，不知大小。立兩表東、西去六丈，齊人目，以索連之。令東表與邑東南隅及東北隅參相直。當東表之北卻行五步，遙望邑西北隅，入索東端二丈二尺六寸半。又卻北行去表一十三步二尺，遙望邑西北隅，適與西表相參合。問邑方及邑去表各幾何？
答曰：邑方 a里 ；邑去表 b里 。
"""

"""
This is a classic ancient Chinese surveying problem involving geometry and similar triangles. Let's break it down and translate it into Python code.

---

### Problem Breakdown:
1. Two poles (East and West) are placed 6 zhang apart.
2. A person stands at different positions and observes the corners of a square city (the "邑").
3. Using the observations and the distances walked, the dimensions of the city (its side length, "邑方") and the distance from the poles to the city (its distance, "邑去表") are calculated.

---

### Assumptions:
- 1 zhang = 10 chi
- 1 bu = 5 chi
- 1 li = 300 zhang = 3000 chi

---

### Variables:
- Distance between the poles = 6 zhang = 60 chi
- First observation:
  - Person moves 5 bu north = \( 5 \times 5 = 25 \) chi.
  - The rope (索) is displaced by \( 2 \times 10 + 2 + 6/10 + 5/100 = 22.65 \) chi.
- Second observation:
  - Person moves \( 13 \times 5 + 2 = 67 \) chi north.
  - The line of sight aligns with the West pole.

Using these observations, we calculate:
1. The side length of the city (邑方, "a").
2. The distance from the poles to the city (邑去表, "b").

---

### Python Code:


"""


from fractions import Fraction

# Constants
distance_between_poles = 6 * 10  # 6 zhang = 60 chi
first_north_distance = 5 * 5  # 5 bu = 25 chi
rope_displacement = 2 * 10 + 2 + Fraction(6, 10) + Fraction(5, 100)  # 22.65 chi
second_north_distance = 13 * 5 + 2  # 67 chi

# Using similar triangles to calculate the distance from the poles to the city (b)
b = (distance_between_poles * first_north_distance) / (rope_displacement - distance_between_poles)

# Using similar triangles to calculate the side length of the city (a)
a = (distance_between_poles * (second_north_distance - first_north_distance)) / (rope_displacement - distance_between_poles)

# Convert results to li (1 li = 3000 chi)
a_in_li = Fraction(a, 3000)
b_in_li = Fraction(b, 3000)

# Results
a_in_li, b_in_li


"""


---

### Explanation of the Code:
1. **Similar Triangles**:
   - The problem uses the principle of similar triangles to relate the distances and displacements.
   - The first observation gives the relationship between the rope displacement and the distance to the city.
   - The second observation gives the relationship between the side length of the city and the distances walked.

2. **Conversion to Li**:
   - Since the final answer is required in li, the results (in chi) are divided by 3000 to convert to li.

---

### Final Answer:
- \( \text{邑方 (a)} \): Side length of the city in li.
- \( \text{邑去表 (b)} \): Distance from the poles to the city in li.
"""


"""
Variable 'a' has wrong value. Expected: 151/48, Actual: -5600/83
Variable 'b' has wrong value. Expected: 83/20, Actual: -10000/249"""
