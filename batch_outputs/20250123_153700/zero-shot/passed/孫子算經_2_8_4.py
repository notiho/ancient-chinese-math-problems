"""
今有屋基，南北三丈，東西六丈，欲以磚瓦砌之，凡積二尺，用磚五枚。問：計幾何？
術曰：置東西六丈，以南北三丈乘之，得一千八百尺；以五乘之，得九千尺；以二除之，即得。
答曰： a枚 。
"""

"""
To solve this problem, we will calculate the number of bricks required to pave the given area. Here's the Python code:


"""


from fractions import Fraction

# Given dimensions of the area
length = 6 * 10  # 東西六丈 (converted to 尺, 1丈 = 10尺)
width = 3 * 10   # 南北三丈 (converted to 尺, 1丈 = 10尺)

# Area of the base in square 尺
area = length * width  # 面積 = 東西 * 南北

# Number of bricks required for every 2 cubic 尺
bricks_per_2_cubic_feet = 5

# Total number of bricks required
a = Fraction(area * bricks_per_2_cubic_feet, 2)  # Divide by 2 cubic 尺

# The result is stored in variable 'a'


"""


The variable `a` will contain the number of bricks required.
"""


"""
"""
