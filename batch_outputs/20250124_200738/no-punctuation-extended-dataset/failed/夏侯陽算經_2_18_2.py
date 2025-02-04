"""
今有布三百九十六端二丈五尺端别一百八十文充腳其布準時估端三百六十文竝扵數内抽給問正腳各幾何
術曰置布數倍丈尺以一百八十文乗之得七萬一千三百七十文為實列腳錢一百八十文并入價錢三百六十文得五百四十文為法實如法得腳端不盡九十文進位因之得四千五百以下法除得八尺三寸不盡者與法俱一十八約之得三分寸之一為命分以減都數餘即正
答曰正 a端 腳 b端
"""

#----- content starts here -----
"""
Suppose there are 396 bolts of cloth, each 2 zhang and 5 chi long. Each bolt is priced at 360 wen, and each extra portion (footing) is priced at 180 wen.
The total cloth is to be distributed, including footing, and the question is: how many bolts are fully paid for, and how much footing remains?

The procedure says:
1. Place the number of bolts and multiply by their length in zhang and chi. Multiply this by 180 wen, obtaining 71370 wen as the dividend.
2. Add the footing price (180 wen) to the bolt price (360 wen), obtaining 540 wen as the divisor.
3. Divide the dividend by the divisor, obtaining the number of bolts. The remainder is 90 wen.
4. Advance the remainder to the next unit, obtaining 4500 chi. Divide this by the divisor, obtaining 8 chi and 3 cun. The remainder is 18.
5. Simplify the remainder with the divisor, obtaining 1/3 cun as the fractional part.
6. Subtract the fractional part from the total, leaving the correct number.

Answer: *a* bolts are fully paid for, and *b* bolts are footing.
"""

from fractions import Fraction

# 布三百九十六端
布端數 = 396

# 每端二丈五尺
每端長度 = 2 * 10 + 5  # Convert to chi (1 zhang = 10 chi)

# 每端腳錢一百八十文
腳錢 = 180

# 每端價錢三百六十文
端價錢 = 360

# 置布數倍丈尺，以一百八十文乘之，得實
實 = 布端數 * 每端長度 * 腳錢

# 列腳錢一百八十文，并入價錢三百六十文，得法
法 = 腳錢 + 端價錢

# 實如法得腳端
腳端 = 實 // 法

# 不盡九十文進位因之
餘文 = 實 % 法
進位 = 餘文 * 10  # Convert to chi (1 zhang = 10 chi)

# 以下法除得八尺三寸
剩餘長度 = Fraction(進位, 法)

# 分解為整數部分和分數部分
整數部分 = int(剩餘長度)
分數部分 = 剩餘長度 - 整數部分

# 分數部分約分
命分 = 分數部分.limit_denominator()

# 正腳端數
a = 腳端

# 剩餘部分為腳端
b = Fraction(整數部分) + 命分#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 79201/300, Actual: 3300
Variable 'b' has wrong value. Expected: 79201/600, Actual: 0"""
