"""
今有木，方三尺，高三尺，欲方五寸作枕一枚。問：得幾何？
術曰：置方三尺，自相乘，得九尺，以高三尺乘之，得二十七尺，以一尺木八枕乘之，即得。
答曰： a枚 。
"""

"""
This problem involves calculating how many wooden pillows (each with a volume of 5寸 x 5寸 x 5寸) can be made from a cubic wooden block with dimensions 3尺 x 3尺 x 3尺.

### Translation into Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Dimensions of the wooden block in 尺
side_length = 3  # 尺
height = 3  # 尺

# Volume of the wooden block in cubic 尺
block_volume = side_length * side_length * height  # 尺^3

# Dimensions of one pillow in 寸
pillow_side_length = 5  # 寸

# Convert pillow dimensions to 尺 (1 尺 = 10 寸)
pillow_side_length_in_尺 = Fraction(pillow_side_length, 10)  # 尺

# Volume of one pillow in cubic 尺
pillow_volume = pillow_side_length_in_尺 ** 3  # 尺^3

# Number of pillows that can be made
a = block_volume // pillow_volume  # 枚

# Result
a  # 枚
#----- content ends here -----


"""


### Explanation:
1. The wooden block has dimensions 3尺 x 3尺 x 3尺, so its volume is \( 3 \times 3 \times 3 = 27 \) cubic 尺.
2. Each pillow has dimensions 5寸 x 5寸 x 5寸. Converting to 尺, this becomes \( \frac{5}{10} \) 尺 x \( \frac{5}{10} \) 尺 x \( \frac{5}{10} \) 尺, or \( \frac{1}{2} \) 尺 x \( \frac{1}{2} \) 尺 x \( \frac{1}{2} \) 尺.
3. The volume of one pillow is \( \left(\frac{1}{2}\right)^3 = \frac{1}{8} \) cubic 尺.
4. The number of pillows that can be made is the total volume of the block divided by the volume of one pillow: \( 27 \div \frac{1}{8} = 27 \times 8 = 216 \).
5. Thus, \( a = 216 \) pillows.


"""


"""
"""
