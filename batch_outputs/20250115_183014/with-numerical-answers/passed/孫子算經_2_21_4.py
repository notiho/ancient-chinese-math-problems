"""
今有築城，上廣二丈，下廣五丈四尺，高三丈八尺，長五千五百五十尺，秋程人功三百尺。問：須功幾何？
術曰：置里數以三百步乘之，內零步，六之，得五萬二千八百二十四尺，并上下廣，得二丈六寸，半之，以深乘之，得一百八十五尺四寸，以長乘得九百七十九萬三千五百六十九尺六寸，以人功三百尺除之，即得。
答曰： a(=26011)功 。
"""

"""
Suppose there is a city wall being constructed. The top width is 2 zhang, the bottom width is 5 zhang and 4 chi, the height is 3 zhang and 8 chi, and the length is 5550 chi. 
The autumn labor rate is 300 chi per person. 
Question: how many labor units are required?

The procedure says: Place the li count and multiply it by 300 bu, converting it into chi. 
Add the top and bottom widths, obtaining 2 zhang and 6 chi, and halve it. 
Multiply it by the depth (height), obtaining 185 chi and 4 cun. 
Multiply it by the length, obtaining 9,793,569 chi and 6 cun. 
Divide it by the labor rate of 300 chi per person, and the result is the number of labor units.

Answer: *a*(=26011) labor units.
"""

# 上廣二丈
上廣 = 2 * 10  # Convert zhang to chi (1 zhang = 10 chi)

# 下廣五丈四尺
下廣 = 5 * 10 + 4  # Convert zhang and chi to chi

# 高三丈八尺
高 = 3 * 10 + 8  # Convert zhang and chi to chi

# 長五千五百五十尺
長 = 5550  # Already in chi

# 秋程人功三百尺
人功 = 300  # Labor rate in chi

# 并上下廣，得二丈六寸
上下廣和 = 上廣 + 下廣  # Add top and bottom widths

# 半之
平均廣 = Fraction(上下廣和, 2)  # Halve the sum of widths

# 以深乘之，得一百八十五尺四寸
橫截面積 = 平均廣 * 高  # Multiply by height to get cross-sectional area

# 以長乘得九百七十九萬三千五百六十九尺六寸
總體積 = 橫截面積 * 長  # Multiply by length to get total volume

# 以人功三百尺除之，即得
a = Fraction(總體積, 人功)  # Divide by labor rate to get labor units

a = int(a)  # Convert to integer since labor units must be whole
# a = 26011
"""
"""
