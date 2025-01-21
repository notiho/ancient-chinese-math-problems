"""
今有絹一千二百二十五匹三丈七尺五寸欲送州每匹一十五文充腳竝於身内抽給其絹時估毎匹一貫一百文問正及腳各幾何
術曰置絹數於丈尺已下折半五因以時估一貫一百文乗得一千六百七十八貫五百三十一文二分五氂復置一貫一百文加一十五文為法除得一千五百五匹不盡四百五十六文二分五氂進位四因之得一萬八千二百五十以下法除之得一丈六尺三寸不盡者與法退位倍之得二百二十三分寸之一百五十一欲知腳價者置元絹數丈尺寸折半五因又以腳錢一十五文乗之得二萬二千八百八十九文六氂二毫半以一貫一百一十五文為法除得二十匹不盡五百八十九文六氂二毫半進位四因之得二萬三千五百六十二文半以下法除之得二丈一尺一寸不盡者如前約之得二百二十三分寸之七十二
答曰正 a匹 b丈 腳 c匹 d丈
"""

"""
This problem is quite complex and involves multiple steps of ancient Chinese arithmetic. Let's carefully translate the procedure into Python code step by step:

### Problem Description:
We have 1225 bolts of silk, each 3 zhang, 7 chi, and 5 cun in length. Each bolt is valued at 1 guan and 100 wen. When sending the silk to the state, 15 wen per bolt is deducted for transportation costs ("脚"). The silk is also partially deducted from the total to cover these costs. The question asks for the number of bolts ("正") and the length of silk ("脚") used for transportation costs.

### Procedure:
The procedure involves multiple calculations:
1. Calculate the total value of the silk.
2. Determine the number of bolts used for the main delivery ("正") and the remainder.
3. Calculate the length of silk used for transportation costs ("脚").
4. Determine the value of the transportation costs in bolts and lengths.

### Python Code:


"""


from fractions import Fraction

# 絹一千二百二十五匹三丈七尺五寸
絹匹數 = 1225
每匹長度 = 3 + Fraction(7, 10) + Fraction(5, 100)  # Convert 3丈7尺5寸 to a fractional value in 丈

# 每匹一貫一百文
每匹估價 = 1 * 1000 + 100  # 1貫 = 1000文, so 1貫100文 = 1100文

# 每匹一十五文充腳
每匹腳錢 = 15

# Step 1: Calculate the total value of the silk
# 置絹數於丈尺已下折半五因以時估一貫一百文乘
總價值 = 絹匹數 * 每匹估價

# Step 2: Add the transportation cost to the value of each bolt
# 復置一貫一百文加一十五文為法
法 = 每匹估價 + 每匹腳錢

# Step 3: Determine the number of bolts for the main delivery ("正")
# 除得正匹數
正匹數 = 總價值 // 法  # Integer division to get the number of bolts
剩餘文 = 總價值 % 法  # Remainder in 文

# Step 4: Convert the remainder to length
# 進位四因之
剩餘文進位 = 剩餘文 * 4

# 以下法除之
剩餘長度 = 剩餘文進位 / 法  # Length in 丈

# 不盡者與法退位倍之
不盡部分 = 剩餘文進位 % 法
退位倍之 = 不盡部分 * 2

# Step 5: Calculate the transportation cost ("腳")
# 置元絹數丈尺寸折半五因又以腳錢一十五文乘之
腳總價值 = 絹匹數 * 每匹長度 * 每匹腳錢

# 以下法除之
腳匹數 = 腳總價值 // 法
腳剩餘文 = 腳總價值 % 法

# 進位四因之
腳剩餘文進位 = 腳剩餘文 * 4

# 以下法除之
腳剩餘長度 = 腳剩餘文進位 / 法

# 不盡者如前約之
腳不盡部分 = 腳剩餘文進位 % 法
腳退位倍之 = 腳不盡部分 * 2

# Final Results
a = 正匹數
b = 剩餘長度
c = 腳匹數
d = 腳剩餘長度

print(f"正 {a}匹 {b}丈, 腳 {c}匹 {d}丈")


"""


### Explanation of Variables:
- `正匹數 (a)`: The number of bolts used for the main delivery.
- `剩餘長度 (b)`: The remaining length of silk in zhang.
- `腳匹數 (c)`: The number of bolts used for transportation costs.
- `腳剩餘長度 (d)`: The remaining length of silk used for transportation costs in zhang.

### Notes:
1. The calculations use fractions (`Fraction`) to ensure precision, as ancient Chinese math often dealt with fractional units.
2. The units of measurement (丈, 尺, 寸) are converted into a single unit (丈) for simplicity.
3. The procedure follows the ancient algorithm step by step, including handling remainders and converting them into lengths.
"""


"""
Variable 'a' has wrong value. Expected: 1505, Actual: 1208
Variable 'b' has wrong value. Expected: 365/223, Actual: 2.0807174887892375
Variable 'c' has wrong value. Expected: 20, Actual: 61
Variable 'd' has wrong value. Expected: 1885/892, Actual: 713/223"""
