"""
今有簫田從四十八步一頭廣二十五步一頭廣三十五步。問：為田㡬何？
術曰：并二廣得六十步半之得三十步以從四十八步乘之得一千四百四十步以畝法除之即得。
答曰： a畝
"""

"""
To solve this problem, we will calculate the area of the field using the given dimensions and convert it into "畝" (a traditional Chinese unit of area). Here's the Python code:


"""


from fractions import Fraction

# Given dimensions
length = 48  # in steps
width1 = 25  # in steps
width2 = 35  # in steps

# Average width
average_width = Fraction(width1 + width2, 2)

# Area in square steps
area_steps = length * average_width

# Conversion factor: 1 畝 = 240 square steps
area_mu = area_steps / 240

# Assign the result to variable 'a'
a = area_mu

# Result
a  # in 畝


"""


The variable `a` will contain the area of the field in 畝.
"""


"""
"""
