"""
今有木，方三尺，高三尺，欲方五寸作枕一枚。問：得幾何？
術曰：置方三尺，自相乘，得九尺，以高三尺乘之，得二十七尺，以一尺木八枕乘之，即得。
答曰： a枚 。
"""

"""
To solve this problem, we need to calculate how many wooden pillows (枕) can be made from a cubic piece of wood. The original wood is a cube with dimensions 3 feet by 3 feet by 3 feet, and each pillow is a cube with dimensions 5 inches by 5 inches by 5 inches. Let's compute this step by step.

1. Convert the dimensions of the pillow from inches to feet since the original wood is measured in feet. There are 12 inches in a foot, so 5 inches is \( \frac{5}{12} \) feet.
2. Calculate the volume of the original wood in cubic feet.
3. Calculate the volume of one pillow in cubic feet.
4. Divide the total volume of the wood by the volume of one pillow to determine how many pillows can be made.

Here is the Python code:


"""


from fractions import Fraction

# Dimensions of the original wood in feet
side_length_original = 3  # feet
volume_original = side_length_original ** 3  # cubic feet

# Dimensions of one pillow in feet
side_length_pillow = Fraction(5, 12)  # 5 inches converted to feet
volume_pillow = side_length_pillow ** 3  # cubic feet

# Calculate the number of pillows
a = volume_original // volume_pillow  # Integer division to get whole pillows


"""


The variable `a` will contain the number of pillows that can be made.
"""


"""
Variable 'a' has wrong value. Expected: 216, Actual: 373"""
