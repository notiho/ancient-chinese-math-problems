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
The work rate is 300 chi per person.

Question: How many workers are needed?

The procedure says:
1. Place the length in li (1 li = 300 bu = 1800 chi). Multiply it by 300 bu, then divide the remainder by 6, obtaining 52824 chi.
2. Add the top and bottom widths, obtaining 2 zhang 6 chi 5 cun. Divide by 2 to get the average width.
3. Multiply the average width by the height, obtaining 185 chi 4 cun.
4. Multiply by the length, obtaining 9793569 chi 6 cun.
5. Divide by the work rate of 300 chi per person to get the number of workers.

Answer: *a* workers.
"""

# Dimensions of the city wall
上廣 = 2  # Top width in zhang
下廣 = 5 + Fraction(4, 10)  # Bottom width in zhang (5 zhang 4 chi)
高 = 3 + Fraction(8, 10)  # Height in zhang (3 zhang 8 chi)
長 = 5550  # Length in chi

# Work rate
人功 = 300  # Work rate in chi per person

# Step 1: Add the top and bottom widths, then divide by 2 to get the average width
平均廣 = (上廣 + 下廣) / 2

# Step 2: Multiply the average width by the height to get the cross-sectional area
截面積 = 平均廣 * 高

# Step 3: Multiply the cross-sectional area by the length to get the total volume
總積 = 截面積 * 長

# Step 4: Divide the total volume by the work rate to get the number of workers
a = Fraction(總積, 人功)  # Number of workers
"""
Variable 'a' has wrong value. Expected: 26011, Actual: 26011/100"""
