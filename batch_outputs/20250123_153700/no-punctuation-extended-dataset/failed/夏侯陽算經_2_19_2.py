"""
今有布二萬五千四百二十八端二丈七尺欲折布為輕貨絹其絹匹價三貫八百七十文其布端價二貫六百文問為絹幾何
術曰置布數倍丈尺以價二貫六百文乗之得六萬六千一百一十四貫二百四文以絹價三貫八百七十文除之得絹匹不盡二千九百九十四文進位四因之得一十一萬九千七百六十以下法除之得三丈九寸不盡者與法俱三約之得一百二十九分寸之五十九
答曰絹 a匹
"""

"""
Suppose there are 25,428 bolts of cloth, each 2 zhang and 7 chi in length. 
It is desired to convert the cloth into light silk. 
The price of each bolt of cloth is 2 guan and 600 wen, and the price of each bolt of silk is 3 guan and 870 wen.
Question: how many bolts of silk can be obtained?

The procedure says: Place the number of bolts of cloth and multiply it by the length in zhang and chi. 
Then multiply it by the price of 2 guan and 600 wen, obtaining the total value in wen.
Divide this by the price of silk, 3 guan and 870 wen, obtaining the number of bolts of silk. 
If there is a remainder, convert it into zhang and chi, and divide it by the length of a bolt of silk. 
Simplify the fraction to obtain the final result.

Answer: *a* bolts of silk.
"""

from fractions import Fraction

# 布數
布數 = 25428

# 每端布的長度 (2丈7尺)
布長度 = 2 * 10 + 7  # 1丈 = 10尺

# 每端布的價值 (2貫600文)
布價值 = 2 * 1000 + 600  # 1貫 = 1000文

# 每匹絹的價值 (3貫870文)
絹價值 = 3 * 1000 + 870  # 1貫 = 1000文

# 計算布的總價值
總價值 = 布數 * 布長度 * 布價值

# 以絹價值除之，得絹匹數和餘數
絹匹數 = 總價值 // 絹價值
餘數 = 總價值 % 絹價值

# 將餘數轉換為布長度
餘布長度 = Fraction(餘數, 絹價值) * 布長度

# 簡化餘布長度
簡化餘布長度 = Fraction(餘布長度).limit_denominator()

# 最終答案
a = 絹匹數 + 簡化餘布長度

"""
Variable 'a' has wrong value. Expected: 11019034/645, Actual: 19833944/43"""
