"""
今有望松生山上，不知高下。立兩表齊，高二丈，前後相去五十步，令後表與前表參相直。從前表卻行七步四尺，薄地遙望松末，與表端參合。又望松本，入表二尺八寸。复從後表卻行八步五尺，薄地遙望松末，亦與表端參合。問松高及山去表各幾何？
術曰：以入表乘表間為實。相多為法，除之。加入表，即得松高。求表去山遠近者：置表間，以前表卻行乘之為實。相多為法，除之，得山去表。
答曰：松高 a丈 ；山去表 b里 。
"""

"""
This is a classic ancient Chinese surveying problem involving similar triangles to calculate the height of a tree (松) on a mountain and the horizontal distance from the tree to a reference point (表). Let's translate the problem into Python code step by step.

### Problem Breakdown:
1. Two poles (表) of equal height (2 丈) are placed 50 步 apart.
2. Observations are made from two positions:
   - From the front pole (前表), walking back 7 步 4 尺 and observing the top and bottom of the tree.
   - From the rear pole (後表), walking back 8 步 5 尺 and observing the same.
3. Using these observations, calculate:
   - The height of the tree (松高).
   - The horizontal distance from the tree to the front pole (山去表).

### Procedure:
1. Use the given observations to form similar triangles.
2. Use the formula provided in the problem to calculate the height of the tree and the distance.

### Units:
- 1 丈 = 10 尺
- 1 里 = 300 步

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Constants
表高 = 2  # 表的高度 (2 丈)
表間 = 50  # 前後表相距 (50 步)

# Observations from the front pole
前表卻行 = 7 + Fraction(4, 10)  # 前表卻行 7 步 4 尺 (convert 尺 to 步)
前表入表 = Fraction(2, 10) + Fraction(8, 100)  # 入表 2 尺 8 寸 (convert 尺 and 寸 to 步)

# Observations from the rear pole
後表卻行 = 8 + Fraction(5, 10)  # 後表卻行 8 步 5 尺 (convert 尺 to 步)

# 松高計算 (Tree Height Calculation)
# 以入表乘表間為實
松高實 = 前表入表 * 表間

# 相多為法
松高法 = 後表卻行 - 前表卻行

# 除之，加入表，即得松高
松高 = (松高實 / 松高法) + 表高

# 山去表計算 (Distance from Tree to Front Pole)
# 置表間，以前表卻行乘之為實
山去表實 = 表間 * 前表卻行

# 相多為法
山去表法 = 後表卻行 - 前表卻行

# 除之，得山去表
山去表 = 山去表實 / 山去表法

# Convert 山去表 from 步 to 里
山去表_里 = 山去表 / 300

# Results
a = 松高  # 松高 in 丈
b = 山去表_里  # 山去表 in 里

# Output the results
print(f"松高: {a} 丈")
print(f"山去表: {b} 里")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Input Conversion**:
   - All measurements are converted into consistent units (步) for calculation.
   - Observations like "7 步 4 尺" are converted into fractional 步 using the conversion: 1 丈 = 10 尺, 1 步 = 6 尺.

2. **松高 Calculation**:
   - The formula for 松高 is derived from similar triangles:
     \[
     \text{松高} = \frac{\text{入表} \times \text{表間}}{\text{後表卻行} - \text{前表卻行}} + \text{表高}
     \]

3. **山去表 Calculation**:
   - The formula for 山去表 is:
     \[
     \text{山去表} = \frac{\text{表間} \times \text{前表卻行}}{\text{後表卻行} - \text{前表卻行}}
     \]
   - Finally, the result is converted from 步 to 里 using the conversion: 1 里 = 300 步.

4. **Output**:
   - The height of the tree (松高) is given in 丈.
   - The horizontal distance from the tree to the front pole (山去表) is given in 里.

---

### Example Output:
If you run the code, it will calculate and output the height of the tree and the distance to the mountain in the specified units.
"""


"""
Variable 'a' has wrong value. Expected: 307/25, Actual: 162/11
Variable 'b' has wrong value. Expected: 23/21, Actual: 37/33"""
