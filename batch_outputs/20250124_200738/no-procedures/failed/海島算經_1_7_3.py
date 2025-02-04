"""
今有登山望津，津在山南。偃矩山上，令句高一丈二尺。從句端斜望津南岸，入下股二丈三尺一寸。又望津北岸，入前望股裏一丈八寸。更登高巖北，卻行二十二步，上登五十一步，偃矩山上。更從句端斜望津南岸，入上股二丈二尺。問津廣幾何？
答曰： a里 。
"""

"""
This is a classic ancient Chinese surveying problem that involves using geometry to calculate the width of a river (津廣). The problem uses a right triangle and the Pythagorean theorem to determine the width of the river based on measurements taken from different points.

Let's break it down step by step and solve it using Python.

---

### Problem Breakdown:
1. **First measurement:**
   - The height of the mountain (句高) is 1 丈 2 尺 = 12 尺.
   - From the top of the mountain, looking diagonally to the south bank of the river, the diagonal line (斜望津南岸) enters the lower leg (下股) by 2 丈 3 尺 1 寸 = 23 尺 1 寸 = 231/10 尺.
   - Looking diagonally to the north bank of the river, the diagonal line enters the front leg (前望股) by 1 丈 8 寸 = 10 尺 8 寸 = 108/10 尺.

2. **Second measurement:**
   - Moving to a higher point on the mountain, the observer moves **22 steps north** and climbs **51 steps up**.
   - From this new height, looking diagonally to the south bank of the river, the diagonal line enters the upper leg (上股) by 2 丈 2 尺 = 22 尺.

3. **Goal:**
   - Calculate the width of the river (津廣).

---

### Solution:
We will use the Pythagorean theorem and geometric relationships to calculate the width of the river step by step.


"""

#----- content starts here -----

from fractions import Fraction

# First measurement
句高 = 12  # Height of the mountain in 尺
下股 = Fraction(231, 10)  # Lower leg (south bank diagonal) in 尺
前望股 = Fraction(108, 10)  # Front leg (north bank diagonal) in 尺

# Second measurement
北移步數 = 22  # Steps moved north
登高步數 = 51  # Steps climbed up
上股 = 22  # Upper leg (south bank diagonal) in 尺

# Step 1: Calculate the width of the river (津廣) from the first measurement
# Using the Pythagorean theorem:
# 下股^2 = 句高^2 + 南岸距離^2
南岸距離 = (下股**2 - 句高**2).sqrt()

# 前望股^2 = 句高^2 + 北岸距離^2
北岸距離 = (前望股**2 - 句高**2).sqrt()

# 津廣 = 南岸距離 + 北岸距離
津廣 = 南岸距離 + 北岸距離

# Step 2: Adjust for the second measurement
# The observer moves north and climbs higher. This changes the geometry.
# We need to recalculate based on the new measurements.

# New height after climbing
新句高 = 句高 + 登高步數

# Using the Pythagorean theorem again:
# 上股^2 = 新句高^2 + 新南岸距離^2
新南岸距離 = (上股**2 - 新句高**2).sqrt()

# Adjust津廣 based on the new南岸距離
津廣 = 新南岸距離 + 北岸距離

# Convert津廣 from 尺 to 里 (1 里 = 300 尺)
津廣_里 = 津廣 / 300

# Output the result
a = 津廣_里
print(f"津廣 = {a} 里")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **First Measurement:**
   - We calculate the distances to the south and north banks of the river using the Pythagorean theorem.
   - The width of the river is the sum of these two distances.

2. **Second Measurement:**
   - The observer moves north and climbs higher, which changes the geometry.
   - We recalculate the distance to the south bank using the new height and adjust the total width of the river.

3. **Conversion:**
   - Finally, we convert the width of the river from 尺 to 里 (1 里 = 300 尺).

---

### Final Answer:
The width of the river (津廣) is `a` 里, where `a` is the result of the calculation.
"""


"""
Code error: 'Fraction' object has no attribute 'sqrt'"""
