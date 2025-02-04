"""
今有屋基，南北三丈，東西六丈，欲以磚瓦砌之，凡積二尺，用磚五枚。問：計幾何？
術曰：置東西六丈，以南北三丈乘之，得一千八百尺；以五乘之，得九千尺；以二除之，即得。
答曰： a枚 。
"""

"""
To solve this problem, we will calculate the number of bricks needed to pave the given area. Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Dimensions of the area
length = 6 * 10  # 東西六丈 converted to 尺 (1丈 = 10尺)
width = 3 * 10   # 南北三丈 converted to 尺 (1丈 = 10尺)

# Area in square 尺
area = length * width  # 面積 = 東西 * 南北

# Bricks needed per 2 square 尺
bricks_per_2_square_feet = 5  # 每二尺用磚五枚

# Total bricks needed
a = Fraction(area * bricks_per_2_square_feet, 2)  # 總磚數 = 面積 * 每二尺磚數 / 2

# Result
a
#----- content ends here -----


"""


The variable `a` will contain the total number of bricks needed.
"""


"""
"""
