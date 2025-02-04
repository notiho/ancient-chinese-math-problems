"""
今有登山臨邑，邑在山南。偃矩山上，令句高三尺五寸。令句端與邑東南隅及東北隅參相直。從句端遙望東北隅，入下股一丈二尺。又施橫句于入股之會，從立句端望西北隅，入橫句五尺。望東南隅，入下股一丈八尺。又設重矩于上，令矩間相去四丈。更從立句端望東南隅，入上股一丈七尺五寸。問邑廣長各幾何？
術曰：以句高乘東南隅入下股，如上股而一，所得減句高，餘為法；以東北隅下股減東南隅下股，餘以乘矩間為實。實如法而一，得邑南北長也。求邑廣：以入橫句乘矩間為實。實如法而一，即得邑東西廣。
答曰：南北長 a里 ；東西廣 b里 。
"""

"""
To solve the problem, we will translate the ancient Chinese mathematical method into Python code. We'll use the `Fraction` class to handle calculations involving fractions. The units for the final answers will be in "里" (Chinese miles).

Here is the Python code:


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

# Step 1: Calculate the 南北長 (a里)
# 法 = (句高 * 東南隅入下股) / 東南隅入上股 - 句高
法 = (句高 * 東南隅入下股) / 東南隅入上股 - 句高

# 實 = (東北隅入下股 - 東南隅入下股) * 矩間
實 = (東北隅入下股 - 東南隅入下股) * 矩間

# 南北長 (a里) = 實 / 法
a = 實 / 法

# Step 2: Calculate the 東西廣 (b里)
# 法 = (句高 * 東南隅入下股) / 東南隅入上股 - 句高 (same as above)
# 實 = 入橫句 * 矩間
實_廣 = 入橫句 * 矩間

# 東西廣 (b里) = 實 / 法
b = 實_廣 / 法

# Convert from 尺 to 里 (1里 = 300尺)
a = a / 300
b = b / 300

# Results
print(f"南北長 a = {a} 里")
print(f"東西廣 b = {b} 里")
#----- content ends here -----


"""


### Explanation:
1. **Input Data**: All measurements are converted into fractions of 尺 (Chinese feet). For example, 3尺5寸 is converted to `Fraction(3, 1) + Fraction(5, 10)`.

2. **南北長 Calculation**:
   - The formula for 法 is derived from the ancient method: \((句高 \times 東南隅入下股) / 東南隅入上股 - 句高\).
   - 實 is calculated as \((東北隅入下股 - 東南隅入下股) \times 矩間\).
   - 南北長 \(a\) is then computed as \(實 / 法\).

3. **東西廣 Calculation**:
   - The formula for 法 is the same as in the 南北長 calculation.
   - 實 for 東西廣 is calculated as \(入橫句 \times 矩間\).
   - 東西廣 \(b\) is then computed as \(實 / 法\).

4. **Unit Conversion**: Since the results are in 尺, they are converted to 里 by dividing by 300 (1里 = 300尺).

### Output:
The program will output the values of \(a\) (南北長) and \(b\) (東西廣) in 里.
"""


"""
Variable 'a' has wrong value. Expected: 4/3, Actual: -8
Variable 'b' has wrong value. Expected: 10/9, Actual: 20/3"""
