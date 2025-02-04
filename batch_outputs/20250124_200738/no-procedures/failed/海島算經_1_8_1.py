"""
今有登山臨邑，邑在山南。偃矩山上，令句高三尺五寸。令句端與邑東南隅及東北隅參相直。從句端遙望東北隅，入下股一丈二尺。又施橫句于入股之會，從立句端望西北隅，入橫句五尺。望東南隅，入下股一丈八尺。又設重矩于上，令矩間相去四丈。更從立句端望東南隅，入上股一丈七尺五寸。問邑廣長各幾何？
答曰：南北長 a里 ；東西廣 b里 。
"""

"""
This is a classic ancient Chinese surveying problem involving geometry and trigonometry. The problem describes a situation where measurements are taken from a mountain to determine the dimensions of a city (length and width). The solution involves interpreting the measurements and applying geometric principles.

Let's break this down step by step and translate it into Python code.

---

### Problem Breakdown:
1. **Given Measurements:**
   - The height of the mountain (`立句高`) is 3 chi 5 cun (3.5 chi).
   - From the top of the mountain, the observer looks at the southeast and northeast corners of the city:
     - Looking at the northeast corner, the measurement (`入下股`) is 1 zhang 2 chi (12 chi).
     - Looking at the southeast corner, the measurement (`入下股`) is 1 zhang 8 chi (18 chi).
   - A horizontal line is drawn, and from this line:
     - Looking at the northwest corner, the measurement (`入橫句`) is 5 chi.
   - A second measuring tool is set up 4 zhang (40 chi) away, and from this:
     - Looking at the southeast corner, the measurement (`入上股`) is 1 zhang 7 chi 5 cun (17.5 chi).

2. **Goal:**
   - Calculate the north-south length (`南北長`) of the city in li.
   - Calculate the east-west width (`東西廣`) of the city in li.

3. **Conversions:**
   - 1 zhang = 10 chi
   - 1 li = 180 zhang = 1800 chi

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Given measurements
立句高 = Fraction(35, 10)  # 3 chi 5 cun = 3.5 chi
入下股_東北 = 12          # 1 zhang 2 chi = 12 chi
入下股_東南 = 18          # 1 zhang 8 chi = 18 chi
入橫句_西北 = 5           # 5 chi
矩間距離 = 40             # 4 zhang = 40 chi
入上股_東南 = Fraction(175, 10)  # 1 zhang 7 chi 5 cun = 17.5 chi

# Step 1: Calculate the north-south length (南北長)
# The north-south length is the difference between 入下股_東北 and 入下股_東南
南北長_尺 = abs(入下股_東北 - 入下股_東南)

# Convert to li (1 li = 1800 chi)
南北長 = Fraction(南北長_尺, 1800)

# Step 2: Calculate the east-west width (東西廣)
# The east-west width is calculated using the horizontal measurements and the second setup
東西廣_尺 = abs(入橫句_西北 + (入上股_東南 - 入下股_東南) * 矩間距離 / 立句高)

# Convert to li (1 li = 1800 chi)
東西廣 = Fraction(東西廣_尺, 1800)

# Results
a = 南北長
b = 東西廣

print(f"南北長: {a} 里")
print(f"東西廣: {b} 里")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **North-South Length (`南北長`):**
   - The north-south length is the difference between the measurements to the northeast and southeast corners (`入下股_東北` and `入下股_東南`).
   - This difference is then converted from chi to li.

2. **East-West Width (`東西廣`):**
   - The east-west width is calculated using the horizontal measurement (`入橫句_西北`) and the difference between the upper and lower measurements (`入上股_東南 - 入下股_東南`), scaled by the distance between the two setups (`矩間距離`) and the height of the mountain (`立句高`).
   - This result is also converted from chi to li.

---

### Final Output:
The program will output the north-south length (`南北長`) and east-west width (`東西廣`) of the city in li.
"""


"""
Variable 'a' has wrong value. Expected: 4/3, Actual: 1/300
Variable 'b' has wrong value. Expected: 10/9, Actual: 1/2520"""
