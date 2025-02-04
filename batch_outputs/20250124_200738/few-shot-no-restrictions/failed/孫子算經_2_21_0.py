"""
今有築城，上廣二丈，下廣五丈四尺，高三丈八尺，長五千五百五十尺，秋程人功三百尺。問：須功幾何？
術曰：置里數以三百步乘之，內零步，六之，得五萬二千八百二十四尺，并上下廣，得二丈六寸，半之，以深乘之，得一百八十五尺四寸，以長乘得九百七十九萬三千五百六十九尺六寸，以人功三百尺除之，即得。
答曰： a功 。
"""

#----- content starts here -----
"""
Suppose there is a city wall to be constructed. The top width is 2 zhang, the bottom width is 5 zhang 4 chi, the height is 3 zhang 8 chi, and the length is 5550 chi. 
One person can complete 300 chi of work in a day. 
Question: how many person-days of labor are required?

The procedure says: 
1. Place the length in li (1 li = 300 bu) and multiply it by 300 bu. 
2. Add the remaining chi, multiply by 6, obtaining the total chi. 
3. Add the top and bottom widths, obtaining 2 zhang 6 chi. 
4. Halve it, then multiply by the height, obtaining the cross-sectional area. 
5. Multiply the cross-sectional area by the length, obtaining the total volume. 
6. Divide the total volume by the per-person work rate (300 chi), obtaining the number of person-days.

Answer: *a* person-days.
"""

from fractions import Fraction

# 城牆參數
上廣 = 2  # zhang
下廣 = 5 + Fraction(4, 10)  # 5丈4尺 = 5.4丈
高 = 3 + Fraction(8, 10)  # 3丈8尺 = 3.8丈
長 = 5550  # chi
人功 = 300  # 每人每天完成300尺

# 計算上下廣的平均值
上下廣 = 上廣 + 下廣  # 上廣 + 下廣
平均廣 = 上下廣 / 2  # 平均廣度

# 計算橫截面積
橫截面積 = 平均廣 * 高  # 橫截面積 = 平均廣 * 高

# 計算總體積
總體積 = 橫截面積 * 長  # 總體積 = 橫截面積 * 長

# 計算所需功數
所需功數 = 總體積 / 人功  # 所需功數 = 總體積 / 每人每天完成的尺數

# 答案
a = 所需功數
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 26011, Actual: 26011/100"""
