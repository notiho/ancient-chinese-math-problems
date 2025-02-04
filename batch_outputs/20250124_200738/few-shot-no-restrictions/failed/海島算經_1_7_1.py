"""
今有登山望津，津在山南。偃矩山上，令句高一丈二尺。從句端斜望津南岸，入下股二丈三尺一寸。又望津北岸，入前望股裏一丈八寸。更登高巖北，卻行二十二步，上登五十一步，偃矩山上。更從句端斜望津南岸，入上股二丈二尺。問津廣幾何？
術曰：以句高乘下股，如上股而一。所得以句高減之，餘為法；置北行，以句高乘之，如上股而一。所得以減上登，餘以乘入股裏為實。實如法而一，即得津廣。
答曰： a里 。
"""

"""
This is a classic ancient Chinese geometry problem involving right triangles and proportional reasoning. Let's break it down step by step and translate it into Python code.

### Problem Breakdown:
1. **Given:**
   - The height of the mountain (`句高`) is 1丈2尺 = 12尺.
   - From the top of the mountain, looking diagonally to the south bank of the river (`津南岸`), the lower leg (`下股`) is 2丈3尺1寸 = 23尺1寸 = 231寸.
   - Looking diagonally to the north bank of the river (`津北岸`), the forward leg (`前望股裏`) is 1丈8寸 = 18寸.
   - Moving north to a higher cliff:
     - Walk backward 22 steps (`北行`).
     - Ascend 51 steps (`上登`).
   - From the new height, looking diagonally to the south bank of the river, the upper leg (`上股`) is 2丈2尺 = 22尺.

2. **Question:**
   - What is the width of the river (`津廣`)?

3. **Procedure:**
   - Multiply the mountain height (`句高`) by the lower leg (`下股`) and divide by the upper leg (`上股`).
   - Subtract the mountain height from the result to get the divisor (`法`).
   - Multiply the backward steps (`北行`) by the mountain height and divide by the upper leg (`上股`).
   - Subtract the result from the ascending steps (`上登`).
   - Multiply the remainder by the forward leg (`入股裏`) to get the dividend (`實`).
   - Divide the dividend by the divisor to get the width of the river (`津廣`).

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
句高 = 12  # Mountain height in 尺
下股 = 231  # Lower leg in 寸
上股 = 220  # Upper leg in 寸
入股裏 = 18  # Forward leg in 寸
北行 = 22  # Backward steps
上登 = 51  # Ascending steps

# Step 1: Calculate the divisor (法)
法 = Fraction(句高 * 下股, 上股) - 句高

# Step 2: Calculate the dividend (實)
實 = (Fraction(北行 * 句高, 上股) - 上登) * 入股裏

# Step 3: Calculate the width of the river (津廣)
津廣 = Fraction(實, 法)

# Convert the result to 里 (1里 = 300步 = 1800尺 = 18000寸)
津廣_里 = Fraction(津廣, 18000)

# Output the result
a = 津廣_里
print(f"津廣: {a} 里")
#----- content ends here -----


"""


---

### Explanation of Units:
- 1丈 = 10尺
- 1尺 = 10寸
- 1里 = 300步 = 1800尺 = 18000寸

### Final Answer:
The width of the river (`津廣`) is `a` 里.
"""


"""
Variable 'a' has wrong value. Expected: 117/50, Actual: -83/1000"""
