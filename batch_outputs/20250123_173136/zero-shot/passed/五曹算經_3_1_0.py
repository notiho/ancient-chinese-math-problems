"""
今有粟二百九十斛。問：為粺米㡬何？
術曰：列粟二百九十斛，以二十七乘之得七千八百三十斛，以五十除之即得。
答曰： a斛 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves converting 290 hu (斛) of grain into polished rice. The calculation involves multiplying by 27 and then dividing by 50.

Here is the Python code:


"""


from fractions import Fraction

# Given values
grain = 290  # in hu

# Calculation
a = Fraction(grain * 27, 50)  # result in hu

# The answer is stored in variable 'a'


"""


The variable `a` will hold the result in hu (斛).
"""


"""
"""
