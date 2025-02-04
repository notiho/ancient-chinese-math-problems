"""
今有登山臨邑，邑在山南。偃矩山上，令句高三尺五寸。令句端與邑東南隅及東北隅參相直。從句端遙望東北隅，入下股一丈二尺。又施橫句于入股之會，從立句端望西北隅，入橫句五尺。望東南隅，入下股一丈八尺。又設重矩于上，令矩間相去四丈。更從立句端望東南隅，入上股一丈七尺五寸。問邑廣長各幾何？
答曰：南北長 a里 ；東西廣 b里 。
"""

"""
This is a classic ancient Chinese surveying problem that involves using geometric principles to calculate the dimensions of a town (邑) based on observations from a mountain. The problem involves multiple measurements and the use of right triangles to determine the north-south length and east-west width of the town.

Let’s break it down step by step and translate it into Python code.

---

### Problem Setup:
1. **Given Measurements:**
   - The height of the mountain (立句高) is 3 chi 5 cun (3.5 chi).
   - Observations are made from the top of the mountain using a carpenter's square (矩).
   - Various measurements are taken by observing the corners of the town:
     - From the top of the mountain to the northeast corner (東北隅), the base (下股) is 1 zhang 2 chi (12 chi).
     - From the top of the mountain to the southeast corner (東南隅), the base (下股) is 1 zhang 8 chi (18 chi).
     - From the top of the mountain to the northwest corner (西北隅), the horizontal base (橫句) is 5 chi.
     - A second carpenter's square is placed 4 zhang (40 chi) higher, and from this new height:
       - To the southeast corner (東南隅), the base (上股) is 1 zhang 7 chi 5 cun (17.5 chi).

2. **Goal:**
   - Calculate the north-south length (南北長) of the town in li.
   - Calculate the east-west width (東西廣) of the town in li.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Convert all measurements to chi (尺)
height_mountain = Fraction(3, 1) + Fraction(5, 10)  # 3 chi 5 cun = 3.5 chi
base_northeast = Fraction(12, 1)  # 1 zhang 2 chi = 12 chi
base_southeast = Fraction(18, 1)  # 1 zhang 8 chi = 18 chi
base_northwest = Fraction(5, 1)  # 5 chi
height_second_square = Fraction(40, 1)  # 4 zhang = 40 chi
base_southeast_second = Fraction(17, 1) + Fraction(5, 10)  # 1 zhang 7 chi 5 cun = 17.5 chi

# Step 1: Calculate the north-south length (南北長)
# Using the difference in bases (下股) between southeast and northeast corners
north_south_length = base_southeast - base_northeast

# Step 2: Calculate the east-west width (東西廣)
# Using the difference in horizontal bases (橫句) between northwest and southeast corners
east_west_width = base_southeast_second - base_northwest

# Step 3: Convert chi to li (1 li = 300 chi)
north_south_length_li = north_south_length / 300
east_west_width_li = east_west_width / 300

# Results
a = north_south_length_li  # 南北長 in li
b = east_west_width_li  # 東西廣 in li

# Output the results
a, b
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Measurements Conversion:**
   - All given measurements are converted into chi (尺) for consistency.
   - 1 zhang = 10 chi, and 1 cun = 1/10 chi.

2. **North-South Length Calculation:**
   - The north-south length is determined by the difference in the bases (下股) between the southeast and northeast corners.

3. **East-West Width Calculation:**
   - The east-west width is determined by the difference in horizontal bases (橫句) between the northwest and southeast corners.

4. **Conversion to Li:**
   - Since the final answer is required in li, and 1 li = 300 chi, the results are divided by 300.

---

### Final Answer:
The north-south length (南北長) is `a` li, and the east-west width (東西廣) is `b` li.
"""


"""
Variable 'a' has wrong value. Expected: 4/3, Actual: 1/50
Variable 'b' has wrong value. Expected: 10/9, Actual: 1/24"""
