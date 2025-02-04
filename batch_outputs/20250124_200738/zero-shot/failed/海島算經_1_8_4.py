"""
今有登山臨邑，邑在山南。偃矩山上，令句高三尺五寸。令句端與邑東南隅及東北隅參相直。從句端遙望東北隅，入下股一丈二尺。又施橫句于入股之會，從立句端望西北隅，入橫句五尺。望東南隅，入下股一丈八尺。又設重矩于上，令矩間相去四丈。更從立句端望東南隅，入上股一丈七尺五寸。問邑廣長各幾何？
術曰：以句高乘東南隅入下股，如上股而一，所得減句高，餘為法；以東北隅下股減東南隅下股，餘以乘矩間為實。實如法而一，得邑南北長也。求邑廣：以入橫句乘矩間為實。實如法而一，即得邑東西廣。
答曰：南北長 a里 ；東西廣 b里 。
"""

"""
To solve this problem, we will translate the given ancient Chinese mathematical problem into Python code. The solution involves using the class `Fraction` to handle non-integer values and calculating the unknowns `a` (南北長) and `b` (東西廣).

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
句高 = Fraction(3, 1) + Fraction(5, 10)  # 3尺5寸 = 3 + 5/10 尺
東北隅入下股 = Fraction(12, 1)  # 1丈2尺 = 12尺
東南隅入下股 = Fraction(18, 1)  # 1丈8尺 = 18尺
入橫句 = Fraction(5, 1)  # 5尺
矩間 = Fraction(40, 1)  # 4丈 = 40尺
東南隅入上股 = Fraction(17, 1) + Fraction(5, 10)  # 1丈7尺5寸 = 17 + 5/10 尺

# Step 1: Calculate 南北長 (a)
# 法 = 句高 * 東南隅入下股 - 句高
法 = 句高 * 東南隅入下股 - 句高

# 實 = (東北隅入下股 - 東南隅入下股) * 矩間
實 = (東北隅入下股 - 東南隅入下股) * 矩間

# 南北長 (a) = 實 / 法
a = 實 / 法

# Step 2: Calculate 東西廣 (b)
# 法 = 句高 * 東南隅入下股 - 句高
法 = 句高 * 東南隅入下股 - 句高

# 實 = 入橫句 * 矩間
實 = 入橫句 * 矩間

# 東西廣 (b) = 實 / 法
b = 實 / 法

# Results
a = a / 10  # Convert from 尺 to 里 (1里 = 10尺)
b = b / 10  # Convert from 尺 to 里 (1里 = 10尺)

# Output the results
a, b
#----- content ends here -----


"""


### Explanation of the Code:
1. **Units Conversion**: All measurements are converted into `尺` for consistency. At the end, the results are converted to `里` (1里 = 10尺).
2. **南北長 Calculation**:
   - The formula for `法` is derived from the problem statement: `法 = 句高 * 東南隅入下股 - 句高`.
   - The formula for `實` is: `實 = (東北隅入下股 - 東南隅入下股) * 矩間`.
   - Finally, `南北長 (a)` is calculated as `a = 實 / 法`.
3. **東西廣 Calculation**:
   - The formula for `法` is the same as above.
   - The formula for `實` is: `實 = 入橫句 * 矩間`.
   - Finally, `東西廣 (b)` is calculated as `b = 實 / 法`.
4. **Output**: The results are stored in variables `a` and `b`, representing the 南北長 and 東西廣 in `里`.

### Final Results:
The variables `a` and `b` will contain the computed values for the 南北長 and 東西廣 in `里`.
"""


"""
Variable 'a' has wrong value. Expected: 4/3, Actual: -48/119
Variable 'b' has wrong value. Expected: 10/9, Actual: 40/119"""
