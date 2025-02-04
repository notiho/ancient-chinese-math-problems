"""
今有登山臨邑，邑在山南。偃矩山上，令句高三尺五寸。令句端與邑東南隅及東北隅參相直。從句端遙望東北隅，入下股一丈二尺。又施橫句于入股之會，從立句端望西北隅，入橫句五尺。望東南隅，入下股一丈八尺。又設重矩于上，令矩間相去四丈。更從立句端望東南隅，入上股一丈七尺五寸。問邑廣長各幾何？
術曰：以句高乘東南隅入下股，如上股而一，所得減句高，餘為法；以東北隅下股減東南隅下股，餘以乘矩間為實。實如法而一，得邑南北長也。求邑廣：以入橫句乘矩間為實。實如法而一，即得邑東西廣。
答曰：南北長 a里 ；東西廣 b里 。
"""

"""
This is a complex ancient Chinese surveying problem involving geometry and trigonometry to calculate the dimensions of a city (邑) based on measurements taken from a mountain. Let's break it down step by step and translate it into Python code.

---

### Problem Breakdown:
1. **Given Measurements:**
   - Height of the vertical leg (句高): 3 尺 5 寸 = \( 3 + \frac{5}{10} = 3.5 \) 尺.
   - Distance from the vertical leg to the southeast corner (東南隅入下股): 1 丈 2 尺 = \( 10 + 2 = 12 \) 尺.
   - Distance from the vertical leg to the northeast corner (東北隅入下股): 1 丈 8 尺 = \( 10 + 8 = 18 \) 尺.
   - Horizontal distance from the vertical leg to the northwest corner (入橫句): 5 尺.
   - Distance between the two measuring tools (矩間): 4 丈 = \( 40 \) 尺.
   - Distance from the vertical leg to the southeast corner using the upper tool (入上股): 1 丈 7 尺 5 寸 = \( 10 + 7 + \frac{5}{10} = 17.5 \) 尺.

2. **Formulas:**
   - **South-North Length (南北長):**
     \[
     \text{法} = \text{句高} \times \text{東南隅入下股} \div \text{入上股} - \text{句高}
     \]
     \[
     \text{實} = (\text{東北隅下股} - \text{東南隅下股}) \times \text{矩間}
     \]
     \[
     \text{南北長} = \text{實} \div \text{法}
     \]

   - **East-West Width (東西廣):**
     \[
     \text{法} = \text{句高}
     \]
     \[
     \text{實} = \text{入橫句} \times \text{矩間}
     \]
     \[
     \text{東西廣} = \text{實} \div \text{法}
     \]

3. **Units Conversion:**
   - 1 丈 = 10 尺.
   - 1 里 = 300 尺.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Given measurements
句高 = Fraction(3, 1) + Fraction(5, 10)  # 3 尺 5 寸 = 3.5 尺
東南隅入下股 = 10 + 2  # 1 丈 2 尺 = 12 尺
東北隅入下股 = 10 + 8  # 1 丈 8 尺 = 18 尺
入橫句 = 5  # 5 尺
矩間 = 40  # 4 丈 = 40 尺
入上股 = 10 + 7 + Fraction(5, 10)  # 1 丈 7 尺 5 寸 = 17.5 尺

# Calculate 南北長 (South-North Length)
法_南北 = (句高 * 東南隅入下股) / 入上股 - 句高
實_南北 = (東北隅入下股 - 東南隅入下股) * 矩間
南北長 = 實_南北 / 法_南北

# Convert 南北長 to 里
南北長_里 = 南北長 / 300

# Calculate 東西廣 (East-West Width)
法_東西 = 句高
實_東西 = 入橫句 * 矩間
東西廣 = 實_東西 / 法_東西

# Convert 東西廣 to 里
東西廣_里 = 東西廣 / 300

# Final results
a = 南北長_里
b = 東西廣_里

print(f"南北長: {a} 里")
print(f"東西廣: {b} 里")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Input Measurements:** All given measurements are converted into 尺 (chi) for consistency.
2. **South-North Length Calculation:**
   - The divisor (法) is calculated using the formula involving the height of the vertical leg, the lower leg distances, and the upper leg distance.
   - The dividend (實) is calculated using the difference between the lower leg distances and the distance between the tools.
   - The length is then calculated by dividing the dividend by the divisor.
3. **East-West Width Calculation:**
   - The divisor (法) is simply the height of the vertical leg.
   - The dividend (實) is calculated using the horizontal distance and the distance between the tools.
   - The width is then calculated by dividing the dividend by the divisor.
4. **Unit Conversion:** The results are converted from 尺 to 里 (1 里 = 300 尺).
5. **Output Results:** The South-North length and East-West width are printed in 里.

---

### Example Output:
If you run the code, you will get the values of `a` (南北長) and `b` (東西廣) in 里.
"""


"""
Variable 'a' has wrong value. Expected: 4/3, Actual: -8/11
Variable 'b' has wrong value. Expected: 10/9, Actual: 4/21"""
