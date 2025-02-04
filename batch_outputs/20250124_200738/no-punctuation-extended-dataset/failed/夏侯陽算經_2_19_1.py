"""
今有布二萬五千四百二十八端二丈七尺欲折布為輕貨絹其絹匹價三貫八百七十文其布端價二貫六百文問為絹幾何
術曰置布數倍丈尺以價二貫六百文乗之得六萬六千一百一十四貫二百四文以絹價三貫八百七十文除之得絹匹不盡二千九百九十四文進位四因之得一十一萬九千七百六十以下法除之得三丈九寸不盡者與法俱三約之得一百二十九分寸之五十九
答曰絹 a匹
"""

#----- content starts here -----
"""
Suppose there are 25,428 bolts of cloth, each 2 zhang and 7 chi in length. 
It is desired to convert the cloth into light silk. 
The price of one bolt of silk is 3 guan and 870 wen, and the price of one bolt of cloth is 2 guan and 600 wen.
Question: how many bolts of silk does it make?

The procedure says: Place the number of bolts of cloth and multiply it by the length in zhang and chi. 
Multiply this by the price of 2 guan and 600 wen, obtaining the total value in wen.
Divide this by the price of 3 guan and 870 wen to get the number of bolts of silk. 
If there is a remainder, convert it into wen and divide again to obtain the remaining length in zhang and chi. 
Simplify the remainder by reducing it to the smallest fraction.

Answer: it makes *a* bolts of silk.
"""

from fractions import Fraction

# 布數
布數 = 25428

# 每端布的長度：2丈7尺
布長度 = 2 * 10 + 7  # 1丈 = 10尺

# 每端布的價值：2貫600文
布價值 = 2 * 1000 + 600  # 1貫 = 1000文

# 絹匹價值：3貫870文
絹價值 = 3 * 1000 + 870  # 1貫 = 1000文

# 計算布的總價值
總價值 = 布數 * 布長度 * 布價值

# 用絹價值除以總價值，計算絹匹數
絹匹 = 總價值 // 絹價值  # 整數部分
剩餘文 = 總價值 % 絹價值  # 餘數部分

# 將剩餘文轉換為布長度
剩餘布長度 = Fraction(剩餘文, 絹價值) * 布長度

# 簡化剩餘布長度
簡化布長度 = Fraction(剩餘布長度).limit_denominator()

a = 絹匹 + 簡化布長度
#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 11019034/645, Actual: 19833944/43"""
