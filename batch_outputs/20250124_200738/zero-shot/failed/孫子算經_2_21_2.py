"""
今有築城，上廣二丈，下廣五丈四尺，高三丈八尺，長五千五百五十尺，秋程人功三百尺。問：須功幾何？
術曰：置里數以三百步乘之，內零步，六之，得五萬二千八百二十四尺，并上下廣，得二丈六寸，半之，以深乘之，得一百八十五尺四寸，以長乘得九百七十九萬三千五百六十九尺六寸，以人功三百尺除之，即得。
答曰： a功 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the amount of labor required to build a city wall with given dimensions and labor efficiency.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions and values
top_width = Fraction(2, 1)  # 2丈 (top width)
bottom_width = Fraction(5, 1) + Fraction(4, 10)  # 5丈4尺 (bottom width)
height = Fraction(3, 1) + Fraction(8, 10)  # 3丈8尺 (height)
length = Fraction(5550, 1)  # 5550尺 (length)
labor_efficiency = Fraction(300, 1)  # 300尺 per person

# Step 1: Add top and bottom widths
total_width = top_width + bottom_width  # Total width

# Step 2: Divide the total width by 2
average_width = total_width / 2  # Average width

# Step 3: Multiply the average width by the height
cross_section_area = average_width * height  # Cross-sectional area

# Step 4: Multiply the cross-sectional area by the length
total_volume = cross_section_area * length  # Total volume

# Step 5: Divide the total volume by labor efficiency
a = total_volume / labor_efficiency  # Total labor required

# The result is stored in variable 'a'
a
#----- content ends here -----


"""


### Explanation of the Code:
1. **Units Conversion**: The dimensions are given in 丈 and 尺. Since 1丈 = 10尺, we convert all dimensions into 尺 for consistency.
2. **Cross-sectional Area**: The average width is calculated by averaging the top and bottom widths. The cross-sectional area is then calculated by multiplying the average width by the height.
3. **Total Volume**: The total volume of the wall is calculated by multiplying the cross-sectional area by the length.
4. **Labor Calculation**: The total labor required is calculated by dividing the total volume by the labor efficiency (300尺 per person).

### Final Answer:
The variable `a` contains the total labor required in terms of the number of people needed.
"""


"""
Variable 'a' has wrong value. Expected: 26011, Actual: 26011/100"""
