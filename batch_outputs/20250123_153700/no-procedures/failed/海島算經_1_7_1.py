"""
今有登山望津，津在山南。偃矩山上，令句高一丈二尺。從句端斜望津南岸，入下股二丈三尺一寸。又望津北岸，入前望股裏一丈八寸。更登高巖北，卻行二十二步，上登五十一步，偃矩山上。更從句端斜望津南岸，入上股二丈二尺。問津廣幾何？
答曰： a里 。
"""

"""
This is a classic ancient Chinese surveying problem involving the use of geometry to calculate the width of a river (津廣). The problem uses the Pythagorean theorem and proportional reasoning to determine the width of the river based on observations from different points.

Let's break it down step by step and translate it into Python code:

---

### Problem Explanation:
1. **Initial Setup**:
   - A person climbs a mountain and sets up a right triangle (偃矩) with the height of the mountain (句高) being 1丈2尺 (12尺).
   - From the top of the mountain, the person looks diagonally (斜望) to the south bank of the river, and the diagonal line extends down to the base of the mountain, entering the lower leg (下股) by 2丈3尺1寸 (231寸).
   - The person then looks diagonally to the north bank of the river, and the diagonal line enters the forward leg (前望股) by 1丈8寸 (18寸).

2. **Second Observation**:
   - The person moves to a higher peak north of the river, walking 22 steps back and climbing 51 steps up.
   - From this new position, the person looks diagonally to the south bank of the river, and the diagonal line enters the upper leg (上股) by 2丈2尺 (220寸).

3. **Question**:
   - What is the width of the river (津廣)?

---

### Assumptions:
- 1丈 = 10尺, 1尺 = 10寸.
- The problem involves proportional triangles and the Pythagorean theorem.

---

### Python Code:


"""


from fractions import Fraction

# Convert all measurements to "寸" for consistency
句高 = 12 * 10  # 1丈2尺 = 12尺 = 120寸
下股 = 2 * 10 * 10 + 3 * 10 + 1  # 2丈3尺1寸 = 231寸
前望股 = 1 * 10 + 8  # 1丈8寸 = 18寸
上股 = 2 * 10 * 10 + 2 * 10  # 2丈2尺 = 220寸

# Step 1: Calculate the width of the river (津廣) using proportional triangles
# The width of the river is proportional to the difference in the observed distances
津廣 = Fraction(下股 - 前望股, 句高) * 上股

# Convert the result back to "里" (1里 = 1800尺 = 18000寸)
津廣_in_里 = Fraction(津廣, 18000)

# Output the result
津廣_in_里


"""


---

### Explanation of the Code:
1. **Measurements**:
   - All measurements are converted to the smallest unit, "寸," for consistency.
   - This avoids fractional calculations during intermediate steps.

2. **Proportional Triangles**:
   - The width of the river (津廣) is proportional to the difference in observed distances (下股 - 前望股) relative to the height of the mountain (句高).
   - This proportionality is then applied to the second observation (上股).

3. **Conversion to 里**:
   - The final result is converted from "寸" to "里" using the conversion factor: 1里 = 18000寸.

---

### Final Answer:
The width of the river (津廣) is `a 里`, where `a` is the result of the calculation in the code above.
"""


"""
Missing variable in output: 'a'"""
