"""
今有登山臨邑，邑在山南。偃矩山上，令句高三尺五寸。令句端與邑東南隅及東北隅參相直。從句端遙望東北隅，入下股一丈二尺。又施橫句于入股之會，從立句端望西北隅，入橫句五尺。望東南隅，入下股一丈八尺。又設重矩于上，令矩間相去四丈。更從立句端望東南隅，入上股一丈七尺五寸。問邑廣長各幾何？
答曰：南北長 a里 ；東西廣 b里 。
"""

"""
This is a complex ancient Chinese surveying problem involving the use of right triangles and geometric relationships to calculate the dimensions of a city (length and width) based on measurements taken from a mountain. Let's break it down step by step and translate it into Python code.

---

### Problem Breakdown:
1. **Given Measurements:**
   - The height of the mountain (`句高`) is 3 chi 5 cun (3.5 chi).
   - The distance from the mountain to the city is measured using a series of right triangles and projections:
     - From the mountain, looking at the northeast corner of the city, the lower leg (`下股`) is 1 zhang 2 chi (12 chi).
     - From the same point, looking at the northwest corner, the horizontal leg (`橫句`) is 5 chi.
     - Looking at the southeast corner, the lower leg (`下股`) is 1 zhang 8 chi (18 chi).
     - A second set of measurements is taken with a larger triangle where the distance between the two measuring points (`矩間`) is 4 zhang (40 chi).
     - From this new point, looking at the southeast corner, the upper leg (`上股`) is 1 zhang 7 chi 5 cun (17.5 chi).

2. **Goal:**
   - Calculate the north-south length (`南北長`) of the city in li.
   - Calculate the east-west width (`東西廣`) of the city in li.

---

### Python Code:


"""


from fractions import Fraction

# Convert all measurements to chi (1 zhang = 10 chi, 1 chi = 10 cun)
句高 = Fraction(3, 1) + Fraction(5, 10)  # 3 chi 5 cun = 3.5 chi
下股_東北 = 12  # 1 zhang 2 chi = 12 chi
橫句_西北 = 5  # 5 chi
下股_東南 = 18  # 1 zhang 8 chi = 18 chi
矩間 = 40  # 4 zhang = 40 chi
上股_東南 = Fraction(17, 1) + Fraction(5, 10)  # 1 zhang 7 chi 5 cun = 17.5 chi

# Step 1: Calculate the north-south length (南北長)
# Using the difference in lower legs (下股_東南 - 下股_東北)
南北長_尺 = 下股_東南 - 下股_東北

# Step 2: Calculate the east-west width (東西廣)
# Using the difference in horizontal projections (橫句_西北 and the additional upper leg 上股_東南)
東西廣_尺 = 橫句_西北 + (矩間 * (上股_東南 - 下股_東南) / 句高)

# Convert chi to li (1 li = 300 chi)
南北長_里 = 南北長_尺 / 300
東西廣_里 = 東西廣_尺 / 300

# Output the results
a = 南北長_里
b = 東西廣_里

print(f"南北長: {a} 里")
print(f"東西廣: {b} 里")


"""


---

### Explanation of the Code:
1. **Conversion of Units:**
   - All measurements are converted to chi for consistency.
   - Final results are converted to li (1 li = 300 chi).

2. **North-South Length (南北長):**
   - The difference between the lower legs (`下股_東南` and `下股_東北`) gives the north-south length in chi.

3. **East-West Width (東西廣):**
   - The horizontal projection (`橫句_西北`) is combined with the additional projection from the second set of measurements (`矩間` and `上股_東南`).

4. **Use of Fractions:**
   - The `Fraction` class is used to ensure precise calculations, especially when dealing with non-integer values like 3.5 chi or 17.5 chi.

---

### Final Output:
The program will calculate and output the north-south length (`南北長`) and east-west width (`東西廣`) of the city in li.
"""


"""
Variable 'a' has wrong value. Expected: 4/3, Actual: 0.02
Variable 'b' has wrong value. Expected: 10/9, Actual: -1/420"""
