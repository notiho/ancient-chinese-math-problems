"""
今有登山臨邑邑在山南偃矩山上令句高三尺五寸令句端與邑東南隅及東北隅參相直從句端遙望東北隅入下股一丈二尺又施橫句于入股之會從立句端望西北隅入橫句五尺望東南隅入下股一丈八尺又設重矩于上令矩間相去四丈更從立句端望東南隅入上股一丈七尺五寸問邑廣長各幾何
術曰以句高乘東南隅入下股如上股而一所得減句高餘為法以東北隅下股減東南隅下股餘以乘矩間為實實如法而一得邑南北長也求邑廣以入橫句乘矩間為實實如法而一即得邑東西廣
答曰南北長 a里 東西廣 b里 
"""

"""
This is a complex ancient Chinese surveying problem involving geometry and trigonometry. The problem describes a scenario where measurements are taken from a mountain to a city (邑) using a series of tools and observations. The goal is to calculate the city's north-south length and east-west width based on the given measurements. Below is the Python implementation of the procedure described in the problem.


"""


from fractions import Fraction

# Given data
句高 = Fraction(3, 1) + Fraction(5, 10)  # 3尺5寸 = 3.5尺
東北隅入下股 = Fraction(12, 1)  # 1丈2尺 = 12尺
東南隅入下股 = Fraction(18, 1)  # 1丈8尺 = 18尺
入橫句 = Fraction(5, 1)  # 5尺
矩間 = Fraction(40, 1)  # 4丈 = 40尺
東南隅入上股 = Fraction(17, 1) + Fraction(5, 10)  # 1丈7尺5寸 = 17.5尺

# Step 1: Calculate the north-south length (南北長)
# 法 = (句高 * 東南隅入下股) - 東南隅入上股
法_南北 = (句高 * 東南隅入下股) - 東南隅入上股

# 實 = 矩間 * (東北隅入下股 - 東南隅入下股)
實_南北 = 矩間 * (東北隅入下股 - 東南隅入下股)

# 南北長 = 實 / 法
南北長 = 實_南北 / 法_南北

# Step 2: Calculate the east-west width (東西廣)
# 法 = (句高 * 東南隅入下股) - 東南隅入上股
法_東西 = 法_南北  # Same as above

# 實 = 矩間 * 入橫句
實_東西 = 矩間 * 入橫句

# 東西廣 = 實 / 法
東西廣 = 實_東西 / 法_東西

# Convert results to li (1 li = 300 chi)
a = 南北長 / 300  # 南北長 in li
b = 東西廣 / 300  # 東西廣 in li

# Final answer
print(f"南北長 a = {a} 里")
print(f"東西廣 b = {b} 里")


"""


### Explanation of the Code:
1. **Input Data**: The given measurements are converted into fractions to ensure precision. Measurements in 尺 (chi) and 寸 (cun) are converted into 尺, and 丈 (zhang) is converted into 尺 as well (1 丈 = 10 尺, 1 尺 = 10 寸).
2. **North-South Length Calculation**:
   - The formula for the divisor (`法`) is derived from the procedure: `(句高 * 東南隅入下股) - 東南隅入上股`.
   - The formula for the dividend (`實`) is: `矩間 * (東北隅入下股 - 東南隅入下股)`.
   - The north-south length is then calculated as `實 / 法`.
3. **East-West Width Calculation**:
   - The divisor (`法`) is the same as for the north-south length.
   - The formula for the dividend (`實`) is: `矩間 * 入橫句`.
   - The east-west width is then calculated as `實 / 法`.
4. **Conversion to Li**: Since the final answer is required in 里 (li), and 1 里 = 300 尺, the results are divided by 300.

### Final Output:
The program calculates the north-south length (`a`) and east-west width (`b`) of the city in 里 (li).
"""


"""
Variable 'a' has wrong value. Expected: 4/3, Actual: -8/455
Variable 'b' has wrong value. Expected: 10/9, Actual: 4/273"""
