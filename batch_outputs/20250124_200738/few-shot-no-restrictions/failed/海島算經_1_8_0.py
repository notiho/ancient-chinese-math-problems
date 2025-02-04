"""
今有登山臨邑，邑在山南。偃矩山上，令句高三尺五寸。令句端與邑東南隅及東北隅參相直。從句端遙望東北隅，入下股一丈二尺。又施橫句于入股之會，從立句端望西北隅，入橫句五尺。望東南隅，入下股一丈八尺。又設重矩于上，令矩間相去四丈。更從立句端望東南隅，入上股一丈七尺五寸。問邑廣長各幾何？
術曰：以句高乘東南隅入下股，如上股而一，所得減句高，餘為法；以東北隅下股減東南隅下股，餘以乘矩間為實。實如法而一，得邑南北長也。求邑廣：以入橫句乘矩間為實。實如法而一，即得邑東西廣。
答曰：南北長 a里 ；東西廣 b里 。
"""

"""
This is a fascinating ancient Chinese surveying problem involving geometry and trigonometry. Let's break it down step by step and translate it into Python code.

### Problem Breakdown:
1. **Given Data:**
   - The height of the vertical leg (立句高) is 3 chi 5 cun (3.5 chi).
   - The distances (入下股) from the observation point to the eastern corners (东南隅 and 东北隅) are given.
   - The horizontal leg (横句) is used to measure the western corners.
   - A second measuring frame (重矩) is placed 4 zhang away, and further measurements are taken.

2. **Goal:**
   - Calculate the north-south length (南北长) of the settlement.
   - Calculate the east-west width (东西广) of the settlement.

3. **Procedure:**
   - Use the given measurements and geometric relationships to calculate the dimensions of the settlement.

---

### Python Code Implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Convert units to chi (尺)
def to_chi(zhang=0, chi=0, cun=0):
    return zhang * 10 + chi + Fraction(cun, 10)

# Given data
句高 = to_chi(chi=3, cun=5)  # 3 chi 5 cun = 3.5 chi
矩間 = to_chi(zhang=4)       # 4 zhang = 40 chi

# 入下股 measurements
東北隅入下股 = to_chi(zhang=1, chi=2)  # 1 zhang 2 chi = 12 chi
東南隅入下股 = to_chi(zhang=1, chi=8)  # 1 zhang 8 chi = 18 chi

# 入橫句 measurement
入橫句 = to_chi(chi=5)  # 5 chi

# 入上股 measurement
東南隅入上股 = to_chi(zhang=1, chi=7, cun=5)  # 1 zhang 7 chi 5 cun = 17.5 chi

# Step 1: Calculate 南北长 (north-south length)
# 法 = (句高 * 東南隅入下股) / 東南隅入上股 - 句高
法_南北 = (句高 * 東南隅入下股) / 東南隅入上股 - 句高

# 實 = (東北隅入下股 - 東南隅入下股) * 矩間
實_南北 = (東北隅入下股 - 東南隅入下股) * 矩間

# 南北长 = 實 / 法
南北長 = 實_南北 / 法_南北

# Step 2: Calculate 東西广 (east-west width)
# 法 = 句高
法_東西 = 句高

# 實 = 入橫句 * 矩間
實_東西 = 入橫句 * 矩間

# 東西广 = 實 / 法
東西廣 = 實_東西 / 法_東西

# Convert results to li (里), where 1 li = 300 chi
南北長_里 = 南北長 / 300
東西廣_里 = 東西廣 / 300

# Final results
a = 南北長_里
b = 東西廣_里

print(f"南北长: {a} 里")
print(f"东西广: {b} 里")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Unit Conversion:**
   - The function `to_chi` converts measurements in zhang, chi, and cun into chi for consistent calculations.

2. **North-South Length (南北长):**
   - The formula for 法 (divisor) and 實 (dividend) is implemented as described in the problem.
   - The north-south length is calculated as `實 / 法`.

3. **East-West Width (东西广):**
   - Similar to the north-south length, the formula for 法 and 實 is used to calculate the east-west width.

4. **Conversion to Li (里):**
   - Since 1 li = 300 chi, the final results are converted to li.

---

### Example Output:
If you run the code, it will calculate the north-south length and east-west width of the settlement in li. Replace the given measurements with actual values if needed.
"""


"""
Variable 'a' has wrong value. Expected: 4/3, Actual: -8
Variable 'b' has wrong value. Expected: 10/9, Actual: 4/21"""
