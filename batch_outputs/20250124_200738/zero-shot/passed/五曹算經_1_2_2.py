"""
今有直田廣八十步從一百九十步。問：為田㡬何？
術曰：列廣八十步以從一百九十步乘之得一萬五千二百步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
To solve this problem, we need to calculate the area of a rectangular field given its width (廣) and length (從), and then convert the area into "畝" (a traditional Chinese unit of area) and "步" (a smaller unit of area). The conversion factor is typically 240 square "步" per "畝".

Here is the Python code to compute the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions of the field
width = 80  # in steps (步)
length = 190  # in steps (步)

# Calculate the total area in square steps (步^2)
total_area = width * length  # in square steps

# Conversion factor: 1 畝 = 240 square steps
area_in_mu = total_area // 240  # whole 畝
remaining_steps = total_area % 240  # remaining square steps (步)

# Assign the results to variables
a = area_in_mu  # 畝
b = remaining_steps  # 步

# Output the results
a, b
#----- content ends here -----


"""


### Explanation:
1. The area of the field is calculated as `width * length`.
2. The total area in square steps is then divided by 240 to determine how many full "畝" (a) the area contains.
3. The remainder of the division gives the leftover area in square steps (b).

### Solution:
The variables `a` and `b` will contain the number of "畝" and "步" respectively.
"""


"""
"""
