"""
今有築城上廣二丈下廣五丈四尺高三丈八尺長五千五百五十尺秋程人功三百尺問須功幾何
術曰置里數以三百步乘之內零步六之得五萬二千八百二十四尺并上下廣得二丈六寸半之以深乘之得一百八十五尺四寸以長乘得九百七十九萬三千五百六十九尺六寸以人功三百尺除之即得
答曰 a功 
"""

#----- content starts here -----
"""
Suppose there is a city wall with the following dimensions:
- Top width: 2 zhang
- Bottom width: 5 zhang 4 chi
- Height: 3 zhang 8 chi
- Length: 5550 chi
The autumn labor rate is 300 chi per person.
Question: how many person-days of labor are required?

The procedure says:
1. Place the length in li (1 li = 300 bu = 150 zhang = 1500 chi).
2. Multiply it by 300 bu, converting it into chi.
3. Add the top and bottom widths, obtaining 2 zhang 6 chi 5 cun.
4. Divide this sum by 2, then multiply by the depth (height), obtaining the cross-sectional area.
5. Multiply the cross-sectional area by the length, obtaining the total volume in chi³.
6. Divide the total volume by the labor rate (300 chi³ per person), obtaining the number of person-days of labor.

Answer: *a* person-days of labor.
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
人功 = 300  # Labor rate in chi³ per person

# 并上下廣得二丈六寸半
上下廣和 = 上廣 + 下廣  # Sum of top and bottom widths

# 之以深乘之
平均廣 = Fraction(上下廣和, 2)  # Average width
截面積 = 平均廣 * 高  # Cross-sectional area

# 以長乘得
總體積 = 截面積 * 長  # Total volume in chi³

# 以人功三百尺除之即得
a = Fraction(總體積, 人功)  # Number of person-days of labor#----- content ends here -----

"""
"""
