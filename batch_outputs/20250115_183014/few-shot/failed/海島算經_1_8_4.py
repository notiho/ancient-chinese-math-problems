"""
今有登山臨邑，邑在山南。偃矩山上，令句高三尺五寸。令句端與邑東南隅及東北隅參相直。從句端遙望東北隅，入下股一丈二尺。又施橫句于入股之會，從立句端望西北隅，入橫句五尺。望東南隅，入下股一丈八尺。又設重矩于上，令矩間相去四丈。更從立句端望東南隅，入上股一丈七尺五寸。問邑廣長各幾何？
術曰：以句高乘東南隅入下股，如上股而一，所得減句高，餘為法；以東北隅下股減東南隅下股，餘以乘矩間為實。實如法而一，得邑南北長也。求邑廣：以入橫句乘矩間為實。實如法而一，即得邑東西廣。
答曰：南北長 a里 ；東西廣 b里 。
"""

"""
This is a complex ancient Chinese surveying problem involving geometry and trigonometry. The problem describes a scenario where measurements are taken from a mountain to determine the dimensions (length and width) of a settlement (邑). Below is the Python implementation of the procedure described in the problem.


"""


from fractions import Fraction

# Given data
句高 = Fraction(3, 1) + Fraction(5, 10)  # 3尺5寸
東北隅入下股 = Fraction(12, 1)  # 1丈2尺
東南隅入下股 = Fraction(18, 1)  # 1丈8尺
入橫句 = Fraction(5, 1)  # 5尺
矩間 = Fraction(40, 1)  # 4丈
東南隅入上股 = Fraction(17, 1) + Fraction(5, 10)  # 1丈7尺5寸

# 求邑南北長
# Step 1: 以句高乘東南隅入下股，如上股而一
南北法 = (句高 * 東南隅入下股) / 東南隅入上股

# Step 2: 所得減句高，餘為法
南北法 -= 句高

# Step 3: 以東北隅下股減東南隅下股，餘以乘矩間為實
南北實 = (東北隅入下股 - 東南隅入下股) * 矩間

# Step 4: 實如法而一，得邑南北長
南北長 = 南北實 / 南北法

# 求邑東西廣
# Step 1: 以入橫句乘矩間為實
東西實 = 入橫句 * 矩間

# Step 2: 實如法而一，即得邑東西廣
東西廣 = 東西實 / 南北法

# Convert results to li (1里 = 300步 = 150丈 = 1500尺)
尺_to_里 = Fraction(1, 1500)
a = 南北長 * 尺_to_里
b = 東西廣 * 尺_to_里

# Final results
a, b


"""


### Explanation of the Code:
1. **Input Conversion**: All measurements are converted into fractions to ensure precision, as ancient Chinese calculations often involved fractional arithmetic.
2. **南北長 Calculation**:
   - The formula for the north-south length is derived from the given procedure: multiplying the height of the vertical leg (句高) by the lower leg's entry for the southeast corner (東南隅入下股), dividing by the upper leg's entry (東南隅入上股), and subtracting the height (句高) to get the divisor (法).
   - The difference between the lower leg entries for the northeast and southeast corners is multiplied by the distance between the two setups (矩間) to get the dividend (實).
   - The north-south length is obtained by dividing the dividend by the divisor.
3. **東西廣 Calculation**:
   - The formula for the east-west width is simpler: multiplying the entry into the horizontal leg (入橫句) by the distance between the two setups (矩間) gives the dividend (實).
   - Dividing this by the same divisor (法) gives the east-west width.
4. **Unit Conversion**: The results are converted from 尺 (chi) to 里 (li), where 1里 = 1500尺.

### Final Answer:
- 南北長: `a` 里
- 東西廣: `b` 里
"""


"""
Variable 'a' has wrong value. Expected: 4/3, Actual: -8/5
Variable 'b' has wrong value. Expected: 10/9, Actual: 4/3"""
