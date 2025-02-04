"""
今有登山臨邑，邑在山南。偃矩山上，令句高三尺五寸。令句端與邑東南隅及東北隅參相直。從句端遙望東北隅，入下股一丈二尺。又施橫句于入股之會，從立句端望西北隅，入橫句五尺。望東南隅，入下股一丈八尺。又設重矩于上，令矩間相去四丈。更從立句端望東南隅，入上股一丈七尺五寸。問邑廣長各幾何？
術曰：以句高乘東南隅入下股，如上股而一，所得減句高，餘為法；以東北隅下股減東南隅下股，餘以乘矩間為實。實如法而一，得邑南北長也。求邑廣：以入橫句乘矩間為實。實如法而一，即得邑東西廣。
答曰：南北長 a里 ；東西廣 b里 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves calculating the length (南北長) and width (東西廣) of a city based on geometric relationships. We'll use the `Fraction` class to handle fractional values and ensure accuracy.

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

# Calculations for 南北長 (length)
實1 = 句高 * 東南隅入下股  # 句高乘東南隅入下股
法1 = 東南隅入上股 - 句高  # 上股 - 句高
實2 = (東北隅入下股 - 東南隅入下股) * 矩間  # (東北隅下股 - 東南隅下股) * 矩間
a = 實2 / 法1  # 南北長 = 實2 / 法1

# Calculations for 東西廣 (width)
實3 = 入橫句 * 矩間  # 入橫句 * 矩間
法2 = 法1  # Same as 法1
b = 實3 / 法2  # 東西廣 = 實3 / 法2

# Results
a = a / 10  # Convert from 尺 to 里 (1里 = 10尺)
b = b / 10  # Convert from 尺 to 里 (1里 = 10尺)

# Output variables
a, b
#----- content ends here -----


"""


### Explanation of the Code:
1. **Input Data**: The problem provides measurements in 尺 (Chinese feet) and 寸 (Chinese inches). These are converted into fractions for precise calculations.
2. **南北長 Calculation**:
   - Compute `實1` as the product of `句高` and `東南隅入下股`.
   - Compute `法1` as the difference between `東南隅入上股` and `句高`.
   - Compute `實2` as the product of the difference between `東北隅入下股` and `東南隅入下股`, and `矩間`.
   - Divide `實2` by `法1` to get the length `a`.
3. **東西廣 Calculation**:
   - Compute `實3` as the product of `入橫句` and `矩間`.
   - Divide `實3` by `法2` (same as `法1`) to get the width `b`.
4. **Unit Conversion**: Convert the results from 尺 to 里 by dividing by 10 (1里 = 10尺).

### Final Output:
The variables `a` and `b` represent the 南北長 (length) and 東西廣 (width) of the city in 里.
"""


"""
Variable 'a' has wrong value. Expected: 4/3, Actual: -12/7
Variable 'b' has wrong value. Expected: 10/9, Actual: 10/7"""
