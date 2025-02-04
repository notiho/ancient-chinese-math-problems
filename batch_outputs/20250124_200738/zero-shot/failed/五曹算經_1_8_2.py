"""
今有牆田方周一千步。問：為田㡬何？
術曰：列田方周一千步以四除之得二百五十步自相乘得六萬二千五百步以畝法除之即得。
答曰： a頃 奇 b步 。
"""

"""
To solve this problem, we need to determine the area of a square field given its perimeter. The perimeter is 1000 steps, and we are tasked with finding the area in terms of "頃" (qing) and "步" (bu). 

1 "頃" = 10000 "步" (conversion factor).

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given perimeter of the square field
perimeter = 1000  # in steps

# Step 1: Calculate the side length of the square
side_length = Fraction(perimeter, 4)  # side length = perimeter / 4

# Step 2: Calculate the area of the square in "步"
area_in_bu = side_length * side_length  # area = side_length^2

# Step 3: Convert the area into "頃" and "步"
a = area_in_bu // 10000  # Number of "頃" (1頃 = 10000步)
b = area_in_bu % 10000   # Remaining "步"

# Results
a = int(a)  # Convert to integer for "頃"
b = int(b)  # Convert to integer for "步"
#----- content ends here -----


"""


After running this code, the values of `a` and `b` will represent the area of the field in "頃" and "步", respectively.
"""


"""
Variable 'a' has wrong value. Expected: 13/5, Actual: 6
Variable 'b' has wrong value. Expected: 100, Actual: 2500"""
