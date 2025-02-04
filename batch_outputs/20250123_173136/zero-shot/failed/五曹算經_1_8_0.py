"""
今有牆田方周一千步。問：為田㡬何？
術曰：列田方周一千步以四除之得二百五十步自相乘得六萬二千五百步以畝法除之即得。
答曰： a頃 奇 b步 。
"""

"""
To solve this problem, we need to calculate the area of a square field given its perimeter. The perimeter of the square field is 1000 steps. The solution involves dividing the perimeter by 4 to find the side length of the square, squaring the side length to find the area in square steps, and then converting the area into the appropriate units of "頃" and "步."

Here is the Python code:


"""


from fractions import Fraction

# Given data
perimeter = 1000  # steps

# Step 1: Calculate the side length of the square
side_length = Fraction(perimeter, 4)  # steps

# Step 2: Calculate the area in square steps
area_in_square_steps = side_length * side_length  # steps^2

# Step 3: Convert the area into "頃" and "步"
# 1 頃 = 100 畝, and 1 畝 = 240 步^2
area_in_mu = area_in_square_steps / 240  # 畝
a = area_in_mu // 100  # 頃 (integer part)
b = area_in_mu % 100  # 畝 (remainder)

# Output the results
a = int(a)  # 頃
b = Fraction(b)  # 畝


"""


The solution is stored in the variables `a` (in "頃") and `b` (in "畝").
"""


"""
Variable 'a' has wrong value. Expected: 13/5, Actual: 2
Variable 'b' has wrong value. Expected: 100, Actual: 725/12"""
