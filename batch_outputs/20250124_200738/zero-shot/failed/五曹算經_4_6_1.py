"""
今有倉從一丈三尺廣六尺高一丈中有從牽二枚方五寸從一丈三尺又横牽三枚方四寸從六尺又柱一枚周三尺高一丈。問：受粟㡬何？
術曰：列從一丈三尺上十之得一百三十寸以廣六十寸乘之得七千八百寸又列高一丈上十之為一百寸以乘之得七十八萬寸為都積又列從牽二枚方五寸自相乘得二十五寸以從一百三十寸乘之得三千二百五十寸以從牽二枚乘之得六千五百寸又列横牽三枚方四寸自相乘得十六寸以從六十寸乘之得九百六十寸以横牽三枚乘之得二千八百八十寸又列柱一枚周三尺上十之得三十寸自相乘得九百寸以高一百寸乘之得九萬寸以十二除之得七千五百寸并從横牽及柱等三位得一萬六千八百八十寸以減都積餘七十六萬三千一百二十寸為實以斛法一千六百二十寸除之即得。
答曰： a斛 奇 b寸 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the volume of a warehouse after accounting for the space taken up by beams and columns. The final answer is expressed in terms of "斛" (a unit of volume) and remaining "寸" (cubic inches).

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Dimensions of the warehouse
length = 130  # 1丈3尺 = 130寸
width = 60    # 6尺 = 60寸
height = 100  # 1丈 = 100寸

# Total volume of the warehouse
total_volume = length * width * height

# Volume taken by the two vertical beams (牽二枚方五寸)
beam_side = 5  # 5寸
beam_volume = (beam_side ** 2) * length * 2  # Two beams

# Volume taken by the three horizontal beams (横牽三枚方四寸)
horizontal_beam_side = 4  # 4寸
horizontal_beam_volume = (horizontal_beam_side ** 2) * width * 3  # Three beams

# Volume taken by the column (柱一枚周三尺高一丈)
column_circumference = 30  # 3尺 = 30寸
column_radius = column_circumference / (2 * Fraction(22, 7))  # Circumference = 2πr
column_volume = Fraction(22, 7) * (column_radius ** 2) * height  # πr^2h
column_volume = column_volume / 12  # Adjust for the column's shape

# Total volume taken by beams and column
obstruction_volume = beam_volume + horizontal_beam_volume + column_volume

# Remaining volume in the warehouse
remaining_volume = total_volume - obstruction_volume

# Convert remaining volume to "斛" and "寸"
unit_volume = 1620  # 1斛 = 1620 cubic寸
a = remaining_volume // unit_volume  # Number of 斛
b = remaining_volume % unit_volume  # Remaining cubic 寸

# Output the results
a = Fraction(a)
b = Fraction(b)
#----- content ends here -----


"""


The variables `a` and `b` contain the final answer in terms of "斛" and "寸".
"""


"""
Variable 'a' has wrong value. Expected: 471, Actual: 475
Variable 'b' has wrong value. Expected: 100, Actual: 11515/22"""
