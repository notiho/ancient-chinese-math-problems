"""
今有木，方三尺，高三尺，欲方五寸作枕一枚。問：得幾何？
術曰：置方三尺，自相乘，得九尺，以高三尺乘之，得二十七尺，以一尺木八枕乘之，即得。
答曰： a枚 。
"""

"""
To solve this problem, we need to calculate how many wooden pillows (each with dimensions of a cube with a side length of 5 inches) can be made from a wooden block with dimensions of 3 feet by 3 feet by 3 feet.

### Step-by-step solution:
1. Convert all dimensions to the same unit. Since the pillow dimensions are given in inches, convert the wooden block dimensions from feet to inches:
   - 1 foot = 12 inches
   - Wooden block dimensions: 3 feet × 3 feet × 3 feet = 36 inches × 36 inches × 36 inches.

2. Calculate the volume of the wooden block:
   - Volume = 36 × 36 × 36 cubic inches.

3. Calculate the volume of one pillow:
   - Each pillow is a cube with a side length of 5 inches.
   - Volume of one pillow = 5 × 5 × 5 cubic inches.

4. Divide the total volume of the wooden block by the volume of one pillow to determine how many pillows can be made.

### Python Code:

"""


from fractions import Fraction

# Dimensions of the wooden block in inches
block_side = 36  # inches
block_volume = block_side * block_side * block_side  # cubic inches

# Dimensions of one pillow in inches
pillow_side = 5  # inches
pillow_volume = pillow_side * pillow_side * pillow_side  # cubic inches

# Calculate the number of pillows
a = block_volume // pillow_volume  # Integer division to get the number of full pillows


"""


### Final Answer:
The variable `a` will contain the number of pillows that can be made.
"""


"""
Variable 'a' has wrong value. Expected: 216, Actual: 373"""
