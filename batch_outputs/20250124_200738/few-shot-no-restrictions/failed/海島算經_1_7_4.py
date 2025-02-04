"""
今有登山望津，津在山南。偃矩山上，令句高一丈二尺。從句端斜望津南岸，入下股二丈三尺一寸。又望津北岸，入前望股裏一丈八寸。更登高巖北，卻行二十二步，上登五十一步，偃矩山上。更從句端斜望津南岸，入上股二丈二尺。問津廣幾何？
術曰：以句高乘下股，如上股而一。所得以句高減之，餘為法；置北行，以句高乘之，如上股而一。所得以減上登，餘以乘入股裏為實。實如法而一，即得津廣。
答曰： a里 。
"""

"""
This is a classic ancient Chinese geometry problem involving the use of right triangles and proportional reasoning to calculate the width of a river (津廣). Let's translate the problem and solution into Python step by step.

---

### Problem Breakdown:
1. **Given:**
   - The height of the mountain (句高) is 1 丈 2 尺 (12 尺).
   - From the top of the mountain, looking diagonally to the south bank of the river (津南岸), the lower leg (入下股) is 2 丈 3 尺 1 寸 (231 寸).
   - Looking diagonally to the north bank of the river (津北岸), the forward leg (入前望股裏) is 1 丈 8 寸 (18 寸).
   - Moving to a higher peak to the north:
     - Retreat 22 步 (北行).
     - Ascend 51 步 (上登).
   - From the higher peak, looking diagonally to the south bank of the river, the upper leg (入上股) is 2 丈 2 尺 (220 寸).

2. **Question:**
   - What is the width of the river (津廣)?

3. **Procedure:**
   - Use the given relationships between the legs of the triangles and the height of the mountain to calculate the width of the river.

---

### Python Code Implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Convert all measurements to a consistent unit (寸, smallest unit)
# 1 丈 = 10 尺, 1 尺 = 10 寸
句高 = 1 * 10 * 10 + 2 * 10  # 1 丈 2 尺 = 120 寸
入下股 = 2 * 10 * 10 + 3 * 10 + 1  # 2 丈 3 尺 1 寸 = 231 寸
入前望股裏 = 1 * 10 + 8  # 1 丈 8 寸 = 18 寸
北行 = 22  # 22 步
上登 = 51  # 51 步
入上股 = 2 * 10 * 10 + 2 * 10  # 2 丈 2 尺 = 220 寸

# Step 1: Calculate the 法 (divisor)
# 法 = (句高 * 入下股) / 入上股 - 句高
法 = Fraction(句高 * 入下股, 入上股) - 句高

# Step 2: Calculate the 實 (numerator)
# 實 = ((北行 * 句高) / 入上股 - 上登) * 入前望股裏
實 = (Fraction(北行 * 句高, 入上股) - 上登) * 入前望股裏

# Step 3: Calculate the width of the river (津廣)
# 津廣 = 實 / 法
津廣 = Fraction(實, 法)

# Convert the result back to 丈 for the final answer
津廣_in_丈 = 津廣 / (10 * 10)  # Convert from 寸 to 丈

# Output the result
a = 津廣_in_丈
print(f"津廣 = {a} 丈")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Unit Conversion:**
   - All measurements are converted to the smallest unit, 寸, for consistency.
   - This avoids errors in calculations due to mixed units.

2. **法 Calculation:**
   - The divisor (法) is calculated using the formula provided in the problem:
     \[
     法 = \frac{\text{句高} \times \text{入下股}}{\text{入上股}} - \text{句高}
     \]

3. **實 Calculation:**
   - The numerator (實) is calculated using the formula:
     \[
     實 = \left(\frac{\text{北行} \times \text{句高}}{\text{入上股}} - \text{上登}\right) \times \text{入前望股裏}
     \]

4. **津廣 Calculation:**
   - The width of the river (津廣) is obtained by dividing 實 by 法:
     \[
     津廣 = \frac{\text{實}}{\text{法}}
     \]

5. **Final Conversion:**
   - The result is converted back to 丈 for the final answer.

---

### Example Output:
If you run the code, it will calculate the width of the river (津廣) in 丈. The result will be stored in `a`.
"""


"""
Variable 'a' has wrong value. Expected: 117/50, Actual: -117/100"""
