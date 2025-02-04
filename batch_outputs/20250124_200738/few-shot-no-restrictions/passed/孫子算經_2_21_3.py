"""
今有築城，上廣二丈，下廣五丈四尺，高三丈八尺，長五千五百五十尺，秋程人功三百尺。問：須功幾何？
術曰：置里數以三百步乘之，內零步，六之，得五萬二千八百二十四尺，并上下廣，得二丈六寸，半之，以深乘之，得一百八十五尺四寸，以長乘得九百七十九萬三千五百六十九尺六寸，以人功三百尺除之，即得。
答曰： a功 。
"""

#----- content starts here -----
"""
Suppose there is a city wall to be built. The top width is 2 zhang, the bottom width is 5 zhang 4 chi, the height is 3 zhang 8 chi, and the length is 5550 chi. 
The autumn labor capacity of one person is 300 chi. 
Question: how many labor units are required?

The procedure says: 
Place the length in li (convert to chi) and multiply it by 300 bu. 
For the remaining bu, divide by 6, obtaining 52824 chi. 
Add the top and bottom widths, obtaining 2 zhang 6 chi. 
Take half of this and multiply by the depth (height), obtaining 185 chi 4 cun. 
Multiply this by the length, obtaining 9793569 chi 6 cun. 
Divide this by the labor capacity of one person (300 chi), obtaining the number of labor units.

Answer: *a* labor units.
"""

from fractions import Fraction

# Dimensions of the wall
上廣 = 2  # in zhang
下廣 = 5 + Fraction(4, 10)  # 5 zhang 4 chi (convert chi to zhang)
高 = 3 + Fraction(8, 10)  # 3 zhang 8 chi (convert chi to zhang)
長 = 5550  # in chi

# Labor capacity of one person
人功 = 300  # in chi

# Step 1: Add the top and bottom widths
上下廣 = 上廣 + 下廣  # in zhang

# Step 2: Take half of the combined width
平均廣 = 上下廣 / 2  # in zhang

# Step 3: Multiply the average width by the height (depth)
截面積 = 平均廣 * 高  # in zhang^2

# Step 4: Convert the cross-sectional area to chi^2 (1 zhang = 10 chi)
截面積 = 截面積 * 100  # in chi^2

# Step 5: Multiply the cross-sectional area by the length
體積 = 截面積 * 長  # in chi^3

# Step 6: Divide the total volume by the labor capacity of one person
a = Fraction(體積, 人功)  # in labor units

# Final answer
a#----- content ends here -----

"""
"""
