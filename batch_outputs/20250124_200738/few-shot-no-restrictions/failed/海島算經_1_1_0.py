"""
今有望松生山上，不知高下。立兩表齊，高二丈，前後相去五十步，令後表與前表參相直。從前表卻行七步四尺，薄地遙望松末，與表端參合。又望松本，入表二尺八寸。复從後表卻行八步五尺，薄地遙望松末，亦與表端參合。問松高及山去表各幾何？
術曰：以入表乘表間為實。相多為法，除之。加入表，即得松高。求表去山遠近者：置表間，以前表卻行乘之為實。相多為法，除之，得山去表。
答曰：松高 a丈 ；山去表 b里 。
"""

"""
This is a classic ancient Chinese surveying problem involving similar triangles to calculate the height of a tree (松高) and the distance from the base of the tree to the measuring point (山去表). Let's translate the problem and solution into Python step by step.

### Problem Breakdown:
1. Two poles (表) of height 2 丈 are placed 50 步 apart.
2. Observations are made from two points:
   - From the first point (7 步 4 尺 away from the front pole), the top of the tree aligns with the top of the pole, and the base of the tree aligns with a point 2 尺 8 寸 into the pole.
   - From the second point (8 步 5 尺 away from the rear pole), the top of the tree aligns with the top of the pole.

### Procedure:
1. To calculate the height of the tree (松高):
   - Use the formula:  
     \[
     松高 = \frac{(入表 \times 表間)}{相多} + 表高
     \]
   - Where:
     - 入表 = the distance the tree's base appears to "enter" the pole (2 尺 8 寸 = 2.8 尺).
     - 表間 = the distance between the two poles (50 步).
     - 相多 = the difference in distances walked backward (8 步 5 尺 - 7 步 4 尺).

2. To calculate the distance from the base of the tree to the front pole (山去表):
   - Use the formula:  
     \[
     山去表 = \frac{(表間 \times 前表卻行)}{相多}
     \]
   - Where:
     - 表間 = the distance between the two poles (50 步).
     - 前表卻行 = the distance walked backward from the front pole (7 步 4 尺 = 7.4 步).
     - 相多 = the difference in distances walked backward (8 步 5 尺 - 7 步 4 尺).

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Constants
表高 = 2  # 表的高度 in 丈
表間 = 50  # 表間距離 in 步

# Observations
前表卻行 = 7 + Fraction(4, 10)  # 7 步 4 尺 = 7.4 步
後表卻行 = 8 + Fraction(5, 10)  # 8 步 5 尺 = 8.5 步
入表 = 2 + Fraction(8, 10)  # 2 尺 8 寸 = 2.8 尺

# Calculations
相多 = 後表卻行 - 前表卻行  # Difference in distances walked backward

# 松高 calculation
松高 = (入表 * 表間) / 相多 + 表高

# 山去表 calculation
山去表 = (表間 * 前表卻行) / 相多

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


### Explanation of the Code:
1. **Units Conversion**: All measurements are converted into consistent units (步 or 尺) for calculations.
2. **Fraction Class**: Used to ensure precision in calculations involving fractions.
3. **松高 Calculation**: The formula for the height of the tree is implemented step by step.
4. **山去表 Calculation**: The formula for the distance from the tree to the front pole is implemented step by step.
5. **Conversion to 丈 and 里**: Final results are converted to the appropriate units for the answer.

### Final Answer:
The height of the tree (松高) is `a 丈`, and the distance from the base of the tree to the front pole (山去表) is `b 里`.
"""


"""
Variable 'a' has wrong value. Expected: 307/25, Actual: 1422/11
Variable 'b' has wrong value. Expected: 23/21, Actual: 185/99"""
