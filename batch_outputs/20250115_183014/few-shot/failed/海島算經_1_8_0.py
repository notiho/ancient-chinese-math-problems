"""
今有登山臨邑，邑在山南。偃矩山上，令句高三尺五寸。令句端與邑東南隅及東北隅參相直。從句端遙望東北隅，入下股一丈二尺。又施橫句于入股之會，從立句端望西北隅，入橫句五尺。望東南隅，入下股一丈八尺。又設重矩于上，令矩間相去四丈。更從立句端望東南隅，入上股一丈七尺五寸。問邑廣長各幾何？
術曰：以句高乘東南隅入下股，如上股而一，所得減句高，餘為法；以東北隅下股減東南隅下股，餘以乘矩間為實。實如法而一，得邑南北長也。求邑廣：以入橫句乘矩間為實。實如法而一，即得邑東西廣。
答曰：南北長 a里 ；東西廣 b里 。
"""

"""
This is a complex ancient Chinese surveying problem involving trigonometry-like reasoning to calculate the dimensions of a city (邑) based on measurements taken from a mountain. Let's translate the procedure into Python step by step.

### Problem Breakdown:
- The city lies south of a mountain.
- Measurements are taken using a carpenter's square (矩) and involve "legs" (句 for vertical, 股 for horizontal).
- The goal is to determine the city's north-south length and east-west width.

### Procedure:
1. **Calculate the north-south length (南北長):**
   - Multiply the height of the vertical leg (句高) by the lower horizontal leg (入下股) of the southeast corner (東南隅).
   - Divide this by the upper horizontal leg (入上股) of the southeast corner, subtracting the vertical leg (句高) from the result to get the divisor (法).
   - Subtract the lower horizontal leg of the southeast corner from the lower horizontal leg of the northeast corner (東北隅下股 - 東南隅下股).
   - Multiply the result by the distance between the two carpenter's squares (矩間) to get the dividend (實).
   - Divide the dividend by the divisor to get the north-south length.

2. **Calculate the east-west width (東西廣):**
   - Multiply the horizontal leg (入橫句) by the distance between the two carpenter's squares (矩間) to get the dividend (實).
   - Divide the dividend by the divisor (法) to get the east-west width.

### Python Code:


"""


from fractions import Fraction

# Given data
句高 = Fraction(3, 1) + Fraction(5, 10)  # 3尺5寸 = 3 + 5/10 尺
矩間 = Fraction(40, 1)  # 矩間相去四丈 = 40 尺
東北隅下股 = Fraction(12, 1)  # 入下股一丈二尺 = 12 尺
東南隅下股 = Fraction(18, 1)  # 入下股一丈八尺 = 18 尺
入橫句 = Fraction(5, 1)  # 入橫句五尺 = 5 尺
入上股 = Fraction(17, 1) + Fraction(5, 10)  # 入上股一丈七尺五寸 = 17 + 5/10 尺

# Calculate 南北長 (north-south length)
# 法 = (句高 * 東南隅下股) / 入上股 - 句高
法 = (句高 * 東南隅下股) / 入上股 - 句高

# 實 = (東北隅下股 - 東南隅下股) * 矩間
實_南北 = (東北隅下股 - 東南隅下股) * 矩間

# 南北長 = 實 / 法
南北長 = 實_南北 / 法

# Calculate 東西廣 (east-west width)
# 實 = 入橫句 * 矩間
實_東西 = 入橫句 * 矩間

# 東西廣 = 實 / 法
東西廣 = 實_東西 / 法

# Convert results to li (里), where 1 里 = 300 尺
a = 南北長 / 300
b = 東西廣 / 300

# Output results
a, b


"""


### Explanation of the Code:
1. **Units Conversion:** All measurements are converted to chi (尺) for consistency. The final results are converted to li (里), where 1 里 = 300 尺.
2. **Fractions:** The `Fraction` class is used to ensure precise calculations, especially when dealing with non-integer values like 3尺5寸 or 1丈7尺5寸.
3. **Procedure Implementation:** The code follows the ancient procedure step by step, calculating the divisor (法), the dividend (實), and the final results for both dimensions.

### Answer:
- 南北長 = `a` 里
- 東西廣 = `b` 里
"""


"""
Variable 'a' has wrong value. Expected: 4/3, Actual: -8
Variable 'b' has wrong value. Expected: 10/9, Actual: 20/3"""
