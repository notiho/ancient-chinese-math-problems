"""
今有方田，廣從各五十六步。問：為田㡬何？
術曰：列田五十六步自相乘，得三千一百三十六步，以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
To solve this problem, we need to calculate the area of a square field where each side is 56 steps long. The area is then converted into "畝" (a traditional Chinese unit of area) and "步" (a smaller unit of area). 

1 畝 = 240 步.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
side_length = 56  # steps
steps_per_mu = 240  # 1 畝 = 240 步

# Calculate the total area in steps
total_area_steps = side_length * side_length

# Convert the total area into 畝 and 步
a = total_area_steps // steps_per_mu  # Whole 畝
b = total_area_steps % steps_per_mu  # Remaining 步

# Results
a, b
#----- content ends here -----


"""


The variables `a` and `b` will contain the solution:
- `a` is the number of 畝.
- `b` is the remaining number of 步.
"""


"""
"""
