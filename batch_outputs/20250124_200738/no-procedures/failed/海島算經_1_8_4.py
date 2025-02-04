"""
今有登山臨邑，邑在山南。偃矩山上，令句高三尺五寸。令句端與邑東南隅及東北隅參相直。從句端遙望東北隅，入下股一丈二尺。又施橫句于入股之會，從立句端望西北隅，入橫句五尺。望東南隅，入下股一丈八尺。又設重矩于上，令矩間相去四丈。更從立句端望東南隅，入上股一丈七尺五寸。問邑廣長各幾何？
答曰：南北長 a里 ；東西廣 b里 。
"""

"""
This is a complex ancient Chinese surveying problem involving the use of right triangles and geometric principles to calculate the dimensions of a town (邑) based on measurements taken from a mountain. Let's break it down step by step and translate it into Python code.

---

### Problem Breakdown:
1. **Given Information:**
   - A mountain is used as a vantage point to measure a town (邑) located to the south of the mountain.
   - A right triangle is formed with the mountain's height (立句, vertical leg) and the distance to the town's corners.
   - Measurements are taken using a gnomon (矩) and involve projecting lines to the town's corners.

2. **Measurements:**
   - The height of the mountain (立句) is 3 chi 5 cun (3.5 chi).
   - From the top of the mountain:
     - Looking at the northeast corner (東北隅), the horizontal leg (下股) is 1 zhang 2 chi (12 chi).
     - Looking at the southeast corner (東南隅), the horizontal leg (下股) is 1 zhang 8 chi (18 chi).
   - A second gnomon is placed 4 zhang (40 chi) away horizontally.
     - From this new position:
       - Looking at the southeast corner, the horizontal leg (上股) is 1 zhang 7 chi 5 cun (17.5 chi).

3. **Goal:**
   - Calculate the north-south length (南北長) and east-west width (東西廣) of the town in li (1 li = 180 chi).

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Convert all measurements to chi (尺)
mountain_height = Fraction(3, 1) + Fraction(5, 10)  # 3 chi 5 cun = 3.5 chi
northeast_leg = 12  # 1 zhang 2 chi = 12 chi
southeast_leg = 18  # 1 zhang 8 chi = 18 chi
second_gnomon_distance = 40  # 4 zhang = 40 chi
second_southeast_leg = Fraction(17, 1) + Fraction(5, 10)  # 1 zhang 7 chi 5 cun = 17.5 chi

# Step 1: Calculate the north-south length (南北長)
# Using the difference in horizontal legs (下股) for the southeast corner
north_south_length = (southeast_leg - second_southeast_leg) * second_gnomon_distance / mountain_height

# Step 2: Calculate the east-west width (東西廣)
# Using the northeast leg and southeast leg
east_west_width = (northeast_leg + southeast_leg) * mountain_height / second_gnomon_distance

# Step 3: Convert results to li (1 li = 180 chi)
north_south_length_li = north_south_length / 180
east_west_width_li = east_west_width / 180

# Output the results
a = north_south_length_li
b = east_west_width_li

a, b
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Mountain Height (立句):**
   - The height of the mountain is given as 3 chi 5 cun, which is converted to a fraction for precise calculations.

2. **North-South Length (南北長):**
   - The difference in horizontal legs (下股) for the southeast corner is used to calculate the north-south length, scaled by the second gnomon's distance and the mountain's height.

3. **East-West Width (東西廣):**
   - The sum of the northeast and southeast legs is used to calculate the east-west width, scaled by the mountain's height and the second gnomon's distance.

4. **Conversion to Li:**
   - Since 1 li = 180 chi, the results are divided by 180 to convert the dimensions into li.

---

### Final Answer:
The north-south length (南北長) is `a` li, and the east-west width (東西廣) is `b` li.
"""


"""
Variable 'a' has wrong value. Expected: 4/3, Actual: 2/63
Variable 'b' has wrong value. Expected: 10/9, Actual: 7/480"""
