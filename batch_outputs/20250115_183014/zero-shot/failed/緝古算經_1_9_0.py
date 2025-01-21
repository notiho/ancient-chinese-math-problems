"""
假令有粟二萬三千一百二十斛七斗三升，欲作方倉一，圓窖一，盛各滿中而粟適盡。令高、深等，使方面少於圓徑九寸，多於高二丈九尺八寸，率徑七，周二十二。問：方、徑、深多少？
求方、徑高深，術曰：十四乘斛法，以乘粟數，二十五而一，為實。又倍多加少，以乘少數，又十一乘之，二十五而一，多自乘加之，為方法。又倍少數，十一乘之，二十五而一，又倍多加之，為廉法，從。開立方除之，即高、深。各加差，即方徑。還元，術曰：倉方自乘，以高乘之，為實。圓徑自乘，以深乘之，一十一乘，一十四而一，為實。皆為斛法除之，即得容粟。
答曰：倉方 a丈 ，窖徑 b丈 ，高與深各 c丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves finding the dimensions of a square granary and a circular granary such that their volumes match the given amount of grain. The solution involves cubic equations and the relationship between the dimensions.

Here is the Python code:


"""


from fractions import Fraction

# Given data
grain_volume = Fraction(2312073, 10)  # 粟二萬三千一百二十斛七斗三升 (斛 as the unit)
pi_ratio = Fraction(22, 7)  # 圓周率 22/7

# Step 1: Calculate the total volume factor
volume_factor = Fraction(14) * grain_volume / Fraction(25)

# Step 2: Calculate the square granary side length (方)
side_difference = Fraction(29, 10)  # 多於高二丈九尺八寸 (2丈9尺8寸 = 29/10丈)
diameter_difference = Fraction(9, 10)  # 少於圓徑九寸 (9寸 = 9/10丈)

# Calculate the square granary side length (方法)
side_factor = (2 * side_difference + diameter_difference) * side_difference
side_factor = side_factor * Fraction(11) / Fraction(25)
side_factor += side_difference ** 2
side_length_cubed = volume_factor / side_factor

# Solve for the side length (方)
a = side_length_cubed ** Fraction(1, 3)

# Step 3: Calculate the circular granary diameter (圓徑)
diameter_factor = (2 * diameter_difference + side_difference) * diameter_difference
diameter_factor = diameter_factor * Fraction(11) / Fraction(25)
diameter_factor += diameter_difference ** 2
diameter_length_cubed = volume_factor / diameter_factor

# Solve for the diameter (圓徑)
b = diameter_length_cubed ** Fraction(1, 3)

# Step 4: Calculate the height/depth (高與深)
c = a - side_difference  # 高與深各 c丈

# Results
a = round(float(a), 2)  # 倉方 a丈
b = round(float(b), 2)  # 窖徑 b丈
c = round(float(c), 2)  # 高與深各 c丈

# Output the results
a, b, c


"""


This code calculates the dimensions of the square granary (side length `a`), the circular granary (diameter `b`), and the height/depth (`c`) based on the given relationships and constraints. The results are stored in variables `a`, `b`, and `c`.
"""


"""
Variable 'a' has wrong value. Expected: 453/100, Actual: 19.69
Variable 'b' has wrong value. Expected: 231/50, Actual: 36.46
Variable 'c' has wrong value. Expected: 31/20, Actual: 16.79"""
