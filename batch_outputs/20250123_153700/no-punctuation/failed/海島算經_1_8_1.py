"""
今有登山臨邑邑在山南偃矩山上令句高三尺五寸令句端與邑東南隅及東北隅參相直從句端遙望東北隅入下股一丈二尺又施橫句于入股之會從立句端望西北隅入橫句五尺望東南隅入下股一丈八尺又設重矩于上令矩間相去四丈更從立句端望東南隅入上股一丈七尺五寸問邑廣長各幾何
術曰以句高乘東南隅入下股如上股而一所得減句高餘為法以東北隅下股減東南隅下股餘以乘矩間為實實如法而一得邑南北長也求邑廣以入橫句乘矩間為實實如法而一即得邑東西廣
答曰南北長 a里 東西廣 b里 
"""

"""
This is a complex ancient Chinese geometry problem involving trigonometric reasoning and proportional relationships. Let's break it down step by step and translate it into Python code.

### Problem Description:
We are tasked with determining the width (east-west) and length (north-south) of a city (邑) based on measurements taken from a mountain. The problem involves multiple measurements and the use of geometric relationships.

### Procedure:
1. **South-North Length (南北長):**
   - Multiply the height of the vertical leg (句高) by the distance the southeast corner (東南隅) enters the lower leg (下股).
   - Subtract the height of the vertical leg (句高) from the result to get the divisor (法).
   - Subtract the southeast corner's lower leg entry (東南隅下股) from the northeast corner's lower leg entry (東北隅下股). Multiply the result by the distance between the two measuring tools (矩間) to get the dividend (實).
   - Divide the dividend by the divisor to get the north-south length (南北長).

2. **East-West Width (東西廣):**
   - Multiply the distance the northwest corner (西北隅) enters the horizontal leg (橫句) by the distance between the two measuring tools (矩間) to get the dividend (實).
   - Divide the dividend by the divisor (法) to get the east-west width (東西廣).

### Python Code:


"""


from fractions import Fraction

# Given data
句高 = Fraction(3, 1) + Fraction(5, 10)  # 3尺5寸 (convert to fractional chi)
矩間 = 4  # 矩間相去四丈 (4丈 = 40尺)
東北隅下股 = 12  # 入下股一丈二尺 (12尺)
東南隅下股 = 18  # 入下股一丈八尺 (18尺)
西北隅入橫句 = 5  # 入橫句五尺 (5尺)
東南隅上股 = Fraction(17, 1) + Fraction(5, 10)  # 入上股一丈七尺五寸 (17尺5寸)

# 南北長 (North-South Length)
# Step 1: Calculate the divisor (法)
法 = (句高 * 東南隅下股) - 句高

# Step 2: Calculate the dividend (實) for 南北長
南北實 = (東北隅下股 - 東南隅下股) * 矩間

# Step 3: Calculate 南北長
南北長 = 南北實 / 法

# 東西廣 (East-West Width)
# Step 1: Calculate the dividend (實) for 東西廣
東西實 = 西北隅入橫句 * 矩間

# Step 2: Calculate 東西廣
東西廣 = 東西實 / 法

# Convert results to li (里), where 1里 = 300尺
a = 南北長 / 300  # 南北長 in 里
b = 東西廣 / 300  # 東西廣 in 里

# Final results
a, b


"""


### Explanation of the Code:
1. **Units Conversion:** All measurements are converted to chi (尺) for consistency. For example, 3尺5寸 is converted to `3 + 5/10` chi.
2. **Fractions:** The `Fraction` class is used to ensure precise calculations, as ancient Chinese mathematics often dealt with exact ratios.
3. **Procedure Implementation:** The steps outlined in the procedure are followed exactly, with clear separation of the divisor (法) and dividend (實) calculations.
4. **Conversion to Li (里):** The final results are converted from chi (尺) to li (里), where 1里 = 300尺.

### Final Answer:
- 南北長 (North-South Length): `a` li
- 東西廣 (East-West Width): `b` li
"""


"""
Variable 'a' has wrong value. Expected: 4/3, Actual: -4/2975
Variable 'b' has wrong value. Expected: 10/9, Actual: 2/1785"""
