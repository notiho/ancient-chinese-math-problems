"""
今有登山望津，津在山南。偃矩山上，令句高一丈二尺。從句端斜望津南岸，入下股二丈三尺一寸。又望津北岸，入前望股裏一丈八寸。更登高巖北，卻行二十二步，上登五十一步，偃矩山上。更從句端斜望津南岸，入上股二丈二尺。問津廣幾何？
答曰： a里 。
"""

"""
This is a classic ancient Chinese surveying problem involving the use of right triangles and geometric principles to calculate the width of a river (津廣). Let's break it down step by step and translate it into Python code.

---

### Problem Breakdown:
1. **Initial Setup**:
   - A person climbs a mountain and places a right triangle (偃矩) on the mountain.
   - The height of the triangle (句高) is 1 丈 2 尺 (12 尺).
   - From the top of the triangle (句端), they look diagonally (斜望) at the south bank of the river. The diagonal line enters the lower leg (下股) by 2 丈 3 尺 1 寸 (23 尺 1 寸).

2. **Observation from the North Bank**:
   - They also observe the north bank of the river, and the diagonal line enters the front leg (前望股) by 1 丈 8 寸 (18 寸).

3. **Second Observation**:
   - The person climbs a higher peak to the north, moves back 22 steps (步), and climbs 51 steps (步) to reach the new observation point.
   - From this new position, they observe the south bank again, and the diagonal line enters the upper leg (上股) by 2 丈 2 尺 (22 尺).

4. **Question**:
   - What is the width of the river (津廣)?

---

### Units Conversion:
- 1 丈 = 10 尺
- 1 尺 = 10 寸
- 1 里 = 300 丈

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Initial data
句高 = 1 * 10 + 2  # 1 丈 2 尺 = 12 尺
下股 = 2 * 10 + 3 + Fraction(1, 10)  # 2 丈 3 尺 1 寸 = 23 尺 1 寸
前望股 = 1 * 10 + Fraction(8, 10)  # 1 丈 8 寸 = 10 尺 8 寸
上股 = 2 * 10 + 2  # 2 丈 2 尺 = 22 尺

# Step data
退步 = 22  # 22 步
登步 = 51  # 51 步
步長 = Fraction(6, 10)  # Assume 1 步 = 0.6 丈 (standard conversion)

# Convert steps to 丈
退丈 = 退步 * 步長
登丈 = 登步 * 步長

# Calculate the width of the river (津廣)
# Using similar triangles and geometric principles:
# Width of the river = (下股 + 上股) - 前望股
津廣_尺 = (下股 + 上股) - 前望股

# Convert 尺 to 丈
津廣_丈 = 津廣_尺 / 10

# Convert 丈 to 里
津廣_里 = 津廣_丈 / 300

# Answer
a = 津廣_里

print(f"津廣為: {a} 里")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Units Conversion**:
   - All measurements are converted to 尺 for consistency.
   - Steps (步) are converted to 丈 using the standard conversion of 1 步 = 0.6 丈.

2. **Geometric Principles**:
   - The width of the river is calculated using the difference in the observed legs of the triangles (下股, 上股, 前望股).

3. **Final Conversion**:
   - The result is converted from 尺 to 丈, and finally to 里, as the answer is requested in 里.

---

### Final Answer:
The width of the river (津廣) is `a` 里, where `a` is the result of the calculation.
"""


"""
Variable 'a' has wrong value. Expected: 117/50, Actual: 343/30000"""
