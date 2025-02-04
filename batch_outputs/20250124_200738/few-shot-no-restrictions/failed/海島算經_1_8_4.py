"""
今有登山臨邑，邑在山南。偃矩山上，令句高三尺五寸。令句端與邑東南隅及東北隅參相直。從句端遙望東北隅，入下股一丈二尺。又施橫句于入股之會，從立句端望西北隅，入橫句五尺。望東南隅，入下股一丈八尺。又設重矩于上，令矩間相去四丈。更從立句端望東南隅，入上股一丈七尺五寸。問邑廣長各幾何？
術曰：以句高乘東南隅入下股，如上股而一，所得減句高，餘為法；以東北隅下股減東南隅下股，餘以乘矩間為實。實如法而一，得邑南北長也。求邑廣：以入橫句乘矩間為實。實如法而一，即得邑東西廣。
答曰：南北長 a里 ；東西廣 b里 。
"""

"""
This is a fascinating ancient Chinese surveying problem involving geometry and trigonometry. Let's break it down step by step and translate it into Python code.

### Problem Explanation:
We are tasked with determining the north-south length and east-west width of a city (邑) located south of a mountain. The problem involves using a surveying tool called a "矩" (a carpenter's square) and measurements of distances and angles. The procedure involves several steps of geometric calculations.

### Variables:
- **句高**: The height of the vertical leg of the square (3 chi 5 cun = 3.5 chi).
- **矩間**: The distance between the two squares (4 zhang = 40 chi).
- **東北隅入下股**: The distance from the northeast corner to the lower leg (1 zhang 2 chi = 12 chi).
- **東南隅入下股**: The distance from the southeast corner to the lower leg (1 zhang 8 chi = 18 chi).
- **入橫句**: The distance from the northwest corner to the horizontal leg (5 chi).
- **東南隅入上股**: The distance from the southeast corner to the upper leg (1 zhang 7 chi 5 cun = 17.5 chi).

### Procedure:
1. **Calculate the north-south length (南北長):**
   - Multiply the height of the vertical leg (句高) by the southeast corner's lower leg distance (東南隅入下股).
   - Divide the result by the upper leg distance (東南隅入上股) and subtract the height of the vertical leg (句高).
   - Use the difference between the northeast and southeast lower leg distances to calculate the actual length.

2. **Calculate the east-west width (東西廣):**
   - Multiply the horizontal leg distance (入橫句) by the distance between the two squares (矩間).
   - Divide the result by the height of the vertical leg (句高).

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
句高 = Fraction(35, 10)  # 3 chi 5 cun = 3.5 chi
矩間 = 40  # 4 zhang = 40 chi
東北隅入下股 = 12  # 1 zhang 2 chi = 12 chi
東南隅入下股 = 18  # 1 zhang 8 chi = 18 chi
入橫句 = 5  # 5 chi
東南隅入上股 = Fraction(175, 10)  # 1 zhang 7 chi 5 cun = 17.5 chi

# Step 1: Calculate 南北長 (north-south length)
# 法 = (句高 * 東南隅入下股) / 東南隅入上股 - 句高
法 = (句高 * 東南隅入下股) / 東南隅入上股 - 句高

# 實 = (東北隅入下股 - 東南隅入下股) * 矩間
實_南北 = (東北隅入下股 - 東南隅入下股) * 矩間

# 南北長 = 實 / 法
南北長 = 實_南北 / 法

# Step 2: Calculate 東西廣 (east-west width)
# 法 = 句高
法_東西 = 句高

# 實 = 入橫句 * 矩間
實_東西 = 入橫句 * 矩間

# 東西廣 = 實 / 法
東西廣 = 實_東西 / 法_東西

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
1. **Step 1 (南北長):**
   - The formula for the north-south length is derived from the relationship between the height of the square, the distances to the lower and upper legs, and the difference between the northeast and southeast distances.
   - The divisor (`法`) is calculated first, followed by the dividend (`實`), and then the length is obtained by dividing the two.

2. **Step 2 (東西廣):**
   - The formula for the east-west width is simpler, involving only the horizontal leg distance and the distance between the two squares.

3. **Unit Conversion:**
   - Since the original measurements are in chi, we convert the final results into li (1 li = 300 chi).

---

### Output:
The program will output the north-south length and east-west width of the city in li:
```
南北長: a 里
東西廣: b 里
```
"""


"""
Variable 'a' has wrong value. Expected: 4/3, Actual: -8
Variable 'b' has wrong value. Expected: 10/9, Actual: 4/21"""
