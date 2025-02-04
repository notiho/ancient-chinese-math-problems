"""
今有布三百九十六端二丈五尺端别一百八十文充腳其布準時估端三百六十文竝扵數内抽給問正腳各幾何
術曰置布數倍丈尺以一百八十文乗之得七萬一千三百七十文為實列腳錢一百八十文并入價錢三百六十文得五百四十文為法實如法得腳端不盡九十文進位因之得四千五百以下法除得八尺三寸不盡者與法俱一十八約之得三分寸之一為命分以減都數餘即正
答曰正 a端 腳 b端
"""

#----- content starts here -----
"""
Suppose there are 396 bolts of cloth, each 2 zhang and 5 chi in length. Each bolt is worth 360 wen, and each additional piece (foot) is worth 180 wen.
The cloth is distributed, and the additional pieces are deducted from the total. 
Question: how many full bolts (zheng) and additional pieces (jiao) are there?

The procedure says:
1. Place the number of bolts and multiply by their length in zhang and chi.
2. Multiply this by 180 wen, obtaining 71,370 wen as the dividend.
3. Add the additional piece price (180 wen) to the bolt price (360 wen), obtaining 540 wen as the divisor.
4. Divide the dividend by the divisor, obtaining the number of additional pieces (jiao) and a remainder of 90 wen.
5. Round up the remainder to the nearest bolt, obtaining 4,500 bolts.
6. Use the divisor to divide the remainder, obtaining 8 chi and 3 cun.
7. Simplify the remainder with the divisor, obtaining 1/3 chi as the fractional part.
8. Subtract the fractional part from the total, leaving the full bolts (zheng).

Answer: *a* full bolts (zheng), *b* additional pieces (jiao).
"""

from fractions import Fraction

# 布三百九十六端
布數 = 396

# 每端二丈五尺
每端長度 = 2 * 10 + 5  # 1丈 = 10尺

# 每端價錢三百六十文
端價錢 = 360

# 每腳價錢一百八十文
腳價錢 = 180

# 置布數倍丈尺，以一百八十文乘之，得七萬一千三百七十文為實
實 = 布數 * 每端長度 * 腳價錢

# 列腳錢一百八十文，并入價錢三百六十文，得五百四十文為法
法 = 端價錢 + 腳價錢

# 實如法，得腳端，不盡九十文
腳端 = 實 // 法
不盡 = 實 % 法

# 進位因之，得四千五百
進位 = 布數

# 以下法除，得八尺三寸
剩餘 = Fraction(不盡, 法)
剩餘尺 = 剩餘 * 每端長度

# 不盡者與法俱一十八約之，得三分寸之一為命分
命分 = Fraction(剩餘尺).limit_denominator(18)

# 以減都數，餘即正
正端 = 布數 - int(命分)
腳端 = int(腳端)

a = 正端
b = 腳端#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 79201/300, Actual: 396
Variable 'b' has wrong value. Expected: 79201/600, Actual: 3300"""
