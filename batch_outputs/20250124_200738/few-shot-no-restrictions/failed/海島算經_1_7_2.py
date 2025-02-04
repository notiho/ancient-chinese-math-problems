"""
今有登山望津，津在山南。偃矩山上，令句高一丈二尺。從句端斜望津南岸，入下股二丈三尺一寸。又望津北岸，入前望股裏一丈八寸。更登高巖北，卻行二十二步，上登五十一步，偃矩山上。更從句端斜望津南岸，入上股二丈二尺。問津廣幾何？
術曰：以句高乘下股，如上股而一。所得以句高減之，餘為法；置北行，以句高乘之，如上股而一。所得以減上登，餘以乘入股裏為實。實如法而一，即得津廣。
答曰： a里 。
"""

"""
This is a classic ancient Chinese geometry problem involving right triangles and proportions. Let's translate the problem into Python step by step.

---

### Problem Breakdown:
1. **Given Data:**
   - The height of the mountain (`句高`) is 1丈2尺 = 12尺.
   - From the top of the mountain:
     - Looking diagonally to the south bank of the river (`津南岸`), the lower leg (`下股`) is 2丈3尺1寸 = 23尺1寸 = 231寸.
     - Looking diagonally to the north bank of the river (`津北岸`), the forward leg (`前望股裏`) is 1丈8寸 = 18寸.
   - Moving to a higher northern peak:
     - Walk back 22 steps (`北行`), then climb up 51 steps (`上登`).
     - From the new height, looking diagonally to the south bank of the river, the upper leg (`上股`) is 2丈2尺 = 22尺.

2. **Goal:**
   - Calculate the width of the river (`津廣`).

3. **Procedure:**
   - Use the given relationships and proportions to calculate the width of the river step by step.

---

### Python Code Implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Convert units to consistent measurements (寸, smallest unit)
# 1 丈 = 10 尺, 1 尺 = 10 寸
丈_to_寸 = 100  # 1 丈 = 100 寸
尺_to_寸 = 10   # 1 尺 = 10 寸

# Given data
句高 = 1 * 丈_to_寸 + 2 * 尺_to_寸  # 句高 = 1丈2尺 = 120寸
下股 = 2 * 丈_to_寸 + 3 * 尺_to_寸 + 1  # 下股 = 2丈3尺1寸 = 231寸
前望股裏 = 1 * 丈_to_寸 + 8  # 前望股裏 = 1丈8寸 = 108寸
北行 = 22  # 北行 = 22步
上登 = 51  # 上登 = 51步
上股 = 2 * 丈_to_寸 + 2 * 尺_to_寸  # 上股 = 2丈2尺 = 220寸

# Step 1: Calculate the 法 (divisor)
# 法 = (句高 * 下股 / 上股) - 句高
法 = Fraction(句高 * 下股, 上股) - 句高

# Step 2: Calculate the 實 (numerator)
# 實 = 北行 * 句高 * 入股裏 / 上股 - 上登
實 = Fraction(北行 * 句高, 上股) - 上登

# Step 3: Calculate 津廣
# 津廣 = 實 / 法
津廣 = Fraction(實, 法)

# Convert 津廣 to 里 (1里 = 1800寸)
寸_to_里 = 1800
津廣_in_里 = Fraction(津廣, 寸_to_里)

# Final answer
a = 津廣_in_里
print(f"津廣 = {a} 里")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Unit Conversion:**
   - All measurements are converted to the smallest unit (`寸`) for consistency.
   - 1 丈 = 10 尺 = 100 寸, 1 尺 = 10 寸.

2. **Step-by-Step Calculation:**
   - The divisor (`法`) is calculated using the formula:  
     \[
     法 = \frac{\text{句高} \times \text{下股}}{\text{上股}} - \text{句高}
     \]
   - The numerator (`實`) is calculated using the formula:  
     \[
     實 = \frac{\text{北行} \times \text{句高}}{\text{上股}} - \text{上登}
     \]
   - The width of the river (`津廣`) is then:  
     \[
     津廣 = \frac{\text{實}}{\text{法}}
     \]

3. **Conversion to 里:**
   - Since the final answer is required in `里`, the result is divided by 1800 (1里 = 1800寸).

---

### Final Output:
The program will output the width of the river (`津廣`) in `里`.
"""


"""
Variable 'a' has wrong value. Expected: 117/50, Actual: -13/3600"""
