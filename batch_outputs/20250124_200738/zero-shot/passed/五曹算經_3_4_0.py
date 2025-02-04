"""
今有粟五百六十斛，凡粟八斗易麥五斗。問：得麥㡬何？
術曰：列粟五百六十斛，以五十乘之得二萬八千斛，以八千除之即得。
答曰： a斛 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves converting a quantity of 粟 (millet) into 麥 (wheat) based on a given exchange rate. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
粟 = 560  # 粟 in 斛
粟_to_麥_ratio = Fraction(5, 8)  # 8斗粟 exchanges for 5斗麥

# Conversion
a = 粟 * 粟_to_麥_ratio

# Result
a  # 麥 in 斛
#----- content ends here -----


"""


The variable `a` represents the amount of 麥 (wheat) in 斛.
"""


"""
"""
