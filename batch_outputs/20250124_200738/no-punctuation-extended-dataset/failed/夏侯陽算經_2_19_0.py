"""
今有布二萬五千四百二十八端二丈七尺欲折布為輕貨絹其絹匹價三貫八百七十文其布端價二貫六百文問為絹幾何
術曰置布數倍丈尺以價二貫六百文乗之得六萬六千一百一十四貫二百四文以絹價三貫八百七十文除之得絹匹不盡二千九百九十四文進位四因之得一十一萬九千七百六十以下法除之得三丈九寸不盡者與法俱三約之得一百二十九分寸之五十九
答曰絹 a匹
"""

#----- content starts here -----
"""
Suppose there are 25,428 bolts of cloth, each 2 zhang and 7 chi long. 
It is desired to convert the cloth into light silk. 
The price of each bolt of cloth is 2 guan and 600 wen, and the price of each bolt of silk is 3 guan and 870 wen.
Question: how many bolts of silk does it make?

The procedure says: Place the number of bolts of cloth and multiply it by the length in zhang and chi. 
Then multiply it by the price of 2 guan and 600 wen, obtaining the total value in wen. 
Divide this by the price of silk, 3 guan and 870 wen, obtaining the number of bolts of silk. 
If there is a remainder, convert it into zhang and chi, then divide it by the price ratio to find the fractional part.

Answer: it makes *a* bolts of silk.
"""

from fractions import Fraction

# 布數
布端數 = 25428

# 每端布的長度 (2丈7尺)
布長度 = 2 * 10 + 7  # 1丈 = 10尺

# 每端布的價值 (2貫600文)
布價值 = 2 * 1000 + 600  # 1貫 = 1000文

# 每匹絹的價值 (3貫870文)
絹價值 = 3 * 1000 + 870  # 1貫 = 1000文

# 計算布的總價值
布總價值 = 布端數 * 布長度 * 布價值

# 用絹的價值除以布的總價值，得到絹匹數和餘數
絹匹數 = 布總價值 // 絹價值
餘數 = 布總價值 % 絹價值

# 餘數轉換為分數
餘數分數 = Fraction(餘數, 絹價值)

# 最終答案
a = 絹匹數 + 餘數分數#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 11019034/645, Actual: 19833840/43"""
