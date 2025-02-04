"""
今有築城上廣二丈下廣五丈四尺高三丈八尺長五千五百五十尺秋程人功三百尺問須功幾何
術曰置里數以三百步乘之內零步六之得五萬二千八百二十四尺并上下廣得二丈六寸半之以深乘之得一百八十五尺四寸以長乘得九百七十九萬三千五百六十九尺六寸以人功三百尺除之即得
答曰 a功 
"""

"""
Suppose there is a city wall with the following dimensions:
- Top width: 2 zhang
- Bottom width: 5 zhang 4 chi
- Height: 3 zhang 8 chi
- Length: 5550 chi
The autumn labor rate is 300 chi per person.
Question: how many person-labor units are required?

The procedure says:
1. Place the length in li (1 li = 300 bu = 150 zhang = 1500 chi). Multiply it by 300 bu.
2. Convert the remaining chi into sixths (1 chi = 6 cun), obtaining 52824 chi.
3. Add the top and bottom widths, obtaining 2 zhang 6 chi 5 cun.
4. Multiply this by the depth (height), obtaining 185 chi 4 cun.
5. Multiply this by the length, obtaining 9793569 chi 6 cun.
6. Divide by the labor rate of 300 chi per person, obtaining the number of person-labor units.

Answer: *a* person-labor units.
"""

# 上廣二丈
上廣 = 2 * 10  # Convert zhang to chi

# 下廣五丈四尺
下廣 = 5 * 10 + 4  # Convert zhang to chi and add chi

# 高三丈八尺
高 = 3 * 10 + 8  # Convert zhang to chi and add chi

# 長五千五百五十尺
長 = 5550  # Already in chi

# 秋程人功三百尺
人功 = 300  # Labor rate in chi per person

# 置里數以三百步乘之 (Convert length to chi; already in chi, so no conversion needed)
# 內零步六之得五萬二千八百二十四尺 (No additional conversion required; length remains in chi)

# 并上下廣得二丈六寸半
上下廣 = 上廣 + 下廣  # Add top and bottom widths

# 之以深乘之得一百八十五尺四寸
積 = 上下廣 * 高  # Multiply by depth (height)

# 以長乘得九百七十九萬三千五百六十九尺六寸
體積 = 積 * 長  # Multiply by length

# 以人功三百尺除之即得
a = Fraction(體積, 人功)  # Divide by labor rate to get person-labor units
"""
Variable 'a' has wrong value. Expected: 26011, Actual: 52022"""
