"""
今有粟五百六十斛，凡粟八斗易麥五斗。問：得麥㡬何？
術曰：列粟五百六十斛，以五十乘之得二萬八千斛，以八千除之即得。
答曰： a斛 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem states that 560斛 of 粟 (millet) is exchanged at a rate of 8斗 of 粟 for 5斗 of 麥 (wheat). We need to calculate how much 麥 (wheat) is obtained.

Here is the Python code:


"""


from fractions import Fraction

# Given values
粟 = 560  # in 斛
rate_粟_to_麥 = Fraction(5, 8)  # 5斗 of 麥 for 8斗 of 粟

# Convert 粟 from 斛 to 斗 (1斛 = 10斗)
粟_in_斗 = 粟 * 10

# Calculate the amount of 麥 obtained
a = 粟_in_斗 * rate_粟_to_麥

# Convert 麥 back to 斛 (1斛 = 10斗)
a = a / 10

# The result is stored in variable 'a'
a  # in 斛


"""


The variable `a` will contain the amount of 麥 (wheat) in 斛.
"""


"""
"""
