"""
今有簫田從四十八步一頭廣二十五步一頭廣三十五步。問：為田㡬何？
術曰：并二廣得六十步半之得三十步以從四十八步乘之得一千四百四十步以畝法除之即得。
答曰： a畝
"""

"""
To solve this problem, we will calculate the area of the field (田) in "畝" (a traditional Chinese unit of area). The field has two widths, 25 steps and 35 steps, and a length of 48 steps. The method involves taking the average width, multiplying it by the length, and then converting the result into "畝."

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
length = 48  # steps
width1 = 25  # steps
width2 = 35  # steps

# Calculate the average width
average_width = Fraction(width1 + width2, 2)  # steps

# Calculate the area in square steps
area_in_square_steps = average_width * length  # steps^2

# Conversion factor: 240 square steps = 1 畝
conversion_factor = 240  # steps^2 per 畝

# Calculate the area in 畝
a = area_in_square_steps / conversion_factor

# The result is stored in variable 'a'
#----- content ends here -----


"""


The variable `a` will contain the area of the field in 畝 as a `Fraction`.
"""


"""
"""
