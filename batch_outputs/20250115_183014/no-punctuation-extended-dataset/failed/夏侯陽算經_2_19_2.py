"""
今有布二萬五千四百二十八端二丈七尺欲折布為輕貨絹其絹匹價三貫八百七十文其布端價二貫六百文問為絹幾何
術曰置布數倍丈尺以價二貫六百文乗之得六萬六千一百一十四貫二百四文以絹價三貫八百七十文除之得絹匹不盡二千九百九十四文進位四因之得一十一萬九千七百六十以下法除之得三丈九寸不盡者與法俱三約之得一百二十九分寸之五十九
答曰絹 a匹 b丈
"""

"""
Suppose there are 25,428 bolts of cloth, each measuring 2 zhang and 7 chi. 
It is desired to convert the cloth into light goods, silk. 
The price of one bolt of cloth is 2 guan and 600 wen, and the price of one bolt of silk is 3 guan and 870 wen.
Question: how many bolts of silk and how much leftover length of silk does it make?

The procedure says: Place the number of bolts of cloth and multiply by their length in zhang and chi. 
Multiply this by the price of one bolt of cloth (2 guan and 600 wen), obtaining the total value in wen. 
Divide this by the price of one bolt of silk (3 guan and 870 wen), obtaining the number of bolts of silk. 
The remainder in wen is converted into zhang and chi by dividing by the price per zhang and chi of silk. 
Simplify the fraction of the remainder.

Answer: It makes *a* bolts of silk and *b* zhang of leftover silk.
"""

from fractions import Fraction

# 布數
布端數 = 25428

# 每端布長度
布長度 = 2 * 10 + 7  # 2丈7尺 converted to 尺 (1丈 = 10尺)

# 布端價
布端價 = 2 * 1000 + 600  # 2貫600文 converted to 文 (1貫 = 1000文)

# 絹匹價
絹匹價 = 3 * 1000 + 870  # 3貫870文 converted to 文 (1貫 = 1000文)

# 計算布的總價值
布總價值 = 布端數 * 布長度 * 布端價

# 用絹匹價除以布總價值，得絹匹數和剩餘文數
絹匹數 = 布總價值 // 絹匹價
剩餘文數 = 布總價值 % 絹匹價

# 計算剩餘文數對應的絹的長度
# 每匹絹的長度為10丈 (假設標準匹長度)
絹每丈價 = 絹匹價 / 10  # 每丈絹的價值
剩餘長度 = Fraction(剩餘文數, 絹每丈價)  # 剩餘長度以丈為單位

# 分離剩餘長度為整數丈和分數部分
整數丈 = int(剩餘長度)  # 整數部分
分數部分 = 剩餘長度 - 整數丈  # 分數部分

# 答案
a = 絹匹數
b = Fraction(整數丈) + 分數部分
"""
Code error: both arguments should be Rational instances"""
