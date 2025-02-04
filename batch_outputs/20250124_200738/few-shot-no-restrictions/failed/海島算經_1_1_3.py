"""
今有望松生山上，不知高下。立兩表齊，高二丈，前後相去五十步，令後表與前表參相直。從前表卻行七步四尺，薄地遙望松末，與表端參合。又望松本，入表二尺八寸。复從後表卻行八步五尺，薄地遙望松末，亦與表端參合。問松高及山去表各幾何？
術曰：以入表乘表間為實。相多為法，除之。加入表，即得松高。求表去山遠近者：置表間，以前表卻行乘之為實。相多為法，除之，得山去表。
答曰：松高 a丈 ；山去表 b里 。
"""

"""
This is a classic ancient Chinese surveying problem involving similar triangles to calculate the height of a tree (松) on a mountain and the horizontal distance from the mountain to the observation point (表). Let's break it down step by step and encode it in Python.

### Problem Breakdown:
1. Two poles (表) of height 2 丈 are placed, separated by a distance of 50 步.
2. Observations are made from two positions:
   - From the first position (7 步 4 尺 away from the front pole), the top of the tree aligns with the top of the pole, and the base of the tree aligns 2 尺 8 寸 into the pole.
   - From the second position (8 步 5 尺 away from the rear pole), the top of the tree also aligns with the top of the pole.

### Procedure:
1. To calculate the height of the tree (松高):
   - Multiply the "入表" (how much the tree base aligns into the pole) by the distance between the poles (表間).
   - Use the difference between the two observation distances as the divisor.
   - Add the height of the pole to get the total height of the tree.

2. To calculate the horizontal distance from the mountain to the pole (山去表):
   - Multiply the distance between the poles (表間) by the first observation distance.
   - Use the difference between the two observation distances as the divisor.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Constants
表高 = 2  # Height of the pole in 丈
表間 = 50  # Distance between the two poles in 步

# Observations
前表卻行 = 7 + Fraction(4, 10)  # 7 步 4 尺 (convert 尺 to decimal 步)
入表 = 2 + Fraction(8, 10)  # 2 尺 8 寸 (convert 尺 and 寸 to decimal 步)
後表卻行 = 8 + Fraction(5, 10)  # 8 步 5 尺 (convert 尺 to decimal 步)

# Step 1: Calculate 松高 (height of the tree)
相多 = 後表卻行 - 前表卻行  # Difference between the two observation distances
實_松高 = 入表 * 表間  # Multiply 入表 by 表間
松高 = Fraction(實_松高, 相多) + 表高  # Divide by 相多 and add the height of the pole

# Step 2: Calculate 山去表 (horizontal distance to the mountain)
實_山去表 = 表間 * 前表卻行  # Multiply 表間 by the first observation distance
山去表 = Fraction(實_山去表, 相多)  # Divide by 相多

# Convert 松高 to 丈 and 山去表 to 里 (1 里 = 180 步)
松高_丈 = 松高  # 松高 is already in 丈
山去表_里 = 山去表 / 180  # Convert 步 to 里

# Results
a = 松高_丈
b = 山去表_里

print(f"松高: {a} 丈")
print(f"山去表: {b} 里")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Input Conversion**:
   - All measurements are converted into a consistent unit (步), with 尺 and 寸 converted to fractional 步.
   - For example, 7 步 4 尺 becomes `7 + 4/10` 步.

2. **Tree Height Calculation**:
   - The formula for tree height uses the "入表" and the difference between the two observation distances (`相多`) to calculate the height above the pole.

3. **Horizontal Distance Calculation**:
   - The formula for the horizontal distance uses the first observation distance and the same divisor (`相多`).

4. **Unit Conversion**:
   - The tree height is already in 丈, so no conversion is needed.
   - The horizontal distance is converted from 步 to 里 using the conversion factor `1 里 = 180 步`.

---

### Example Output:
If you run the code, it will calculate the height of the tree (`松高`) in 丈 and the horizontal distance to the mountain (`山去表`) in 里.
"""


"""
Variable 'a' has wrong value. Expected: 307/25, Actual: 1422/11
Variable 'b' has wrong value. Expected: 23/21, Actual: 185/99"""
