"""
今有絹一千二百二十五匹三丈七尺五寸欲送州每匹一十五文充腳竝於身内抽給其絹時估毎匹一貫一百文問正及腳各幾何
術曰置絹數於丈尺已下折半五因以時估一貫一百文乗得一千六百七十八貫五百三十一文二分五氂復置一貫一百文加一十五文為法除得一千五百五匹不盡四百五十六文二分五氂進位四因之得一萬八千二百五十以下法除之得一丈六尺三寸不盡者與法退位倍之得二百二十三分寸之一百五十一欲知腳價者置元絹數丈尺寸折半五因又以腳錢一十五文乗之得二萬二千八百八十九文六氂二毫半以一貫一百一十五文為法除得二十匹不盡五百八十九文六氂二毫半進位四因之得二萬三千五百六十二文半以下法除之得二丈一尺一寸不盡者如前約之得二百二十三分寸之七十二
答曰正 a匹 b丈 腳 c匹 d丈
"""

"""
This problem involves a complex calculation involving silk, its valuation, and distribution between the main portion ("正") and the additional portion ("腳"). Below is the Python implementation of the procedure described in the problem.


"""


from fractions import Fraction

# 絹一千二百二十五匹三丈七尺五寸
絹匹數 = 1225
絹長度 = 3 + Fraction(7, 10) + Fraction(5, 100)  # Convert 丈尺寸 to a single value in 丈

# 每匹一貫一百文 (時估)
時估 = 1 + Fraction(100, 1000)  # 1貫100文 = 1.1貫

# 每匹腳錢一十五文
腳錢 = Fraction(15, 1000)  # 15文 = 0.015貫

# 置絹數於丈尺已下折半五因
絹總長度 = 絹匹數 * 絹長度  # Total length of silk
絹總長度_折半五因 = 絹總長度 * Fraction(5, 2)

# 時估乘之
總價值 = 絹匹數 * 時估

# 加腳錢為法
法 = 時估 + 腳錢

# 除得正匹數
正匹數 = int(總價值 // 法)  # 正匹數 (integer part)
剩餘價值 = 總價值 % 法  # Remaining value after division

# 剩餘價值進位四因之
剩餘價值_進位 = 剩餘價值 * 4

# 以下法除之得正長度
正長度 = 剩餘價值_進位 / 法

# 不盡者與法退位倍之
正長度_餘數 = 正長度 % 1  # Fractional part of 正長度
正長度_餘數_退位 = 正長度_餘數 * 2

# 折算為分寸
正長度_分寸 = Fraction(正長度_餘數_退位 * 100, 1)

# 計算腳價
腳價值 = 絹總長度_折半五因 * 腳錢

# 以法除得腳匹數
腳匹數 = int(腳價值 // 法)  # 腳匹數 (integer part)
腳剩餘價值 = 腳價值 % 法  # Remaining value after division

# 腳剩餘價值進位四因之
腳剩餘價值_進位 = 腳剩餘價值 * 4

# 以下法除之得腳長度
腳長度 = 腳剩餘價值_進位 / 法

# 不盡者與法退位倍之
腳長度_餘數 = 腳長度 % 1  # Fractional part of 腳長度
腳長度_餘數_退位 = 腳長度_餘數 * 2

# 折算為分寸
腳長度_分寸 = Fraction(腳長度_餘數_退位 * 100, 1)

# 答案
a = 正匹數
b = 正長度
c = 腳匹數
d = 腳長度

print(f"正 {a}匹 {b}丈")
print(f"腳 {c}匹 {d}丈")


"""


### Explanation:
1. **絹數與長度計算**:
   - The total length of silk is calculated by multiplying the number of silk pieces by their length in 丈, 尺, 寸.
   - The length is then adjusted using the "折半五因" rule.

2. **正匹數計算**:
   - The total value of the silk is calculated using the given valuation (時估).
   - The divisor (法) is the valuation plus the additional cost (腳錢).
   - The integer part of the division gives the number of 正匹數, and the remainder is used to calculate the 正長度.

3. **腳匹數計算**:
   - The remaining value is used to calculate the number of additional pieces (腳匹數) and their corresponding length (腳長度).

4. **進位與退位**:
   - Remaining fractional values are adjusted using the "進位四因之" and "退位倍之" rules to refine the results.

5. **結果輸出**:
   - The results are presented as the number of 正匹數 and 腳匹數, along with their respective lengths in 丈.

This implementation follows the procedure described in the problem and provides the required results.
"""


"""
Variable 'a' has wrong value. Expected: 1505, Actual: 1208
Variable 'b' has wrong value. Expected: 365/223, Actual: 464/223
Variable 'c' has wrong value. Expected: 20, Actual: 154
Variable 'd' has wrong value. Expected: 1885/892, Actual: 889/446"""
