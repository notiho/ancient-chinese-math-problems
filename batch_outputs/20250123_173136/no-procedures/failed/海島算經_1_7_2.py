"""
今有登山望津，津在山南。偃矩山上，令句高一丈二尺。從句端斜望津南岸，入下股二丈三尺一寸。又望津北岸，入前望股裏一丈八寸。更登高巖北，卻行二十二步，上登五十一步，偃矩山上。更從句端斜望津南岸，入上股二丈二尺。問津廣幾何？
答曰： a里 。
"""

"""
This is a classic ancient Chinese geometry problem involving right triangles and measurements to calculate the width of a river (津廣). Let's break it down step by step and translate it into Python code.

### Problem Breakdown:
1. **First observation from the mountain:**
   - The height of the mountain (句高) is 1 丈 2 尺 = 12 尺.
   - From the top of the mountain, looking diagonally to the south bank of the river, the diagonal (斜望津南岸) enters the lower leg (下股) by 2 丈 3 尺 1 寸 = 23 尺 1 寸 = \( 23 + \frac{1}{10} \) 尺.
   - Looking diagonally to the north bank of the river, the diagonal enters the front leg (前望股) by 1 丈 8 寸 = \( 10 + \frac{8}{10} \) 尺.

2. **Second observation from a higher peak:**
   - Moving north, the observer climbs 22 steps horizontally and 51 steps vertically to a higher peak.
   - From this new height, looking diagonally to the south bank of the river, the diagonal enters the upper leg (上股) by 2 丈 2 尺 = 22 尺.

3. **Goal:**
   - Calculate the width of the river (津廣).

---

### Python Code:


"""


from fractions import Fraction

# First observation
句高_初 = 12  # Height of the mountain in 尺
下股 = 23 + Fraction(1, 10)  # Lower leg in 尺
前望股 = 10 + Fraction(8, 10)  # Front leg in 尺

# Second observation
水平步 = 22  # Horizontal steps (assume 1 step = 6 尺)
垂直步 = 51  # Vertical steps (assume 1 step = 6 尺)
句高_高 = 句高_初 + 垂直步 * 6  # New height after climbing
上股 = 22  # Upper leg in 尺

# Calculate the width of the river (津廣)
# Using the principle of similar triangles:
# Width of the river = 下股 + 前望股 + 上股
津廣 = 下股 + 前望股 + 上股

# Convert 尺 to 里 (1 里 = 300 尺)
a = 津廣 / 300

# Output the result
a


"""


---

### Explanation of the Code:
1. **Units Conversion:**
   - All measurements are converted into 尺 for consistency.
   - At the end, the width of the river (津廣) is converted into 里 (1 里 = 300 尺).

2. **Similar Triangles:**
   - The problem uses the principle of similar triangles to calculate the width of the river by summing the distances observed from the two banks.

3. **Result:**
   - The variable `a` will contain the width of the river in 里.


"""


"""
Variable 'a' has wrong value. Expected: 117/50, Actual: 559/3000"""
