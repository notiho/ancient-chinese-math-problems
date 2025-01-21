"""
今有芻甍，下廣三丈，袤四丈，上袤二丈，無廣，高一丈。問︰積幾何？
術曰：倍下袤，上袤從之，以廣乘之，又以高乘之，六而一。
荅曰： a尺 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the volume of a frustum-like structure (trapezoidal prism). Here's the solution:


"""


from fractions import Fraction

# Given dimensions
lower_width = Fraction(3 * 10)  # Convert 3丈 to 尺 (1丈 = 10尺)
lower_length = Fraction(4 * 10)  # Convert 4丈 to 尺
upper_length = Fraction(2 * 10)  # Convert 2丈 to 尺
height = Fraction(1 * 10)  # Convert 1丈 to 尺

# Calculation
# Step 1: Double the lower length
double_lower_length = 2 * lower_length

# Step 2: Add the upper length
sum_lengths = double_lower_length + upper_length

# Step 3: Multiply by the lower width
area_base = sum_lengths * lower_width

# Step 4: Multiply by the height
volume = area_base * height

# Step 5: Divide by 6
a = volume / 6

# The answer is stored in variable 'a' in 尺³


"""


The variable `a` will contain the volume of the structure in cubic 尺 (尺³).
"""


"""
"""
