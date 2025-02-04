"""
今有登山臨邑，邑在山南。偃矩山上，令句高三尺五寸。令句端與邑東南隅及東北隅參相直。從句端遙望東北隅，入下股一丈二尺。又施橫句于入股之會，從立句端望西北隅，入橫句五尺。望東南隅，入下股一丈八尺。又設重矩于上，令矩間相去四丈。更從立句端望東南隅，入上股一丈七尺五寸。問邑廣長各幾何？
術曰：以句高乘東南隅入下股，如上股而一，所得減句高，餘為法；以東北隅下股減東南隅下股，餘以乘矩間為實。實如法而一，得邑南北長也。求邑廣：以入橫句乘矩間為實。實如法而一，即得邑東西廣。
答曰：南北長 a里 ；東西廣 b里 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves computing the north-south length (`a`) and east-west width (`b`) of the city (`邑`) using the given geometric relationships.

Here is the Python code:


"""


from fractions import Fraction

# Given data
句高 = Fraction(3, 1) + Fraction(5, 10)  # 3尺5寸 = 3 + 5/10 尺
東北隅入下股 = Fraction(12, 1)  # 1丈2尺 = 12尺
東南隅入下股 = Fraction(18, 1)  # 1丈8尺 = 18尺
入橫句 = Fraction(5, 1)  # 5尺
矩間 = Fraction(40, 1)  # 4丈 = 40尺
東南隅入上股 = Fraction(17, 1) + Fraction(5, 10)  # 1丈7尺5寸 = 17 + 5/10 尺

# Calculations for north-south length (a)
實_南北 = (東北隅入下股 - 東南隅入下股) * 矩間
法_南北 = (句高 * 東南隅入下股) / 東南隅入上股 - 句高
a = 實_南北 / 法_南北

# Calculations for east-west width (b)
實_東西 = 入橫句 * 矩間
法_東西 = 法_南北  # Same as 法_南北
b = 實_東西 / 法_東西

# Results
a  # 南北長 in 尺
b  # 東西廣 in 尺


"""


### Explanation of the Code:
1. **Units Conversion**: All measurements are converted to `尺` (1丈 = 10尺, 1尺 = 10寸).
2. **North-South Length (`a`)**:
   - The formula for `a` is derived from the ancient text:
     \[
     a = \frac{(東北隅入下股 - 東南隅入下股) \times 矩間}{\left(\frac{句高 \times 東南隅入下股}{東南隅入上股} - 句高\right)}
     \]
3. **East-West Width (`b`)**:
   - The formula for `b` is derived from the ancient text:
     \[
     b = \frac{入橫句 \times 矩間}{\left(\frac{句高 \times 東南隅入下股}{東南隅入上股} - 句高\right)}
     \]
4. **Fractions**: The `Fraction` class is used to ensure precise calculations, especially when dealing with non-integer values.

### Results:
- `a` represents the north-south length of the city in 尺.
- `b` represents the east-west width of the city in 尺.
"""


"""
Variable 'a' has wrong value. Expected: 4/3, Actual: -2400
Variable 'b' has wrong value. Expected: 10/9, Actual: 2000"""
