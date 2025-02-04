"""
今有登山臨邑邑在山南偃矩山上令句高三尺五寸令句端與邑東南隅及東北隅參相直從句端遙望東北隅入下股一丈二尺又施橫句于入股之會從立句端望西北隅入橫句五尺望東南隅入下股一丈八尺又設重矩于上令矩間相去四丈更從立句端望東南隅入上股一丈七尺五寸問邑廣長各幾何
術曰以句高乘東南隅入下股如上股而一所得減句高餘為法以東北隅下股減東南隅下股餘以乘矩間為實實如法而一得邑南北長也求邑廣以入橫句乘矩間為實實如法而一即得邑東西廣
答曰南北長 a里 東西廣 b里 
"""

"""
This is a complex ancient Chinese surveying problem involving geometry and trigonometry. Let's break it down and translate it into Python step by step.

### Problem Description:
We are tasked with finding the north-south length and east-west width of a city (邑) located south of a mountain. The problem involves using a series of measurements taken from a right triangle (偃矩) and applying the given procedure (術).

### Procedure Explanation:
1. **North-South Length (南北長):**
   - Multiply the height of the vertical leg (句高) by the distance the southeast corner (東南隅) enters the lower leg (下股).
   - Subtract the height of the vertical leg (句高) from the result to obtain the divisor (法).
   - Subtract the southeast corner's lower leg distance (東南隅下股) from the northeast corner's lower leg distance (東北隅下股). Multiply the result by the distance between the two measuring tools (矩間) to obtain the dividend (實).
   - Divide the dividend by the divisor to get the north-south length.

2. **East-West Width (東西廣):**
   - Multiply the distance the west corner (西北隅) enters the horizontal leg (橫句) by the distance between the two measuring tools (矩間) to obtain the dividend (實).
   - Divide the dividend by the divisor (法) to get the east-west width.

### Python Code Implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
句高 = Fraction(3, 1) + Fraction(5, 10)  # 3尺5寸 = 3 + 5/10 尺
東北隅下股 = Fraction(12, 1)  # 1丈2尺 = 12尺
東南隅下股 = Fraction(18, 1)  # 1丈8尺 = 18尺
矩間 = Fraction(40, 1)  # 4丈 = 40尺
東南隅上股 = Fraction(17, 1) + Fraction(5, 10)  # 1丈7尺5寸 = 17 + 5/10 尺
西北隅橫句 = Fraction(5, 1)  # 5尺

# Procedure for 南北長 (North-South Length)
# 法 = (句高 * 東南隅下股) - 句高
法_南北 = (句高 * 東南隅下股) - 句高

# 實 = (東北隅下股 - 東南隅下股) * 矩間
實_南北 = (東北隅下股 - 東南隅下股) * 矩間

# 南北長 = 實 / 法
南北長 = 實_南北 / 法_南北

# Procedure for 東西廣 (East-West Width)
# 實 = 西北隅橫句 * 矩間
實_東西 = 西北隅橫句 * 矩間

# 東西廣 = 實 / 法
東西廣 = 實_東西 / 法_南北

# Convert results to li (里), where 1里 = 300尺
南北長_里 = 南北長 / 300
東西廣_里 = 東西廣 / 300

# Final answers
a = 南北長_里
b = 東西廣_里

print(f"南北長: {a} 里, 東西廣: {b} 里")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Input Conversion:**
   - All measurements are converted into chi (尺) for consistency. For example, 1丈 = 10尺, and 1寸 = 1/10尺.

2. **North-South Length Calculation:**
   - The formula for the divisor (法) and the dividend (實) is implemented as described in the procedure.
   - The result is divided to obtain the north-south length in chi, then converted to li (里), where 1里 = 300尺.

3. **East-West Width Calculation:**
   - Similarly, the formula for the east-west width is implemented, using the same divisor (法) as for the north-south length.

4. **Output:**
   - The results are printed in li (里) as required by the problem.

### Final Answer:
The code will compute the values of `a` (南北長) and `b` (東西廣) in li (里).
"""


"""
Variable 'a' has wrong value. Expected: 4/3, Actual: -8/595
Variable 'b' has wrong value. Expected: 10/9, Actual: 4/357"""
