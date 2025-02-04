"""
今有牆田方周一千步。問：為田㡬何？
術曰：列田方周一千步以四除之得二百五十步自相乘得六萬二千五百步以畝法除之即得。
答曰： a頃 奇 b步 。
"""

"""
To solve this problem, we need to compute the area of a square field given its perimeter. The perimeter is 1000 steps, and the solution involves dividing the perimeter by 4 to find the side length, squaring the side length to find the area in square steps, and then converting the area into "頃" and "步" using the appropriate conversion factors.

1 "頃" = 100 畝  
1 畝 = 240 步²  

Here is the Python code to compute the solution:


"""


from fractions import Fraction

# Given data
perimeter = 1000  # in steps

# Step 1: Calculate the side length of the square field
side_length = Fraction(perimeter, 4)  # side length in steps

# Step 2: Calculate the area in square steps
area_in_steps_squared = side_length * side_length  # area in steps²

# Step 3: Convert the area into 畝
area_in_mu = area_in_steps_squared / 240  # 1 畝 = 240 步²

# Step 4: Convert 畝 into 頃 and 步
a = area_in_mu // 100  # 1 頃 = 100 畝
remaining_mu = area_in_mu % 100
b = remaining_mu * 240  # Convert remaining 畝 back to 步²

# Final results
a = int(a)  # 頃
b = int(b)  # 步²

# Output variables a and b


"""


After running this code, the variables `a` and `b` will contain the values of the area in "頃" and "步²", respectively.
"""


"""
Variable 'a' has wrong value. Expected: 13/5, Actual: 2
Variable 'b' has wrong value. Expected: 100, Actual: 14500"""
