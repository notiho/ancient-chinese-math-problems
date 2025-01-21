"""
今有登山臨邑，邑在山南。偃矩山上，令句高三尺五寸。令句端與邑東南隅及東北隅參相直。從句端遙望東北隅，入下股一丈二尺。又施橫句于入股之會，從立句端望西北隅，入橫句五尺。望東南隅，入下股一丈八尺。又設重矩于上，令矩間相去四丈。更從立句端望東南隅，入上股一丈七尺五寸。問邑廣長各幾何？
術曰：以句高乘東南隅入下股，如上股而一，所得減句高，餘為法；以東北隅下股減東南隅下股，餘以乘矩間為實。實如法而一，得邑南北長也。求邑廣：以入橫句乘矩間為實。實如法而一，即得邑東西廣。
答曰：南北長 a里 ；東西廣 b里 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves calculating the north-south length (`a`) and east-west width (`b`) of a city based on geometric relationships. Here's the Python code:


"""


from fractions import Fraction

# Given data
句高 = Fraction(3, 1) + Fraction(5, 10)  # 3尺5寸 = 3 + 5/10 尺
東北隅入下股 = Fraction(12, 1)  # 1丈2尺 = 12尺
東南隅入下股 = Fraction(18, 1)  # 1丈8尺 = 18尺
入橫句 = Fraction(5, 1)  # 5尺
矩間 = Fraction(40, 1)  # 4丈 = 40尺
東南隅入上股 = Fraction(17, 1) + Fraction(5, 10)  # 1丈7尺5寸 = 17 + 5/10 尺

# Step 1: Calculate the north-south length (a)
# 法 = 句高 * 東南隅入下股 - 句高
法 = 句高 * 東南隅入下股 - 句高

# 實 = (東北隅入下股 - 東南隅入下股) * 矩間
實 = (東北隅入下股 - 東南隅入下股) * 矩間

# a = 實 / 法
a = 實 / 法

# Step 2: Calculate the east-west width (b)
# 法 = 句高 * 東南隅入下股 - 句高
法 = 句高 * 東南隅入下股 - 句高

# 實 = 入橫句 * 矩間
實 = 入橫句 * 矩間

# b = 實 / 法
b = 實 / 法

# Convert results to 丈 (1丈 = 10尺)
a = a / 10  # Convert north-south length to 丈
b = b / 10  # Convert east-west width to 丈

# Results
a, b


"""


### Explanation of the Code:
1. **Input Data**: The problem provides measurements in 尺 (Chinese feet) and 寸 (Chinese inches). These are converted into fractions for precise calculations.
2. **North-South Length (`a`)**:
   - The formula for `a` is derived from the ancient method: \( a = \frac{\text{實}}{\text{法}} \), where:
     - \( \text{法} = \text{句高} \times \text{東南隅入下股} - \text{句高} \)
     - \( \text{實} = (\text{東北隅入下股} - \text{東南隅入下股}) \times \text{矩間} \)
3. **East-West Width (`b`)**:
   - The formula for `b` is also derived from the ancient method: \( b = \frac{\text{實}}{\text{法}} \), where:
     - \( \text{法} = \text{句高} \times \text{東南隅入下股} - \text{句高} \)
     - \( \text{實} = \text{入橫句} \times \text{矩間} \)
4. **Conversion to 丈**: Since the final answer is required in 丈, we divide the results by 10 (1丈 = 10尺).

### Final Output:
The variables `a` and `b` contain the north-south length and east-west width of the city in 丈, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 4/3, Actual: -48/119
Variable 'b' has wrong value. Expected: 10/9, Actual: 40/119"""
