"""
今有登山望津，津在山南。偃矩山上，令句高一丈二尺。從句端斜望津南岸，入下股二丈三尺一寸。又望津北岸，入前望股裏一丈八寸。更登高巖北，卻行二十二步，上登五十一步，偃矩山上。更從句端斜望津南岸，入上股二丈二尺。問津廣幾何？
術曰：以句高乘下股，如上股而一。所得以句高減之，餘為法；置北行，以句高乘之，如上股而一。所得以減上登，餘以乘入股裏為實。實如法而一，即得津廣。
答曰： a里 。
"""

"""
This is a classic ancient Chinese geometry problem involving right triangles and proportions. Let's break it down step by step and translate the procedure into Python code.

### Problem Breakdown:
1. **Given:**
   - The height of the mountain (`句高`) is 1 丈 2 尺 (12 尺).
   - From the top of the mountain, looking diagonally to the south bank of the river (`津南岸`), the line enters the lower leg (`下股`) by 2 丈 3 尺 1 寸 (231 寸).
   - Looking diagonally to the north bank of the river (`津北岸`), the line enters the forward leg (`前望股裏`) by 1 丈 8 寸 (18 寸).
   - Moving north, the observer walks back 22 步 and climbs 51 步 to reach a higher peak.
   - From the higher peak, looking diagonally to the south bank of the river, the line enters the upper leg (`上股`) by 2 丈 2 尺 (220 寸).

2. **Question:**
   - What is the width of the river (`津廣`)?

3. **Procedure:**
   - Multiply the height of the mountain (`句高`) by the lower leg (`下股`), divide by the upper leg (`上股`), and subtract the height of the mountain to get the divisor (`法`).
   - Multiply the northward walk (`北行`) by the height of the mountain, divide by the upper leg (`上股`), and subtract the climb (`上登`).
   - Multiply the result by the forward leg (`入股裏`) to get the dividend (`實`).
   - Divide the dividend by the divisor to get the width of the river.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Convert all measurements to 寸 (smallest unit for consistency)
# 1 丈 = 10 尺, 1 尺 = 10 寸

# Given values
句高 = 1 * 10 * 10 + 2 * 10  # 1 丈 2 尺 = 120 寸
下股 = 2 * 10 * 10 + 3 * 10 + 1  # 2 丈 3 尺 1 寸 = 231 寸
前望股裏 = 1 * 10 * 10 + 8  # 1 丈 8 寸 = 108 寸
北行 = 22  # 22 步
上登 = 51  # 51 步
上股 = 2 * 10 * 10 + 2 * 10  # 2 丈 2 尺 = 220 寸

# Step 1: Calculate the divisor (法)
法 = Fraction(句高 * 下股, 上股) - 句高

# Step 2: Calculate the dividend (實)
實 = (Fraction(北行 * 句高, 上股) - 上登) * 前望股裏

# Step 3: Calculate the width of the river (津廣)
津廣 = Fraction(實, 法)

# Convert the result to 里 (1 里 = 1800 寸)
津廣_里 = Fraction(津廣, 1800)

# Output the result
a = 津廣_里
print(f"津廣 = {a} 里")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Unit Conversion:**
   - All measurements are converted to the smallest unit, `寸`, for consistency.
   - 1 丈 = 10 尺, 1 尺 = 10 寸.

2. **Divisor Calculation (`法`):**
   - Multiply the height of the mountain (`句高`) by the lower leg (`下股`), divide by the upper leg (`上股`), and subtract the height of the mountain.

3. **Dividend Calculation (`實`):**
   - Multiply the northward walk (`北行`) by the height of the mountain (`句高`), divide by the upper leg (`上股`), subtract the climb (`上登`), and multiply by the forward leg (`前望股裏`).

4. **River Width (`津廣`):**
   - Divide the dividend (`實`) by the divisor (`法`) to get the width of the river in `寸`.
   - Convert the result to `里` (1 里 = 1800 寸).

---

### Example Output:
If you run the code, it will calculate the width of the river (`津廣`) in `里`. The result will be stored in the variable `a`.
"""


"""
Variable 'a' has wrong value. Expected: 117/50, Actual: -39/100"""
