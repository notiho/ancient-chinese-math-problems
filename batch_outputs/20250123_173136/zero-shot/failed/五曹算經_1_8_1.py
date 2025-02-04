"""
今有牆田方周一千步。問：為田㡬何？
術曰：列田方周一千步以四除之得二百五十步自相乘得六萬二千五百步以畝法除之即得。
答曰： a頃 奇 b步 。
"""

"""
To solve this problem, we need to determine the area of a square field given that its perimeter is 1000 steps. The solution involves dividing the perimeter by 4 to find the side length of the square, squaring the side length to find the area in square steps, and then converting the area into the appropriate units (qǐng and bù).

Here is the Python code to compute the solution:


"""


from fractions import Fraction

# Given data
perimeter = 1000  # steps

# Step 1: Calculate the side length of the square
side_length = Fraction(perimeter, 4)  # steps

# Step 2: Calculate the area in square steps
area_square_steps = side_length * side_length  # square steps

# Step 3: Convert square steps to qǐng and bù
# 1 qǐng = 10000 square steps
a = area_square_steps // 10000  # qǐng
b = area_square_steps % 10000  # square steps (bù)

# Results
a = int(a)  # Convert to integer for qǐng
b = int(b)  # Convert to integer for bù


"""


After running this code, the variables `a` and `b` will contain the solution:
- `a` is the number of qǐng.
- `b` is the remaining number of square steps (bù).
"""


"""
Variable 'a' has wrong value. Expected: 13/5, Actual: 6
Variable 'b' has wrong value. Expected: 100, Actual: 2500"""
