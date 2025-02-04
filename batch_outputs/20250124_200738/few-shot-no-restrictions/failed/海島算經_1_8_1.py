"""
今有登山臨邑，邑在山南。偃矩山上，令句高三尺五寸。令句端與邑東南隅及東北隅參相直。從句端遙望東北隅，入下股一丈二尺。又施橫句于入股之會，從立句端望西北隅，入橫句五尺。望東南隅，入下股一丈八尺。又設重矩于上，令矩間相去四丈。更從立句端望東南隅，入上股一丈七尺五寸。問邑廣長各幾何？
術曰：以句高乘東南隅入下股，如上股而一，所得減句高，餘為法；以東北隅下股減東南隅下股，餘以乘矩間為實。實如法而一，得邑南北長也。求邑廣：以入橫句乘矩間為實。實如法而一，即得邑東西廣。
答曰：南北長 a里 ；東西廣 b里 。
"""

"""
This is a complex ancient Chinese surveying problem involving the use of geometry to calculate the dimensions of a city (邑) based on observations from a mountain. Let's break it down step by step and translate it into Python code.

### Problem Breakdown:
1. **Given Data:**
   - The height of the vertical leg (立句) is 3 chi 5 cun (3.5 chi).
   - Observations:
     - From the vertical leg's top, looking at the northeast corner of the city, the lower leg (下股) is 1 zhang 2 chi (12 chi).
     - Looking at the southeast corner, the lower leg is 1 zhang 8 chi (18 chi).
     - A horizontal leg (橫句) is placed at the intersection, and looking at the northwest corner, the horizontal leg is 5 chi.
   - A second measurement is taken with a new setup:
     - The distance between the two setups (矩間) is 4 zhang (40 chi).
     - From the new setup, looking at the southeast corner, the upper leg (上股) is 1 zhang 7 chi 5 cun (17.5 chi).

2. **Goal:**
   - Calculate the city's north-south length (南北長) and east-west width (東西廣).

3. **Procedure:**
   - **North-South Length (南北長):**
     - Multiply the height of the vertical leg (句高) by the southeast corner's lower leg (東南隅入下股).
     - Divide the result by the upper leg (上股), subtract the height of the vertical leg (句高), and use the remainder as the divisor (法).
     - Subtract the northeast corner's lower leg (東北隅下股) from the southeast corner's lower leg (東南隅下股), multiply the result by the distance between the setups (矩間), and use this as the dividend (實).
     - Divide the dividend by the divisor to get the north-south length.
   - **East-West Width (東西廣):**
     - Multiply the horizontal leg (入橫句) by the distance between the setups (矩間).
     - Divide the result by the divisor to get the east-west width.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
句高 = Fraction(35, 10)  # 3 chi 5 cun = 3.5 chi
東北隅下股 = 12  # 1 zhang 2 chi = 12 chi
東南隅下股 = 18  # 1 zhang 8 chi = 18 chi
入橫句 = 5  # 5 chi
矩間 = 40  # 4 zhang = 40 chi
上股 = Fraction(175, 10)  # 1 zhang 7 chi 5 cun = 17.5 chi

# Calculate 南北長 (North-South Length)
法_南北 = (句高 * 東南隅下股) / 上股 - 句高  # 法 for 南北長
實_南北 = (東南隅下股 - 東北隅下股) * 矩間  # 實 for 南北長
南北長 = 實_南北 / 法_南北  # 南北長

# Calculate 東西廣 (East-West Width)
法_東西 = 法_南北  # Same 法 as 南北長
實_東西 = 入橫句 * 矩間  # 實 for 東西廣
東西廣 = 實_東西 / 法_東西  # 東西廣

# Convert chi to li (1 li = 300 chi)
南北長_里 = 南北長 / 300
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
1. **Units:**
   - All measurements are converted to chi for consistency.
   - Final results are converted to li (1 li = 300 chi).

2. **Fractions:**
   - The `Fraction` class is used to ensure precise calculations, especially when dealing with divisions.

3. **Step-by-Step Calculations:**
   - The divisor (法) and dividend (實) are calculated separately for both the north-south length and the east-west width.
   - The results are divided to get the respective dimensions.

---

### Example Output:
If you run the code, it will calculate the north-south length (`a`) and east-west width (`b`) of the city in li.
"""


"""
Variable 'a' has wrong value. Expected: 4/3, Actual: 8
Variable 'b' has wrong value. Expected: 10/9, Actual: 20/3"""
