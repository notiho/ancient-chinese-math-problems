"""
今有登山臨邑，邑在山南。偃矩山上，令句高三尺五寸。令句端與邑東南隅及東北隅參相直。從句端遙望東北隅，入下股一丈二尺。又施橫句于入股之會，從立句端望西北隅，入橫句五尺。望東南隅，入下股一丈八尺。又設重矩于上，令矩間相去四丈。更從立句端望東南隅，入上股一丈七尺五寸。問邑廣長各幾何？
術曰：以句高乘東南隅入下股，如上股而一，所得減句高，餘為法；以東北隅下股減東南隅下股，餘以乘矩間為實。實如法而一，得邑南北長也。求邑廣：以入橫句乘矩間為實。實如法而一，即得邑東西廣。
答曰：南北長 a里 ；東西廣 b里 。
"""

"""
This is a complex ancient Chinese surveying problem involving geometry and trigonometry. Let's break it down step by step and translate it into Python code.

### Problem Description:
We are tasked with determining the length (north-south) and width (east-west) of a city (邑) based on measurements taken from a mountain using a surveying instrument (偃矩). The procedure involves multiple steps and calculations.

### Procedure:
1. **Determine the north-south length (南北長):**
   - Multiply the height of the vertical leg (句高) by the entry of the lower leg (入下股) for the southeastern corner (東南隅).
   - Divide by the upper leg (上股), subtract the height of the vertical leg (句高), and use the result as the divisor (法).
   - Subtract the lower leg entry for the southeastern corner (東南隅) from the lower leg entry for the northeastern corner (東北隅).
   - Multiply the difference by the distance between the two surveying instruments (矩間) to get the dividend (實).
   - Divide the dividend by the divisor to get the north-south length (南北長).

2. **Determine the east-west width (東西廣):**
   - Multiply the entry of the horizontal leg (入橫句) by the distance between the two surveying instruments (矩間) to get the dividend (實).
   - Divide the dividend by the divisor (法) to get the east-west width (東西廣).

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
句高 = Fraction(3, 1) + Fraction(5, 10)  # 3尺5寸 = 3 + 5/10 尺
東北隅入下股 = Fraction(12, 1)  # 1丈2尺 = 12尺
東南隅入下股 = Fraction(18, 1)  # 1丈8尺 = 18尺
入橫句 = Fraction(5, 1)  # 5尺
矩間 = Fraction(40, 1)  # 4丈 = 40尺
東南隅入上股 = Fraction(17, 1) + Fraction(5, 10)  # 1丈7尺5寸 = 17 + 5/10 尺

# Step 1: Calculate 南北長 (north-south length)
# 法 = (句高 * 東南隅入下股) / 東南隅入上股 - 句高
法 = (句高 * 東南隅入下股) / 東南隅入上股 - 句高

# 實 = (東北隅入下股 - 東南隅入下股) * 矩間
實_南北 = (東北隅入下股 - 東南隅入下股) * 矩間

# 南北長 = 實 / 法
南北長 = 實_南北 / 法

# Step 2: Calculate 東西廣 (east-west width)
# 實 = 入橫句 * 矩間
實_東西 = 入橫句 * 矩間

# 東西廣 = 實 / 法
東西廣 = 實_東西 / 法

# Convert results to li (1里 = 300尺)
a = 南北長 / 300
b = 東西廣 / 300

# Output the results
a, b
#----- content ends here -----


"""


### Explanation of the Code:
1. **Input Conversion:** All measurements are converted into chi (尺) for consistency. For example, 1丈2尺 = 12尺, and 3尺5寸 = 3 + 5/10 尺.
2. **North-South Length Calculation:** The formula for the divisor (法) and the dividend (實) is implemented step by step, following the procedure described in the problem.
3. **East-West Width Calculation:** Similarly, the formula for the east-west width is implemented.
4. **Unit Conversion:** The final results are converted from chi (尺) to li (里), where 1里 = 300尺.

### Final Answer:
- 南北長 = `a` 里
- 東西廣 = `b` 里
"""


"""
Variable 'a' has wrong value. Expected: 4/3, Actual: -8
Variable 'b' has wrong value. Expected: 10/9, Actual: 20/3"""
