"""
今有屋基，南北三丈，東西六丈，欲以磚瓦砌之，凡積二尺，用磚五枚。問：計幾何？
術曰：置東西六丈，以南北三丈乘之，得一千八百尺；以五乘之，得九千尺；以二除之，即得。
答曰： a枚 。
"""

"""
To solve this problem, we will calculate the total number of bricks needed to construct the wall. Here's the Python code:


"""


from fractions import Fraction

# Dimensions of the base
south_north = Fraction(3 * 10)  # Convert 丈 to 尺 (1 丈 = 10 尺)
east_west = Fraction(6 * 10)    # Convert 丈 to 尺 (1 丈 = 10 尺)

# Total area in square 尺
total_area = south_north * east_west

# Bricks needed for every 2 cubic 尺
bricks_per_2_cubic_feet = 5

# Total bricks needed
a = total_area * bricks_per_2_cubic_feet / 2

# Result
a


"""


The variable `a` will contain the total number of bricks needed.
"""


"""
"""
