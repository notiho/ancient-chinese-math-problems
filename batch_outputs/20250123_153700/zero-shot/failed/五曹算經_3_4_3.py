"""
今有粟五百六十斛，凡粟八斗易麥五斗。問：得麥㡬何？
術曰：列粟五百六十斛，以五十乘之得二萬八千斛，以八千除之即得。
答曰： a斛 。
"""

"""
To solve this problem, we need to calculate how much wheat (in "斛") can be obtained by exchanging 560斛 of millet, given that 8斗 of millet can be exchanged for 5斗 of wheat. Here's the Python code:


"""


from fractions import Fraction

# Given values
millet = 560  # in 斛
millet_per_exchange = 8  # in 斗
wheat_per_exchange = 5  # in 斗

# Convert millet to 斗 (1 斛 = 10 斗)
millet_in_dou = millet * 10

# Calculate the amount of wheat obtained
a = Fraction(millet_in_dou * wheat_per_exchange, millet_per_exchange)

# Result
a  # in 斗


"""


The variable `a` will contain the amount of wheat in 斗.
"""


"""
Variable 'a' has wrong value. Expected: 350, Actual: 3500"""
