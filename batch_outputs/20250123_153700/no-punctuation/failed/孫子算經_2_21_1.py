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
The autumn labor capacity of one person is 300 chi.

Question: How many units of labor are required?

The procedure says:
1. Place the length in li (1 li = 300 bu = 150 zhang = 1500 chi). Multiply it by 300 bu.
2. Convert any remaining bu to chi by dividing by 6. This gives the total length in chi.
3. Add the top and bottom widths, obtaining 2 zhang 6 chi 5 cun.
4. Multiply this by the depth (height), obtaining the cross-sectional area.
5. Multiply the cross-sectional area by the length, obtaining the total volume.
6. Divide the total volume by the labor capacity of one person (300 chi), obtaining the required labor.

Answer: *a* units of labor.
"""

# 上廣二丈
上廣 = 2 * 10  # Convert zhang to chi

# 下廣五丈四尺
下廣 = 5 * 10 + 4  # Convert zhang to chi and add chi

# 高三丈八尺
高 = 3 * 10 + 8  # Convert zhang to chi and add chi

# 長五千五百五十尺
長 = 5550  # Length in chi

# 秋程人功三百尺
人功 = 300  # Labor capacity in chi

# 并上下廣，得二丈六寸半
上下廣 = 上廣 + 下廣  # Add top and bottom widths

# Convert 2丈6寸半 to chi (1 cun = 1/10 chi, 1 zhang = 10 chi)
上下廣 += Fraction(5, 10)  # Add 5 cun (half chi)

# 以深乘之，得一百八十五尺四寸
截面積 = 上下廣 * 高  # Cross-sectional area in chi^2

# 以長乘，得總體積
總體積 = 截面積 * 長  # Total volume in chi^3

# 以人功三百尺除之，即得
a = Fraction(總體積, 人功)  # Required labor in units

a
"""
Variable 'a' has wrong value. Expected: 26011, Actual: 104747/2"""
