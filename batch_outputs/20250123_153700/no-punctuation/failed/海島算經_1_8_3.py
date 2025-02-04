"""
今有登山臨邑邑在山南偃矩山上令句高三尺五寸令句端與邑東南隅及東北隅參相直從句端遙望東北隅入下股一丈二尺又施橫句于入股之會從立句端望西北隅入橫句五尺望東南隅入下股一丈八尺又設重矩于上令矩間相去四丈更從立句端望東南隅入上股一丈七尺五寸問邑廣長各幾何
術曰以句高乘東南隅入下股如上股而一所得減句高餘為法以東北隅下股減東南隅下股餘以乘矩間為實實如法而一得邑南北長也求邑廣以入橫句乘矩間為實實如法而一即得邑東西廣
答曰南北長 a里 東西廣 b里 
"""

"""
This problem involves a complex geometric calculation based on ancient Chinese surveying techniques. Let's translate the procedure into Python code step by step.

### Problem Description:
A person stands on a mountain and observes a village located to the south of the mountain. Using a series of measurements involving right triangles and distances, the goal is to calculate the north-south length and east-west width of the village.

### Procedure:
1. **North-South Length Calculation**:
   - Multiply the height of the vertical leg (句高) by the distance the southeast corner enters the lower leg (東南隅入下股).
   - Subtract the height of the vertical leg (句高) from the result.
   - Use the difference as the divisor (法).
   - Subtract the southeast corner's lower leg entry (東南隅下股) from the northeast corner's lower leg entry (東北隅下股).
   - Multiply the result by the distance between the two measuring tools (矩間) to get the dividend (實).
   - Divide the dividend by the divisor to get the north-south length.

2. **East-West Width Calculation**:
   - Multiply the distance the northwest corner enters the horizontal leg (入橫句) by the distance between the two measuring tools (矩間) to get the dividend (實).
   - Divide the dividend by the divisor to get the east-west width.

### Python Code:


"""


from fractions import Fraction

# Given data
句高 = Fraction(3, 1) + Fraction(5, 10)  # 3尺5寸 = 3 + 5/10 尺
東北隅入下股 = Fraction(12, 1)  # 1丈2尺 = 12尺
東南隅入下股 = Fraction(18, 1)  # 1丈8尺 = 18尺
入橫句 = Fraction(5, 1)  # 5尺
矩間 = Fraction(40, 1)  # 4丈 = 40尺
東南隅入上股 = Fraction(17, 1) + Fraction(5, 10)  # 1丈7尺5寸 = 17 + 5/10 尺

# Calculate the divisor (法) for north-south length
法_南北 = 句高 * 東南隅入下股 - 句高

# Calculate the dividend (實) for north-south length
實_南北 = (東北隅入下股 - 東南隅入下股) * 矩間

# Calculate the north-south length
南北長 = Fraction(實_南北, 法_南北)

# Calculate the divisor (法) for east-west width (same as 法_南北)
法_東西 = 法_南北

# Calculate the dividend (實) for east-west width
實_東西 = 入橫句 * 矩間

# Calculate the east-west width
東西廣 = Fraction(實_東西, 法_東西)

# Convert results to li (1 li = 300 chi)
a = 南北長 / 300
b = 東西廣 / 300

# Output the results
a, b


"""


### Explanation of the Code:
1. **Input Conversion**:
   - All measurements are converted into chi (尺) for consistency.
   - Fractions are used to handle non-integer values (e.g., 3尺5寸 = 3 + 5/10 尺).

2. **North-South Length Calculation**:
   - The divisor (法) is calculated as `句高 * 東南隅入下股 - 句高`.
   - The dividend (實) is calculated as `(東北隅入下股 - 東南隅入下股) * 矩間`.
   - The north-south length is obtained by dividing the dividend by the divisor.

3. **East-West Width Calculation**:
   - The divisor (法) is the same as for the north-south length.
   - The dividend (實) is calculated as `入橫句 * 矩間`.
   - The east-west width is obtained by dividing the dividend by the divisor.

4. **Conversion to Li**:
   - Since the final answer is required in li (里), the results are divided by 300 (1里 = 300尺).

### Final Answer:
The north-south length (*a*) and east-west width (*b*) of the village are given in li.
"""


"""
Variable 'a' has wrong value. Expected: 4/3, Actual: -8/595
Variable 'b' has wrong value. Expected: 10/9, Actual: 4/357"""
