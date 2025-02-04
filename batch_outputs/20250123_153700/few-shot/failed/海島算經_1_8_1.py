"""
今有登山臨邑，邑在山南。偃矩山上，令句高三尺五寸。令句端與邑東南隅及東北隅參相直。從句端遙望東北隅，入下股一丈二尺。又施橫句于入股之會，從立句端望西北隅，入橫句五尺。望東南隅，入下股一丈八尺。又設重矩于上，令矩間相去四丈。更從立句端望東南隅，入上股一丈七尺五寸。問邑廣長各幾何？
術曰：以句高乘東南隅入下股，如上股而一，所得減句高，餘為法；以東北隅下股減東南隅下股，餘以乘矩間為實。實如法而一，得邑南北長也。求邑廣：以入橫句乘矩間為實。實如法而一，即得邑東西廣。
答曰：南北長 a里 ；東西廣 b里 。
"""

"""
This is a complex ancient Chinese surveying problem involving geometry and trigonometry. Let's break it down and translate the procedure into Python code step by step.

### Problem Description:
We are tasked with calculating the length (南北長) and width (東西廣) of a town (邑) based on measurements taken from a mountain using a carpenter's square (矩). The problem involves multiple measurements and calculations based on the given procedure.

### Procedure Explanation:
1. **南北長 (North-South Length):**
   - Multiply the height of the vertical leg (句高) by the lower leg's (下股) entry for the southeast corner (東南隅).
   - Divide the result by the upper leg (上股), then subtract the height of the vertical leg (句高). The remainder is the divisor (法).
   - Subtract the lower leg's entry for the southeast corner (東南隅) from the lower leg's entry for the northeast corner (東北隅). Multiply the result by the distance between the two carpenter's squares (矩間). This is the dividend (實).
   - Divide the dividend by the divisor to get the North-South length.

2. **東西廣 (East-West Width):**
   - Multiply the horizontal leg's (橫句) entry by the distance between the two carpenter's squares (矩間). This is the dividend (實).
   - Divide the dividend by the divisor to get the East-West width.

### Python Code Implementation:


"""


from fractions import Fraction

# Given data
句高 = Fraction(3, 1) + Fraction(5, 10)  # 3尺5寸 = 3 + 5/10 尺
東北隅入下股 = Fraction(12, 1)  # 1丈2尺 = 12尺
東南隅入下股 = Fraction(18, 1)  # 1丈8尺 = 18尺
入橫句 = Fraction(5, 1)  # 5尺
矩間 = Fraction(40, 1)  # 4丈 = 40尺
東南隅入上股 = Fraction(17, 1) + Fraction(5, 10)  # 1丈7尺5寸 = 17 + 5/10 尺

# 南北長 calculation
# Step 1: Calculate 法 (divisor)
法 = (句高 * 東南隅入下股) / 東南隅入上股 - 句高

# Step 2: Calculate 實 (dividend)
實_南北 = (東北隅入下股 - 東南隅入下股) * 矩間

# Step 3: Calculate 南北長
南北長 = 實_南北 / 法

# 東西廣 calculation
# Step 1: Calculate 實 (dividend)
實_東西 = 入橫句 * 矩間

# Step 2: Calculate 東西廣
東西廣 = 實_東西 / 法

# Convert results to li (里), where 1里 = 300尺
a = 南北長 / 300
b = 東西廣 / 300

# Final answers
a, b


"""


### Explanation of the Code:
1. **Units Conversion:** All measurements are converted to chi (尺) for consistency. For example, 1丈 = 10尺, and 1寸 = 1/10尺.
2. **Fractions:** The `Fraction` class is used to ensure precise calculations without floating-point errors.
3. **Procedure Implementation:** The procedure is followed step by step as described in the problem, ensuring the calculations for both the North-South length and East-West width are accurate.
4. **Conversion to Li (里):** The final results are converted to li, where 1里 = 300尺.

### Final Answer:
- 南北長 = `a` 里
- 東西廣 = `b` 里
"""


"""
Variable 'a' has wrong value. Expected: 4/3, Actual: -8
Variable 'b' has wrong value. Expected: 10/9, Actual: 20/3"""
