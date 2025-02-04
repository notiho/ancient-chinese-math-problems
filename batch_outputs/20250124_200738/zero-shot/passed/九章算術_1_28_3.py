"""
今有箕田，舌廣二十步，踵廣五步，正從三十步。問：為田幾何？
術曰：并踵、舌而半之，以乘正從。畝法而一。
荅曰： a畝 。
"""

"""
To translate the ancient Chinese math problem into Python code, we will compute the area of the field (田) based on the given dimensions and the method described. Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions
舌廣 = 20  # in 步
踵廣 = 5   # in 步
正從 = 30  # in 步

# Calculation
a = Fraction((舌廣 + 踵廣), 2) * 正從  # Area in 步^2

# Convert 步^2 to 畝 (1 畝 = 240 步^2)
a = a / 240

# The result is stored in variable 'a' in 畝
#----- content ends here -----


"""


The variable `a` will contain the area of the field in 畝.
"""


"""
"""
