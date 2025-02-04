"""
今有布二萬五千四百二十八端二丈七尺欲折布為輕貨絹其絹匹價三貫八百七十文其布端價二貫六百文問為絹幾何
術曰置布數倍丈尺以價二貫六百文乗之得六萬六千一百一十四貫二百四文以絹價三貫八百七十文除之得絹匹不盡二千九百九十四文進位四因之得一十一萬九千七百六十以下法除之得三丈九寸不盡者與法俱三約之得一百二十九分寸之五十九
答曰絹 a匹
"""

#----- content starts here -----
"""
Suppose there are 25,428 bolts of cloth, each 2 zhang and 7 chi in length. 
It is desired to convert the cloth into light goods, specifically silk. 
The price of each bolt of silk is 3 guan and 870 wen, and the price of each bolt of cloth is 2 guan and 600 wen. 
Question: how many bolts of silk can be obtained?

The procedure says: Place the number of bolts of cloth, multiply by their length in zhang and chi, and then multiply by the price of 2 guan and 600 wen. 
This gives the total value in wen. 
Divide this by the price of silk, 3 guan and 870 wen, to obtain the number of bolts of silk. 
The remainder is 2,994 wen. 
Round up to the nearest bolt. 
For the remaining length, multiply by the divisor (silk price) and divide by the cloth price to obtain the leftover length in zhang and chi. 
Simplify the fraction to get the final result.

Answer: *a* bolts of silk.
"""

from fractions import Fraction

# 布數
布數 = 25428

# 每端布長度：2丈7尺
布長度 = 2 * 10 + 7  # Convert to chi (1丈 = 10尺)

# 布端價：2貫600文
布價 = 2 * 1000 + 600  # Convert to wen (1貫 = 1000文)

# 絹匹價：3貫870文
絹價 = 3 * 1000 + 870  # Convert to wen (1貫 = 1000文)

# 計算布的總價值
總價值 = 布數 * 布長度 * 布價  # 總價值 in wen

# 用絹價除以總價值，計算絹匹數
絹匹 = 總價值 // 絹價  # 整數部分
剩餘文 = 總價值 % 絹價  # 餘數部分

# 計算剩餘部分的布長度
剩餘布長度 = Fraction(剩餘文, 絹價) * 布長度

# 簡化剩餘布長度
剩餘布長度 = Fraction(剩餘布長度).limit_denominator()

# 答案
a = 絹匹  # 絹匹數
#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 11019034/645, Actual: 461252"""
