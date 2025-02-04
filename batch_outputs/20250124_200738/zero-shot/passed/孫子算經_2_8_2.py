"""
今有屋基，南北三丈，東西六丈，欲以磚瓦砌之，凡積二尺，用磚五枚。問：計幾何？
術曰：置東西六丈，以南北三丈乘之，得一千八百尺；以五乘之，得九千尺；以二除之，即得。
答曰： a枚 。
"""

"""
To solve this problem, we will calculate the number of bricks (a枚) required to build the structure. Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Dimensions of the base
south_north = Fraction(3 * 10)  # 南北三丈 (converted to 尺)
east_west = Fraction(6 * 10)    # 東西六丈 (converted to 尺)

# Volume of the base
volume = south_north * east_west  # 面積 in 尺^2

# Total number of bricks required
a = (volume * 5) / 2  # 每二尺用五枚

# Result
a  # Number of bricks
#----- content ends here -----


"""


The variable `a` will store the number of bricks required.
"""


"""
"""
