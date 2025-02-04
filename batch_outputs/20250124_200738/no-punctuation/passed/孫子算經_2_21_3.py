"""
今有築城上廣二丈下廣五丈四尺高三丈八尺長五千五百五十尺秋程人功三百尺問須功幾何
術曰置里數以三百步乘之內零步六之得五萬二千八百二十四尺并上下廣得二丈六寸半之以深乘之得一百八十五尺四寸以長乘得九百七十九萬三千五百六十九尺六寸以人功三百尺除之即得
答曰 a功 
"""

#----- content starts here -----
"""
Suppose there is a city wall to be built. The top width is 2 zhang, the bottom width is 5 zhang and 4 chi, the height is 3 zhang and 8 chi, and the length is 5550 chi. 
The autumn labor rate is 300 chi per person. 
Question: how many laborers are needed?

The procedure says: Place the length in li (1 li = 300 bu = 150 zhang = 1500 chi). Multiply it by 300 bu. 
For the remainder chi, divide by 6, obtaining 52824 chi. 
Add the top and bottom widths, obtaining 2 zhang 6 chi 5 cun. Divide it by 2, and multiply by the depth, obtaining 185 chi 4 cun. 
Multiply by the length, obtaining 9793569 chi 6 cun. Divide by the labor rate of 300 chi, obtaining the number of laborers.

Answer: *a* laborers.
"""

from fractions import Fraction

# 上廣二丈
上廣 = 2 * 10  # Convert zhang to chi

# 下廣五丈四尺
下廣 = 5 * 10 + 4  # Convert zhang to chi and add chi

# 高三丈八尺
高 = 3 * 10 + 8  # Convert zhang to chi and add chi

# 長五千五百五十尺
長 = 5550  # Length in chi

# 秋程人功三百尺
人功 = 300  # Labor rate in chi

# 置里數以三百步乘之
# 1 li = 300 bu = 1500 chi
里數 = 長 // 1500  # Convert length to li
零步 = 長 % 1500  # Remaining chi after converting to li

# 內零步六之得五萬二千八百二十四尺
零步轉換 = Fraction(零步, 6)

# 并上下廣得二丈六寸半
上下廣 = 上廣 + 下廣
上下廣平均 = Fraction(上下廣, 2)  # Average width

# 之以深乘之得一百八十五尺四寸
體積截面 = 上下廣平均 * 高

# 以長乘得九百七十九萬三千五百六十九尺六寸
總體積 = 體積截面 * 長

# 以人功三百尺除之即得
a = Fraction(總體積, 人功)  # Number of laborers#----- content ends here -----

"""
"""
