"""
今有絹一千二百二十五匹三丈七尺五寸欲送州每匹一十五文充腳竝於身内抽給其絹時估毎匹一貫一百文問正及腳各幾何
術曰置絹數於丈尺已下折半五因以時估一貫一百文乗得一千六百七十八貫五百三十一文二分五氂復置一貫一百文加一十五文為法除得一千五百五匹不盡四百五十六文二分五氂進位四因之得一萬八千二百五十以下法除之得一丈六尺三寸不盡者與法退位倍之得二百二十三分寸之一百五十一欲知腳價者置元絹數丈尺寸折半五因又以腳錢一十五文乗之得二萬二千八百八十九文六氂二毫半以一貫一百一十五文為法除得二十匹不盡五百八十九文六氂二毫半進位四因之得二萬三千五百六十二文半以下法除之得二丈一尺一寸不盡者如前約之得二百二十三分寸之七十二
答曰正 a匹 腳 b匹
"""

"""
This problem involves calculating the number of "正" (main) and "腳" (extra) silk rolls distributed based on their prices and contributions. Below is the Python implementation of the procedure described in the problem:


"""

#----- content starts here -----

from fractions import Fraction

# 絹一千二百二十五匹三丈七尺五寸
絹匹數 = 1225
絹長度 = Fraction(3 * 10 + 7, 10) + Fraction(5, 100)  # Convert 3丈7尺5寸 to a fraction in terms of 丈

# 每匹一貫一百文
時估 = 1 * 1000 + 100  # Convert 1貫1百文 to 文

# 每匹腳錢一十五文
腳錢 = 15

# 置絹數於丈尺已下折半五因
絹總長度 = 絹匹數 * 絹長度
絹總長度_折半五因 = 絹總長度 * Fraction(1, 2) * 5

# 以時估一貫一百文乘
總價值 = 絹總長度_折半五因 * 時估

# 加一十五文為法
法 = 時估 + 腳錢

# 除得正匹數
正匹數 = int(總價值 // 法)

# 不盡部分
不盡部分 = 總價值 % 法

# 進位四因之
進位後 = 不盡部分 * 4

# 以下法除之
剩餘長度 = Fraction(進位後, 法)

# 求腳匹數
腳價值 = 絹總長度_折半五因 * 腳錢
腳匹數 = int(腳價值 // 法)

# 不盡部分
腳不盡部分 = 腳價值 % 法

# 進位四因之
腳進位後 = 腳不盡部分 * 4

# 以下法除之
腳剩餘長度 = Fraction(腳進位後, 法)

# 答案
a = 正匹數
b = 腳匹數
#----- content ends here -----


"""


### Explanation:
1. **絹總長度**: The total length of silk is calculated by multiplying the number of rolls by the length of each roll (converted to a fraction).
2. **絹總長度_折半五因**: The total length is halved and multiplied by 5, as per the procedure.
3. **總價值**: The total value of the silk is calculated by multiplying the adjusted length by the price per roll.
4. **法**: The divisor is the price per roll plus the extra contribution (腳錢).
5. **正匹數**: The number of "正" rolls is obtained by dividing the total value by the divisor.
6. **不盡部分**: The remainder from the division is used to calculate the remaining length.
7. **腳匹數**: The number of "腳" rolls is calculated similarly, using the extra contribution (腳錢).

### Final Answer:
- 正匹數 (`a`) is the number of main rolls.
- 腳匹數 (`b`) is the number of extra rolls.
"""


"""
Variable 'a' has wrong value. Expected: 1342825/892, Actual: 11329
Variable 'b' has wrong value. Expected: 73245/3568, Actual: 154"""
