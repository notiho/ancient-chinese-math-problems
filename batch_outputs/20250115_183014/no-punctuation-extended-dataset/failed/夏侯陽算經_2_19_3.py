"""
今有布二萬五千四百二十八端二丈七尺欲折布為輕貨絹其絹匹價三貫八百七十文其布端價二貫六百文問為絹幾何
術曰置布數倍丈尺以價二貫六百文乗之得六萬六千一百一十四貫二百四文以絹價三貫八百七十文除之得絹匹不盡二千九百九十四文進位四因之得一十一萬九千七百六十以下法除之得三丈九寸不盡者與法俱三約之得一百二十九分寸之五十九
答曰絹 a匹 b丈
"""

"""
Suppose there are 25,428 bolts of cloth, each 2 zhang and 7 chi long. 
It is desired to convert the cloth into light goods, silk. 
The price of each bolt of silk is 3 guan and 870 wen, and the price of each bolt of cloth is 2 guan and 600 wen.
Question: how many bolts of silk and how much leftover length does it make?

The procedure says: Place the number of bolts of cloth, multiply by the length in zhang and chi, and then multiply by the price of 2 guan and 600 wen. 
This gives 66,114 guan and 204 wen. 
Divide this by the price of silk, 3 guan and 870 wen, to obtain the number of bolts of silk. 
The remainder is 2,994 wen. 
Convert this into zhang and chi by multiplying by 4, obtaining 119,760. 
Divide this by the price of silk to get 3 zhang and 9 cun. 
The remainder, together with the divisor, is reduced by their greatest common divisor, giving 129 cun and 59 parts.

Answer: *a* bolts of silk and *b* zhang.
"""

from fractions import Fraction

# 布數
布端數 = 25428

# 每端長度：2丈7尺
每端長度 = 2 + Fraction(7, 10)  # 1丈 = 10尺

# 布端價：2貫600文
布端價 = 2 * 1000 + 600  # 1貫 = 1000文

# 絹匹價：3貫870文
絹匹價 = 3 * 1000 + 870  # 1貫 = 1000文

# 置布數倍丈尺，以價二貫六百文乘之
總布價 = 布端數 * 每端長度 * 布端價

# 以絹價三貫八百七十文除之，得絹匹
絹匹 = 總布價 // 絹匹價

# 不盡者
剩餘文 = 總布價 % 絹匹價

# 進位四因之
剩餘文進位 = 剩餘文 * 4

# 以下法除之
剩餘長度 = 剩餘文進位 // 絹匹價

# 不盡者與法俱三約之
剩餘部分 = Fraction(剩餘文進位 % 絹匹價, 絹匹價)

# 答案
a = 絹匹
b = Fraction(剩餘長度) + 剩餘部分

# 絹匹數與剩餘長度
a匹 = a
b丈 = b

a匹, b丈
"""
Variable 'a' has wrong value. Expected: 17083, Actual: 46125
Variable 'b' has wrong value. Expected: 1996/645, Actual: 36/43"""
