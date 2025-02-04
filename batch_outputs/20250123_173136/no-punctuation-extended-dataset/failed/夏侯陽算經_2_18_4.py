"""
今有布三百九十六端二丈五尺端别一百八十文充腳其布準時估端三百六十文竝扵數内抽給問正腳各幾何
術曰置布數倍丈尺以一百八十文乗之得七萬一千三百七十文為實列腳錢一百八十文并入價錢三百六十文得五百四十文為法實如法得腳端不盡九十文進位因之得四千五百以下法除得八尺三寸不盡者與法俱一十八約之得三分寸之一為命分以減都數餘即正
答曰正 a端 腳 b端
"""

"""
Suppose there are 396 bolts of cloth, each bolt being 2 zhang and 5 chi in length. 
Each bolt has an additional cost of 180 wen for tailoring.
The cloth is valued at 360 wen per bolt.
From the total amount, the tailoring cost is to be deducted.
Question: how many bolts are fully paid for, and how much remains for tailoring?

The procedure says:
1. Multiply the total number of bolts by their length in zhang and chi, and then by 180 wen, obtaining 71370 wen as the dividend.
2. Add the tailoring cost (180 wen) to the cloth price (360 wen), obtaining 540 wen as the divisor.
3. Divide the dividend by the divisor, obtaining the number of fully paid bolts. The remainder is 90 wen.
4. Convert the remainder into zhang and chi. Divide the remainder by the divisor (540 wen), obtaining 8 chi and 3 cun.
5. Simplify the fraction of cun (18 parts), obtaining 1/3 cun.
6. Subtract this from the total, leaving the remainder.

Answer: *a* bolts are fully paid for, and *b* bolts remain for tailoring.
"""

from fractions import Fraction

# 布三百九十六端
布數 = 396

# 每端二丈五尺
每端長度_丈 = 2
每端長度_尺 = 5

# 每端別一百八十文
腳錢 = 180

# 每端布價三百六十文
布價 = 360

# 置布數倍丈尺，以一百八十文乘之，得七萬一千三百七十文為實
實 = 布數 * (每端長度_丈 * 10 + 每端長度_尺) * 腳錢

# 列腳錢一百八十文，并入價錢三百六十文，得五百四十文為法
法 = 布價 + 腳錢

# 實如法得腳端，不盡九十文
腳端 = 實 // 法
餘文 = 實 % 法

# 餘文進位因之，得八尺三寸
餘尺 = (餘文 * 10) // 法
餘寸 = Fraction((餘文 * 10) % 法, 法) * 10

# 以下法除，得三分寸之一為命分
命分 = Fraction(餘寸).limit_denominator(18)

# 答案
a = 腳端
b = Fraction(餘尺, 10) + 命分
"""
Variable 'a' has wrong value. Expected: 79201/300, Actual: 3300
Variable 'b' has wrong value. Expected: 79201/600, Actual: 0"""
