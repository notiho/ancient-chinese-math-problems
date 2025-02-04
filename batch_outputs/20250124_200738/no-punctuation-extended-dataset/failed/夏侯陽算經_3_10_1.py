"""
今有絹一千二百二十五匹三丈七尺五寸欲送州每匹一十五文充腳竝於身内抽給其絹時估毎匹一貫一百文問正及腳各幾何
術曰置絹數於丈尺已下折半五因以時估一貫一百文乗得一千六百七十八貫五百三十一文二分五氂復置一貫一百文加一十五文為法除得一千五百五匹不盡四百五十六文二分五氂進位四因之得一萬八千二百五十以下法除之得一丈六尺三寸不盡者與法退位倍之得二百二十三分寸之一百五十一欲知腳價者置元絹數丈尺寸折半五因又以腳錢一十五文乗之得二萬二千八百八十九文六氂二毫半以一貫一百一十五文為法除得二十匹不盡五百八十九文六氂二毫半進位四因之得二萬三千五百六十二文半以下法除之得二丈一尺一寸不盡者如前約之得二百二十三分寸之七十二
答曰正 a匹 腳 b匹
"""

"""
This problem involves calculating the distribution of silk (絹) and its associated costs, based on the given rates and rules. Here's the solution encoded in Python:


"""

#----- content starts here -----

from fractions import Fraction

# 絹一千二百二十五匹三丈七尺五寸
絹匹數 = 1225
絹長度_丈 = 3
絹長度_尺 = 7
絹長度_寸 = 5

# 每匹一貫一百文 (時估)
時估 = 1 * 1000 + 100  # 一貫一百文 in 文
腳錢 = 15  # 每匹腳錢

# Step 1: Calculate the total value of the silk
# 置絹數於丈尺已下折半五因
總長度_寸 = 絹長度_丈 * 100 + 絹長度_尺 * 10 + 絹長度_寸
總長度_寸 = Fraction(總長度_寸, 2)  # 折半
總價值 = (絹匹數 * 時估) + (總長度_寸 * 時估 / 10)

# Step 2: Add the cost of the "腳錢" and calculate the divisor
# 復置一貫一百文加一十五文為法
法 = 時估 + 腳錢

# Step 3: Calculate the 正 (main) silk distribution
# 除得正匹數
正匹數 = int(總價值 // 法)

# Step 4: Calculate the remaining value after 正匹數
# 不盡部分
剩餘文 = 總價值 % 法

# Step 5: Calculate the "腳" (additional) silk distribution
# 進位四因之
剩餘文進位 = 剩餘文 * 4

# 以下法除之
腳匹數 = int(剩餘文進位 // 法)

# Final Answer
a = 正匹數
b = 腳匹數

print(f"正 {a}匹 腳 {b}匹")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Input Values**: The silk quantity and dimensions are converted into a unified unit (寸) for easier calculations.
2. **Total Value Calculation**: The total value of the silk is calculated by multiplying the number of silk pieces by their estimated price and adding the length-based value.
3. **Main Silk Distribution (正匹數)**: The total value is divided by the combined cost of one silk piece and its associated "腳錢" to determine the main distribution.
4. **Remaining Value and Additional Distribution (腳匹數)**: The remainder is scaled up (multiplied by 4) and divided again to calculate the additional distribution.

### Final Answer:
The values of `a` (正匹數) and `b` (腳匹數) are the main and additional distributions of silk, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 1342825/892, Actual: 1227
Variable 'b' has wrong value. Expected: 73245/3568, Actual: 0"""
