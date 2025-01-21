"""
今有布二萬五千四百二十八端二丈七尺欲折布為輕貨絹其絹匹價三貫八百七十文其布端價二貫六百文問為絹幾何
術曰置布數倍丈尺以價二貫六百文乗之得六萬六千一百一十四貫二百四文以絹價三貫八百七十文除之得絹匹不盡二千九百九十四文進位四因之得一十一萬九千七百六十以下法除之得三丈九寸不盡者與法俱三約之得一百二十九分寸之五十九
答曰絹 a匹 b丈
"""

"""
Suppose there are 25,428 bolts of cloth, each measuring 2 zhang and 7 chi.
It is desired to convert the cloth into light silk (juan).
The price of each bolt of cloth is 2 guan and 600 wen, and the price of each bolt of silk is 3 guan and 870 wen.
Question: how many bolts of silk and how much leftover length of silk are obtained?

The procedure says: Place the number of bolts of cloth, multiply by the length in zhang and chi, and multiply by the price of 2 guan and 600 wen.
This gives 66,114 guan and 200 wen.
Divide by the price of silk, 3 guan and 870 wen, to obtain the number of bolts of silk.
The remainder is 2,994 wen.
Round up and multiply by 4, obtaining 119,760.
Divide by the length of silk, obtaining 3 zhang and 9 cun.
The remainder, together with the divisor, is reduced by 3, obtaining 129 cun and 59 parts.

Answer: *a* bolts of silk and *b* zhang.
"""

from fractions import Fraction

# 布數
布端數 = 25428

# 每端布長
布長_丈 = 2
布長_尺 = 7
布長 = 布長_丈 + Fraction(布長_尺, 10)

# 布端價
布端價 = 2 * 1000 + 600  # 2貫6百文 = 2600文

# 絹匹價
絹匹價 = 3 * 1000 + 870  # 3貫8百7十文 = 3870文

# 置布數倍丈尺，以價二貫六百文乘之
總布價 = 布端數 * 布長 * 布端價

# 以絹價三貫八百七十文除之，得絹匹
絹匹 = 總布價 // 絹匹價

# 不盡者
剩餘文 = 總布價 % 絹匹價

# 進位四因之
進位 = 剩餘文 * 4

# 以下法除之，得丈
丈 = 進位 // 絹匹價

# 不盡者與法俱三約之，得分寸
剩餘丈 = Fraction(進位 % 絹匹價, 絹匹價)
分寸 = 剩餘丈 * 10 * 3  # 轉換為分寸

a = 絹匹
b = 丈 + 分寸


"""
Variable 'a' has wrong value. Expected: 17083, Actual: 46125
Variable 'b' has wrong value. Expected: 1996/645, Actual: 1080/43"""
