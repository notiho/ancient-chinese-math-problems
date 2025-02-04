"""
今有簫田從四十八步一頭廣二十五步一頭廣三十五步。問：為田㡬何？
術曰：并二廣得六十步半之得三十步以從四十八步乘之得一千四百四十步以畝法除之即得。
答曰： a畝
"""

"""
To solve this problem, we will compute the area of the field in terms of "畝" (a traditional Chinese unit of area). The field has two widths: 25 steps and 35 steps, and a length of 48 steps. The average width is used to calculate the area.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
length = 48  # steps
width1 = 25  # steps
width2 = 35  # steps

# Calculate the average width
average_width = Fraction(width1 + width2, 2)  # steps

# Calculate the area in square steps
area_in_square_steps = length * average_width  # steps^2

# Convert square steps to 畝 (1 畝 = 240 square steps)
a = area_in_square_steps / 240  # 畝

# The result is stored in variable 'a'
#----- content ends here -----


"""


The value of `a` will represent the area of the field in 畝.
"""


"""
"""
