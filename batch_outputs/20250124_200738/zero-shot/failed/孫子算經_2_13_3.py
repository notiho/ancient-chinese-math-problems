"""
今有方田桑生中央，從角至桑，一百四十七步。問：為田幾何？
術曰：置角至桑一百四十七步，倍之，得二百九十四步，以五乘之，得一千四百七十步，以七除之，得二百一十步，自相乘，得四萬四千一百步，以二百四十步除之，即得。
答曰： a頃 ，奇 b步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the area of a square field based on the given steps and operations. Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
steps_to_center = 147  # steps from the corner to the center

# Calculations
doubled_steps = steps_to_center * 2  # Double the steps
multiplied_by_five = doubled_steps * 5  # Multiply by 5
divided_by_seven = Fraction(multiplied_by_five, 7)  # Divide by 7
side_length = divided_by_seven  # The side length of the square field
area_in_steps = side_length * side_length  # Area in square steps
area_in_qing = Fraction(area_in_steps, 240)  # Convert to qing (1 qing = 240 square steps)

# Extract the integer part (qing) and the remainder (steps)
a = area_in_qing.numerator // area_in_qing.denominator  # Integer part (qing)
b = area_in_qing.numerator % area_in_qing.denominator  # Remainder (steps)

# Results
a, b  # a qing, b steps
#----- content ends here -----


"""


### Explanation:
1. Start with the given steps from the corner to the center (`147` steps).
2. Double the steps, multiply by 5, and divide by 7 to calculate the side length of the square field.
3. Square the side length to find the area in square steps.
4. Convert the area from square steps to qing using the conversion factor `1 qing = 240 square steps`.
5. Extract the integer part (`a`, in qing) and the remainder (`b`, in steps).

The variables `a` and `b` will contain the final answer: `a` qing and `b` steps.
"""


"""
Variable 'a' has wrong value. Expected: 183/100, Actual: 183
Variable 'b' has wrong value. Expected: 180, Actual: 3"""
