"""
今有布三百九十六端二丈五尺端别一百八十文充腳其布準時估端三百六十文竝扵數内抽給問正腳各幾何
術曰置布數倍丈尺以一百八十文乗之得七萬一千三百七十文為實列腳錢一百八十文并入價錢三百六十文得五百四十文為法實如法得腳端不盡九十文進位因之得四千五百以下法除得八尺三寸不盡者與法俱一十八約之得三分寸之一為命分以減都數餘即正
答曰正 a端 腳 b端
"""

"""
Suppose there are 396 bolts of cloth, each measuring 2 zhang and 5 chi. Each bolt is worth 180 wen as a surcharge for the extra length.
The cloth is valued at the current market price of 360 wen per bolt, and the surcharge is included in the total.
Question: how many bolts are fully paid for, and how many bolts are surcharged?

The procedure says: Place the number of bolts and multiply by the length in zhang and chi. Multiply this by 180 wen, obtaining 71370 wen as the dividend.
List the surcharge of 180 wen and add it to the market price of 360 wen, obtaining 540 wen as the divisor.
Divide the dividend by the divisor, obtaining the number of surcharged bolts. The remainder is 90 wen.
Advance the remainder to the next unit, obtaining 4500 chi. Divide by the divisor, obtaining 8 chi and 3 cun. The remainder is combined with the divisor, forming 18. Simplify this to obtain 1/3 chi as the fractional part.
Subtract this from the total number of bolts to obtain the fully paid bolts.

Answer: *a* bolts are fully paid, and *b* bolts are surcharged.
"""

from fractions import Fraction

# 布三百九十六端
布數 = 396

# 二丈五尺
丈 = 2
尺 = 5

# 每端脚錢一百八十文
腳錢 = 180

# 每端價錢三百六十文
價錢 = 360

# 置布數倍丈尺，以一百八十文乘之，得七萬一千三百七十文為實
實 = 布數 * (丈 * 10 + 尺) * 腳錢

# 列腳錢一百八十文，并入價錢三百六十文，得五百四十文為法
法 = 腳錢 + 價錢

# 實如法得腳端，不盡九十文
腳端 = 實 // 法
餘文 = 實 % 法

# 進位因之，得四千五百
進位 = 餘文 * 50

# 以下法除，得八尺三寸
進位除法 = 進位 // 法
餘進位 = 進位 % 法

# 不盡者與法俱一十八，約之，得三分寸之一為命分
命分 = Fraction(餘進位, 法)

# 以減都數，餘即正
正端 = 布數 - (腳端 + 命分)

a = 正端
b = 腳端
"""
Variable 'a' has wrong value. Expected: 79201/300, Actual: -2904
Variable 'b' has wrong value. Expected: 79201/600, Actual: 3300"""
