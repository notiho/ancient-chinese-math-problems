"""
今有築城，上廣二丈，下廣五丈四尺，高三丈八尺，長五千五百五十尺，秋程人功三百尺。問：須功幾何？
術曰：置里數以三百步乘之，內零步，六之，得五萬二千八百二十四尺，并上下廣，得二丈六寸，半之，以深乘之，得一百八十五尺四寸，以長乘得九百七十九萬三千五百六十九尺六寸，以人功三百尺除之，即得。
答曰： a功 。
"""

"""
Suppose there is a city wall to be built. The top width is 2 zhang, the bottom width is 5 zhang 4 chi, the height is 3 zhang 8 chi, and the length is 5550 chi. 
The autumn labor rate is 300 chi per person. 
Question: how many units of labor are required?

The procedure says: Place the length in li, multiply it by 300 bu, and convert it to chi. 
Add the top and bottom widths, obtaining 2 zhang 6 chi. Halve it, then multiply by the depth (height), obtaining 185 chi 4 cun. 
Multiply this by the length, obtaining the total volume. 
Divide by the labor rate of 300 chi, obtaining the number of labor units.

Answer: *a* units of labor.
"""

from fractions import Fraction

# 上廣二丈
上廣 = 2 * 10  # Convert zhang to chi

# 下廣五丈四尺
下廣 = 5 * 10 + 4  # Convert zhang to chi and add chi

# 高三丈八尺
高 = 3 * 10 + 8  # Convert zhang to chi and add chi

# 長五千五百五十尺
長 = 5550  # Already in chi

# 秋程人功三百尺
人功 = 300  # Labor rate in chi

# 并上下廣，得二丈六寸
上下廣 = 上廣 + 下廣  # Add top and bottom widths

# 半之
平均廣 = Fraction(上下廣, 2)  # Halve the sum of widths

# 以深乘之，得一百八十五尺四寸
截面積 = 平均廣 * 高  # Multiply by height to get cross-sectional area

# 以長乘得九百七十九萬三千五百六十九尺六寸
體積 = 截面積 * 長  # Multiply by length to get total volume

# 以人功三百尺除之，即得
a = Fraction(體積, 人功)  # Divide by labor rate to get labor units
"""
"""
