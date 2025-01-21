"""
今有布二萬五千四百二十八端二丈七尺欲折布為輕貨絹其絹匹價三貫八百七十文其布端價二貫六百文問為絹幾何
術曰置布數倍丈尺以價二貫六百文乗之得六萬六千一百一十四貫二百四文以絹價三貫八百七十文除之得絹匹不盡二千九百九十四文進位四因之得一十一萬九千七百六十以下法除之得三丈九寸不盡者與法俱三約之得一百二十九分寸之五十九
答曰絹 a匹 b丈
"""

"""
Suppose there are 25,428 bolts of cloth, each measuring 2 zhang and 7 chi. 
It is desired to convert the cloth into light silk fabric. 
The price of one bolt of cloth is 2 guan and 600 wen, and the price of one bolt of silk fabric is 3 guan and 870 wen.
Question: how many bolts of silk fabric and how much leftover length in zhang and chi?

The procedure says: Place the number of bolts of cloth and multiply by their length in zhang and chi. 
Multiply this by the price of one bolt of cloth (2 guan and 600 wen), obtaining the total value in wen.
Divide this by the price of one bolt of silk fabric (3 guan and 870 wen), obtaining the number of bolts of silk fabric. 
The remainder is 2,994 wen. 
Round up and multiply by 4, obtaining 119,760. 
Divide this by the silk fabric price, obtaining 3 zhang and 9 chi. 
The remainder is reduced with the divisor, obtaining 129/59 chi.

Answer: *a* bolts of silk fabric and *b* zhang.
"""

from fractions import Fraction

# 布數
布端數 = 25428

# 每端布長二丈七尺
布長_丈 = 2
布長_尺 = 7
布長 = 布長_丈 + Fraction(布長_尺, 10)

# 布端價二貫六百文
布端價 = 2 * 1000 + 600  # Convert to wen

# 絹匹價三貫八百七十文
絹匹價 = 3 * 1000 + 870  # Convert to wen

# 置布數倍丈尺
總布長 = 布端數 * 布長

# 以價二貫六百文乘之
總布價值 = 總布長 * 布端價

# 以絹價三貫八百七十文除之
絹匹數 = 總布價值 // 絹匹價  # Integer division for full bolts of silk
剩餘文 = 總布價值 % 絹匹價  # Remainder in wen

# 剩餘文進位四因之
剩餘文進位 = 剩餘文 * 4

# 以下法除之
剩餘長度 = 剩餘文進位 // 絹匹價  # Integer division for zhang
剩餘文_進位餘 = 剩餘文進位 % 絹匹價  # Remainder in wen after zhang calculation

# 與法俱三約之
剩餘長度_分數 = Fraction(剩餘文_進位餘, 絹匹價)

# 答案
a = 絹匹數
b = 剩餘長度 + 剩餘長度_分數


"""
Variable 'a' has wrong value. Expected: 17083, Actual: 46125
Variable 'b' has wrong value. Expected: 1996/645, Actual: 36/43"""
