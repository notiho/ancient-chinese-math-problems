"""
今有屋基，南北三丈，東西六丈，欲以磚瓦砌之，凡積二尺，用磚五枚。問：計幾何？
術曰：置東西六丈，以南北三丈乘之，得一千八百尺；以五乘之，得九千尺；以二除之，即得。
答曰： a枚 。
"""

"""
To solve this problem, we will calculate the number of bricks required to build a wall for the given dimensions. Here's the Python code:


"""


from fractions import Fraction

# Dimensions of the base
south_north = Fraction(3 * 10)  # 3丈 converted to 尺 (1丈 = 10尺)
east_west = Fraction(6 * 10)    # 6丈 converted to 尺 (1丈 = 10尺)

# Calculate the area in square 尺
area = south_north * east_west  # 南北 * 東西

# Bricks required per 2 cubic 尺
bricks_per_two_cubic_feet = 5

# Total volume in cubic 尺
total_volume = area * 2  # Multiply by 2 because the height is 2尺

# Total number of bricks required
a = total_volume / 2 * bricks_per_two_cubic_feet

# Result
a


"""


The variable `a` will contain the total number of bricks required.
"""


"""
Variable 'a' has wrong value. Expected: 4500, Actual: 9000"""
