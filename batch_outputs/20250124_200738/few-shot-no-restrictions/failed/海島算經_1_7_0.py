"""
今有登山望津，津在山南。偃矩山上，令句高一丈二尺。從句端斜望津南岸，入下股二丈三尺一寸。又望津北岸，入前望股裏一丈八寸。更登高巖北，卻行二十二步，上登五十一步，偃矩山上。更從句端斜望津南岸，入上股二丈二尺。問津廣幾何？
術曰：以句高乘下股，如上股而一。所得以句高減之，餘為法；置北行，以句高乘之，如上股而一。所得以減上登，餘以乘入股裏為實。實如法而一，即得津廣。
答曰： a里 。
"""

"""
This is a classic ancient Chinese geometry problem involving right triangles and proportional relationships. Let's break it down and encode the solution step by step in Python.

### Problem Breakdown:
1. **Initial Setup**:
   - The height of the mountain (`句高`) is 1丈2尺 (12尺).
   - From the top of the mountain, looking diagonally to the south bank of the river (`津南岸`), the lower leg (`下股`) is 2丈3尺1寸 (231寸).
   - Looking diagonally to the north bank of the river (`津北岸`), the forward leg (`前望股`) is 1丈8寸 (108寸).

2. **Second Observation**:
   - Moving north, the observer walks backward 22步 and climbs 51步 to reach a higher peak.
   - From this higher peak, looking diagonally to the south bank of the river, the upper leg (`上股`) is 2丈2尺 (220寸).

3. **Goal**:
   - Calculate the width of the river (`津廣`).

4. **Procedure**:
   - Use the relationships between the legs of the triangles and the height of the mountain to calculate the width of the river.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Convert all measurements to a consistent unit (寸, the smallest unit in the problem)
# 1 丈 = 10 尺, 1 尺 = 10 寸
句高 = 1 * 10 * 10 + 2 * 10  # 1丈2尺 = 120寸
下股 = 2 * 10 * 10 + 3 * 10 + 1  # 2丈3尺1寸 = 231寸
前望股 = 1 * 10 * 10 + 8  # 1丈8寸 = 108寸
上股 = 2 * 10 * 10 + 2 * 10  # 2丈2尺 = 220寸
北行 = 22 * 6  # 22步, assuming 1步 = 6尺 = 60寸
上登 = 51 * 6  # 51步, assuming 1步 = 6尺 = 60寸

# Step 1: Calculate the "法" (divisor)
# 法 = (句高 * 下股) / 上股 - 句高
法 = Fraction(句高 * 下股, 上股) - 句高

# Step 2: Calculate the "實" (numerator)
# 實 = (北行 * 句高 / 上股 - 上登) * 前望股
實 = (Fraction(北行 * 句高, 上股) - 上登) * 前望股

# Step 3: Calculate the width of the river (津廣)
# 津廣 = 實 / 法
津廣 = Fraction(實, 法)

# Convert the result back to 丈 for the final answer
津廣_in_丈 = 津廣 / (10 * 10)  # 1丈 = 100寸

# Output the result
a = 津廣_in_丈
print(f"津廣 = {a} 丈")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Unit Conversion**:
   - All measurements are converted to the smallest unit (`寸`) to ensure consistency in calculations.

2. **Step-by-Step Calculation**:
   - The divisor (`法`) is calculated using the given formula: `(句高 * 下股) / 上股 - 句高`.
   - The numerator (`實`) is calculated using the formula: `((北行 * 句高 / 上股) - 上登) * 前望股`.
   - The width of the river (`津廣`) is then obtained by dividing `實` by `法`.

3. **Final Conversion**:
   - The result is converted back to `丈` for the final answer.

---

### Example Output:
If you run the code, it will calculate the width of the river (`津廣`) in 丈. The exact value will depend on the precise relationships in the problem, but the procedure ensures an accurate result.


"""


"""
Variable 'a' has wrong value. Expected: 117/50, Actual: -1053/25"""
