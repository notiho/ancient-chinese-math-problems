"""
今有粟三百六十二斛。問：為御米㡬何？
術曰：列粟三百六十二斛，以二十一升乘之得七千六百二斛，以五十除之即得。
答曰： a斛 。
"""

"""
To solve this problem, let's translate the ancient Chinese math problem into Python code. The problem involves converting 362斛 (a unit of volume) of 粟 (grain) into 御米 (processed rice) using the given method.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
粟 = 362  # in 斛
conversion_factor = Fraction(21, 50)  # 21升 per 50升

# Calculation
a = 粟 * conversion_factor  # Result in 斛

# Output the result
a  # This will hold the value of 御米 in 斛
#----- content ends here -----


"""


The variable `a` will contain the answer in 斛 as a `Fraction`.
"""


"""
"""
