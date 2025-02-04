"""
今有築城，上廣二丈，下廣五丈四尺，高三丈八尺，長五千五百五十尺，秋程人功三百尺。問：須功幾何？
術曰：置里數以三百步乘之，內零步，六之，得五萬二千八百二十四尺，并上下廣，得二丈六寸，半之，以深乘之，得一百八十五尺四寸，以長乘得九百七十九萬三千五百六十九尺六寸，以人功三百尺除之，即得。
答曰： a功 。
"""

#----- content starts here -----
"""
Suppose there is a city wall to be built. The top width is 2 zhang, the bottom width is 5 zhang and 4 chi, the height is 3 zhang and 8 chi, and the length is 5550 chi. 
One person can complete 300 chi of work in one day. 
Question: how many person-days of labor are required?

The procedure says: Place the length in li (1 li = 300 bu) and multiply it by 300 bu. 
Convert any remaining bu into chi and multiply by 6, obtaining the total length in chi. 
Add the top and bottom widths, obtaining 2 zhang and 6 chi. 
Halve this value and multiply it by the depth (height), obtaining 185 chi and 4 cun. 
Multiply this by the total length, obtaining 9,793,569 chi and 6 cun. 
Divide this by the labor rate of 300 chi per person-day, and the result is the required number of person-days.

Answer: *a* person-days.
"""

# 上廣二丈
上廣 = 2 * 10  # Convert zhang to chi

# 下廣五丈四尺
下廣 = 5 * 10 + 4  # Convert zhang to chi and add chi

# 高三丈八尺
高 = 3 * 10 + 8  # Convert zhang to chi and add chi

# 長五千五百五十尺
長 = 5550

# 秋程人功三百尺
人功 = 300

# 并上下廣，得二丈六寸
上下廣 = 上廣 + 下廣  # Add top and bottom widths

# 半之
平均廣 = Fraction(上下廣, 2)  # Halve the sum of widths

# 以深乘之，得一百八十五尺四寸
橫截面積 = 平均廣 * 高  # Multiply by height

# 以長乘
總體積 = 橫截面積 * 長  # Multiply by length

# 以人功三百尺除之，即得
a = Fraction(總體積, 人功)  # Divide by labor rate to get person-days#----- content ends here -----

"""
"""
