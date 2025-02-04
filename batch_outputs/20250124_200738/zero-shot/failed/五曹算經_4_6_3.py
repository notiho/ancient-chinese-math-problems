"""
今有倉從一丈三尺廣六尺高一丈中有從牽二枚方五寸從一丈三尺又横牽三枚方四寸從六尺又柱一枚周三尺高一丈。問：受粟㡬何？
術曰：列從一丈三尺上十之得一百三十寸以廣六十寸乘之得七千八百寸又列高一丈上十之為一百寸以乘之得七十八萬寸為都積又列從牽二枚方五寸自相乘得二十五寸以從一百三十寸乘之得三千二百五十寸以從牽二枚乘之得六千五百寸又列横牽三枚方四寸自相乘得十六寸以從六十寸乘之得九百六十寸以横牽三枚乘之得二千八百八十寸又列柱一枚周三尺上十之得三十寸自相乘得九百寸以高一百寸乘之得九萬寸以十二除之得七千五百寸并從横牽及柱等三位得一萬六千八百八十寸以減都積餘七十六萬三千一百二十寸為實以斛法一千六百二十寸除之即得。
答曰： a斛 奇 b寸 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the volume of a granary while subtracting the volumes of certain objects inside it. The final result will be expressed in units of "斛" and "寸". Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Dimensions of the granary
length = 130  # 1丈3尺 = 130寸
width = 60  # 6尺 = 60寸
height = 100  # 1丈 = 100寸

# Total volume of the granary
total_volume = length * width * height

# Volume of the first obstruction (牽二枚方五寸)
side_1 = 5  # 方五寸 = 5寸 x 5寸
volume_1 = side_1 * side_1 * length * 2  # Two such obstructions

# Volume of the second obstruction (横牽三枚方四寸)
side_2 = 4  # 方四寸 = 4寸 x 4寸
volume_2 = side_2 * side_2 * width * 3  # Three such obstructions

# Volume of the third obstruction (柱一枚周三尺高一丈)
circumference = 30  # 周三尺 = 30寸
radius = circumference / (2 * 3.141592653589793)  # Calculate radius from circumference
volume_3 = 3.141592653589793 * radius * radius * height  # Volume of the cylinder
volume_3 = volume_3 / 12  # Divided by 12 as per the problem

# Total volume of obstructions
total_obstruction_volume = volume_1 + volume_2 + volume_3

# Remaining volume of the granary
remaining_volume = total_volume - total_obstruction_volume

# Convert remaining volume to "斛" and "寸"
volume_per_hu = 1620  # 1斛 = 1620寸
a = remaining_volume // volume_per_hu  # Number of "斛"
b = remaining_volume % volume_per_hu  # Remaining "寸"

# Results
a = Fraction(a)
b = Fraction(b)

# Output the results
a, b
#----- content ends here -----


"""


This code calculates the values of `a` (number of "斛") and `b` (remaining "寸") based on the given problem. The use of the `Fraction` class ensures that any fractional values are represented accurately.
"""


"""
Variable 'a' has wrong value. Expected: 471, Actual: 475
Variable 'b' has wrong value. Expected: 100, Actual: 4493987176217/8589934592"""
