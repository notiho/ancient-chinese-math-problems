"""
今有布三百九十六端二丈五尺端别一百八十文充腳其布準時估端三百六十文竝扵數内抽給問正腳各幾何
術曰置布數倍丈尺以一百八十文乗之得七萬一千三百七十文為實列腳錢一百八十文并入價錢三百六十文得五百四十文為法實如法得腳端不盡九十文進位因之得四千五百以下法除得八尺三寸不盡者與法俱一十八約之得三分寸之一為命分以減都數餘即正
答曰正 a端 腳 b端
"""

"""
Suppose there are 396 bolts of cloth, each bolt measuring 2 zhang and 5 chi. Each bolt is priced at 360 wen, and an additional 180 wen is charged as a surcharge for each bolt. 
The total cost is to be distributed among the bolts, with the surcharge included. 
Question: how many bolts are fully paid (正腳), and how much of the remaining bolt is partially paid (腳)?

The procedure says:
1. Multiply the total number of bolts by their length in zhang and chi, and then multiply by 180 wen to get the total surcharge (實).
2. Add the surcharge (180 wen) to the price of a bolt (360 wen) to get the divisor (法).
3. Divide the total surcharge (實) by the divisor (法) to get the number of fully paid bolts (正腳). If there is a remainder, convert it into zhang and chi.
4. For the remainder, divide it by the divisor (法) to get the fraction of the bolt that is partially paid (腳).
5. Simplify the fraction to its lowest terms.

Answer: *a* bolts are fully paid (正腳), and *b* bolts are partially paid (腳).
"""

from fractions import Fraction

# 布三百九十六端
布數 = 396

# 每端二丈五尺
丈 = 2
尺 = 5

# 每端脚錢一百八十文
腳錢 = 180

# 每端價錢三百六十文
價錢 = 360

# 置布數倍丈尺，以一百八十文乘之，得實
實 = 布數 * (丈 * 10 + 尺) * 腳錢

# 列腳錢一百八十文，并入價錢三百六十文，得法
法 = 腳錢 + 價錢

# 實如法，得正腳端
正腳端 = 實 // 法

# 不盡九十文進位因之
餘文 = 實 % 法

# 餘文以下法除，得部分腳
部分腳 = Fraction(餘文, 法)

# 簡化分數
部分腳 = 部分腳.limit_denominator()

a = 正腳端
b = 部分腳
"""
Variable 'a' has wrong value. Expected: 79201/300, Actual: 3300
Variable 'b' has wrong value. Expected: 79201/600, Actual: 0"""
