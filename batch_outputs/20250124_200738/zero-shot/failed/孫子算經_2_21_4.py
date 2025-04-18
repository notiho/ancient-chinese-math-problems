"""
今有築城，上廣二丈，下廣五丈四尺，高三丈八尺，長五千五百五十尺，秋程人功三百尺。問：須功幾何？
術曰：置里數以三百步乘之，內零步，六之，得五萬二千八百二十四尺，并上下廣，得二丈六寸，半之，以深乘之，得一百八十五尺四寸，以長乘得九百七十九萬三千五百六十九尺六寸，以人功三百尺除之，即得。
答曰： a功 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the total amount of work (功) required to build a city wall based on its dimensions and the work rate of workers. Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions of the city wall
top_width = Fraction(2)  # 2丈
bottom_width = Fraction(5) + Fraction(4, 10)  # 5丈4尺 = 5 + 4/10 丈
height = Fraction(3) + Fraction(8, 10)  # 3丈8尺 = 3 + 8/10 丈
length = Fraction(5550)  # 5550尺
work_rate = Fraction(300)  # 300尺 per person

# Step 1: Calculate the average width
average_width = (top_width + bottom_width) / 2

# Step 2: Calculate the cross-sectional area
cross_sectional_area = average_width * height

# Step 3: Calculate the total volume
total_volume = cross_sectional_area * length

# Step 4: Calculate the total work required
a = total_volume / work_rate

# The answer is stored in variable 'a'
a
#----- content ends here -----


"""


### Explanation of the Code:
1. **Dimensions Conversion**: All dimensions are converted into fractions to handle non-integer values (e.g., 4尺 = 4/10丈).
2. **Average Width**: The average width is calculated as the mean of the top and bottom widths.
3. **Cross-Sectional Area**: The cross-sectional area is calculated by multiplying the average width by the height.
4. **Total Volume**: The total volume is obtained by multiplying the cross-sectional area by the length of the wall.
5. **Total Work**: The total work required is calculated by dividing the total volume by the work rate (300尺 per person).

### Units:
- All calculations are performed in terms of 丈 and 尺.
- The final result `a` represents the total work required in terms of "person-work" (功).


"""


"""
Variable 'a' has wrong value. Expected: 26011, Actual: 26011/100"""
