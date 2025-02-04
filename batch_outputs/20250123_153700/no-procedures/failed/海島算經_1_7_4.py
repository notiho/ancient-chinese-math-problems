"""
今有登山望津，津在山南。偃矩山上，令句高一丈二尺。從句端斜望津南岸，入下股二丈三尺一寸。又望津北岸，入前望股裏一丈八寸。更登高巖北，卻行二十二步，上登五十一步，偃矩山上。更從句端斜望津南岸，入上股二丈二尺。問津廣幾何？
答曰： a里 。
"""

"""
This is a classic ancient Chinese surveying problem involving the use of geometry to calculate the width of a river (津廣). The problem involves multiple observations and measurements using a right triangle (偃矩), and we need to calculate the width of the river based on the given data.

Let's break it down step by step and translate it into Python code.

---

### Problem Breakdown:
1. **Initial Setup:**
   - The height of the mountain (句高) is 1 丈 2 尺 = 12 尺.
   - From the top of the mountain, looking diagonally to the south bank of the river, the diagonal (斜望) enters the lower leg (下股) by 2 丈 3 尺 1 寸 = 23 尺 1 寸 = 231/10 尺.
   - Looking diagonally to the north bank of the river, the diagonal enters the forward leg (前望股) by 1 丈 8 寸 = 10 尺 8 寸 = 108/10 尺.

2. **Second Observation:**
   - Moving north, the observer walks 22 步 backward and climbs 51 步 up to another high point.
   - From this new point, looking diagonally to the south bank of the river, the diagonal enters the upper leg (上股) by 2 丈 2 尺 = 22 尺.

3. **Goal:**
   - Calculate the width of the river (津廣).

---

### Python Code:


"""


from fractions import Fraction

# Convert all measurements to 尺
丈_to_尺 = 10
步_to_尺 = 6  # Assuming 1 步 = 6 尺
寸_to_尺 = Fraction(1, 10)

# Initial measurements
句高 = 1 * 丈_to_尺 + 2  # 1 丈 2 尺 = 12 尺
下股 = 2 * 丈_to_尺 + 3 + 1 * 寸_to_尺  # 2 丈 3 尺 1 寸 = 231/10 尺
前望股 = 1 * 丈_to_尺 + 8 * 寸_to_尺  # 1 丈 8 寸 = 108/10 尺

# Second observation measurements
北行 = 22 * 步_to_尺  # 22 步 = 132 尺
登高 = 51 * 步_to_尺  # 51 步 = 306 尺
上股 = 2 * 丈_to_尺 + 2  # 2 丈 2 尺 = 22 尺

# Step 1: Calculate the width of the river (津廣) using geometry
# Using the first observation:
南岸_距離 = (句高 * 下股) / (下股 - 前望股)

# Using the second observation:
北岸_距離 = (句高 + 登高) * 上股 / (上股 - 前望股)

# The total width of the river is the sum of the distances to the south and north banks
津廣 = 南岸_距離 + 北岸_距離

# Convert the result to 里 (1 里 = 300 尺)
津廣_里 = 津廣 / 300

# Output the result
津廣_里


"""


---

### Explanation of the Code:
1. **Unit Conversion:**
   - All measurements are converted to 尺 for consistency.
   - 丈 is converted to 尺 (1 丈 = 10 尺), 步 is converted to 尺 (1 步 = 6 尺), and 寸 is converted to 尺 (1 寸 = 1/10 尺).

2. **First Observation:**
   - Using the geometry of a right triangle, the distance to the south bank (南岸_距離) is calculated as:
     \[
     南岸_距離 = \frac{\text{句高} \times \text{下股}}{\text{下股} - \text{前望股}}
     \]

3. **Second Observation:**
   - Similarly, the distance to the north bank (北岸_距離) is calculated as:
     \[
     北岸_距離 = \frac{(\text{句高} + \text{登高}) \times \text{上股}}{\text{上股} - \text{前望股}}
     \]

4. **Total Width:**
   - The total width of the river (津廣) is the sum of the distances to the south and north banks:
     \[
     津廣 = 南岸_距離 + 北岸_距離
     \]

5. **Conversion to 里:**
   - The result is converted to 里 (1 里 = 300 尺).

---

### Final Answer:
The variable `津廣_里` will contain the width of the river in 里 as a `Fraction`.
"""


"""
Missing variable in output: 'a'"""
