"""
今有粟五百六十斛，凡粟八斗易麥五斗。問：得麥㡬何？
術曰：列粟五百六十斛，以五十乘之得二萬八千斛，以八千除之即得。
答曰： a斛 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem states that 560斛 (hú) of 粟 (sù, millet) is exchanged at a rate of 8斗 (dǒu) of millet for 5斗 of 麥 (mài, wheat). The goal is to calculate how much wheat (in 斛) is obtained.

Here is the Python code:


"""


from fractions import Fraction

# Given values
millet = 560  # in 斛
millet_per_trade = 8  # in 斗
wheat_per_trade = 5  # in 斗

# Convert millet to wheat
# 1 斛 = 10 斗, so we calculate the total wheat in 斛
a = Fraction(millet * wheat_per_trade, millet_per_trade * 10)

# The result
a  # in 斛


"""


The variable `a` will hold the amount of wheat in 斛.
"""


"""
Variable 'a' has wrong value. Expected: 350, Actual: 35"""
