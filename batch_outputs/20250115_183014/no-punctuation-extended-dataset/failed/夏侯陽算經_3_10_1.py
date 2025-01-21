"""
今有絹一千二百二十五匹三丈七尺五寸欲送州每匹一十五文充腳竝於身内抽給其絹時估毎匹一貫一百文問正及腳各幾何
術曰置絹數於丈尺已下折半五因以時估一貫一百文乗得一千六百七十八貫五百三十一文二分五氂復置一貫一百文加一十五文為法除得一千五百五匹不盡四百五十六文二分五氂進位四因之得一萬八千二百五十以下法除之得一丈六尺三寸不盡者與法退位倍之得二百二十三分寸之一百五十一欲知腳價者置元絹數丈尺寸折半五因又以腳錢一十五文乗之得二萬二千八百八十九文六氂二毫半以一貫一百一十五文為法除得二十匹不盡五百八十九文六氂二毫半進位四因之得二萬三千五百六十二文半以下法除之得二丈一尺一寸不盡者如前約之得二百二十三分寸之七十二
答曰正 a匹 b丈 腳 c匹 d丈
"""

"""
This problem involves calculating the number of silk rolls (絹) and their lengths that are allocated for the main payment (正) and the additional payment (腳). The procedure is complex and involves multiple steps of division, multiplication, and handling remainders. Below is the Python implementation of the procedure:


"""


from fractions import Fraction

# 絹一千二百二十五匹三丈七尺五寸
絹匹數 = 1225
絹長度 = 3 + Fraction(7, 10) + Fraction(5, 100)  # Convert 丈尺寸 to a single fractional value

# 每匹一貫一百文 (時估)
時估 = 1 + Fraction(100, 1000)  # 1貫100文 = 1.1貫

# 每匹腳錢一十五文
腳錢 = Fraction(15, 1000)  # 15文 = 0.015貫

# 置絹數於丈尺已下折半五因
絹總長度 = 絹匹數 * 絹長度  # Total length of silk
絹總長度_折半五因 = 絹總長度 * Fraction(5, 2)  # Multiply by 5/2

# 時估乘之
總價值 = 絹匹數 * 時估  # Total value of silk in 貫

# 加腳錢為法
法 = 時估 + 腳錢  # 法 = 1.1貫 + 0.015貫 = 1.115貫

# 除得正匹數
正匹數 = int(總價值 // 法)  # Integer division to get the number of 正匹
正匹餘數 = 總價值 % 法  # Remainder after division

# 餘數進位四因之
正匹餘數_進位 = 正匹餘數 * 4

# 以下法除之得正長度
正長度 = 正匹餘數_進位 / 法

# 不盡者與法退位倍之
正長度_不盡 = 正長度 % 1  # Fractional part of 正長度
正長度_退位 = 正長度_不盡 * 2

# 正長度最終值
正長度_最終 = int(正長度) + Fraction(正長度_退位, 1)

# 欲知腳價者置元絹數丈尺寸折半五因
腳價值 = 絹總長度_折半五因 * 腳錢  # Total value of additional payment (腳)

# 以法除得腳匹數
腳匹數 = int(腳價值 // 法)  # Integer division to get the number of 腳匹
腳匹餘數 = 腳價值 % 法  # Remainder after division

# 餘數進位四因之
腳匹餘數_進位 = 腳匹餘數 * 4

# 以下法除之得腳長度
腳長度 = 腳匹餘數_進位 / 法

# 不盡者與法退位倍之
腳長度_不盡 = 腳長度 % 1  # Fractional part of 腳長度
腳長度_退位 = 腳長度_不盡 * 2

# 腳長度最終值
腳長度_最終 = int(腳長度) + Fraction(腳長度_退位, 1)

# 答案
a = 正匹數
b = 正長度_最終
c = 腳匹數
d = 腳長度_最終

print(f"正 {a}匹 {b}丈 腳 {c}匹 {d}丈")


"""


### Explanation of Variables:
1. `絹匹數`: Total number of silk rolls (1225).
2. `絹長度`: Length of each silk roll in 丈, 尺, 寸 converted to a single fractional value.
3. `時估`: Value of each silk roll (1貫100文 = 1.1貫).
4. `腳錢`: Additional payment per silk roll (15文 = 0.015貫).
5. `法`: The divisor used for calculating 正 and 腳 (1.115貫).
6. `正匹數`: Number of silk rolls allocated for the main payment (正).
7. `正長度_最終`: Total length of silk rolls allocated for the main payment (正).
8. `腳匹數`: Number of silk rolls allocated for the additional payment (腳).
9. `腳長度_最終`: Total length of silk rolls allocated for the additional payment (腳).

### Final Answer:
The program calculates the number of silk rolls and their lengths for both the main payment (正) and the additional payment (腳).
"""


"""
Variable 'a' has wrong value. Expected: 1505, Actual: 1208
Variable 'b' has wrong value. Expected: 365/223, Actual: 482/223
Variable 'c' has wrong value. Expected: 20, Actual: 154
Variable 'd' has wrong value. Expected: 1885/892, Actual: 666/223"""
