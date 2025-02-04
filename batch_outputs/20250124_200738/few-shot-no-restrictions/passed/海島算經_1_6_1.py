"""
今有望清淵，淵下有白石。偃矩岸上，令句高三尺。斜望水岸，入下股四尺五寸。望白石，入下股二尺四寸。又設重矩于上，其間相去四尺。更從句端斜望水岸，入上股四尺。以望白石，入上股二尺二寸。問水深幾何？
術曰：置望水上下股相減，餘以乘望石上股為上率。又以望石上下股相減，餘以乘望水上股為下率。兩率相減，餘以乘矩間為實；以二差相乘為法。實如法而一，得水深。
答曰： a丈 。
"""

"""
This problem involves using geometric principles to calculate the depth of water based on observations made with a measuring tool (a carpenter's square or similar device). Here's the solution translated into Python:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
句高 = 3  # 高 of the carpenter's square (in 尺)
望水_下股 = Fraction(4, 1) + Fraction(5, 10)  # 入下股 for observing the water's edge (4 尺 5 寸)
望石_下股 = Fraction(2, 1) + Fraction(4, 10)  # 入下股 for observing the white stone (2 尺 4 寸)
矩間 = 4  # Distance between the two carpenter's squares (in 尺)
望水_上股 = Fraction(4, 1)  # 入上股 for observing the water's edge (4 尺)
望石_上股 = Fraction(2, 1) + Fraction(2, 10)  # 入上股 for observing the white stone (2 尺 2 寸)

# Procedure
# Step 1: Calculate the "upper rate" (上率)
望水_上下股差 = 望水_下股 - 望水_上股
上率 = 望水_上下股差 * 望石_上股

# Step 2: Calculate the "lower rate" (下率)
望石_上下股差 = 望石_下股 - 望石_上股
下率 = 望石_上下股差 * 望水_上股

# Step 3: Calculate the depth of the water
兩率差 = 上率 - 下率
實 = 兩率差 * 矩間
法 = 望水_上下股差 * 望石_上下股差
水深 = Fraction(實, 法)

# Convert the result to 丈 (1 丈 = 10 尺)
水深_丈 = 水深 / 10

# Answer
a = 水深_丈
print(f"水深為 {a} 丈。")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Input Data**: The given measurements (in 尺 and 寸) are converted into fractions for precise calculations.
2. **Upper Rate (上率)**: Calculated using the difference in the "望水" (observing the water's edge) lower and upper 股, multiplied by the "望石" (observing the white stone) upper 股.
3. **Lower Rate (下率)**: Calculated using the difference in the "望石" lower and upper 股, multiplied by the "望水" upper 股.
4. **Depth Calculation**: The difference between the two rates (兩率差) is multiplied by the distance between the two carpenter's squares (矩間) to get the numerator (實). The denominator (法) is the product of the differences in the 股 for "望水" and "望石". The depth is then calculated as `實 / 法`.
5. **Conversion to 丈**: Since the depth is initially in 尺, it is divided by 10 to convert to 丈.

### Example Output:
If you run the code, it will calculate the depth of the water in 丈 based on the given measurements.
"""


"""
"""
