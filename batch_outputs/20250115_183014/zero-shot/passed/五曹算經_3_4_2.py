"""
今有粟五百六十斛，凡粟八斗易麥五斗。問：得麥㡬何？
術曰：列粟五百六十斛，以五十乘之得二萬八千斛，以八千除之即得。
答曰： a斛 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given values
粟 = 560  # 粟 in 斛
粟換麥比率_粟 = 8  # 粟換麥比率 (粟 8 斗)
粟換麥比率_麥 = 5  # 粟換麥比率 (麥 5 斗)

# Convert 粟換麥比率 to 斛
粟換麥比率_粟_斛 = Fraction(粟換麥比率_粟, 10)  # 8 斗 = 8/10 斛
粟換麥比率_麥_斛 = Fraction(粟換麥比率_麥, 10)  # 5 斗 = 5/10 斛

# Calculate 麥 obtained
a = Fraction(粟) * 粟換麥比率_麥_斛 / 粟換麥比率_粟_斛

# Result
a  # 麥 in 斛


"""


The variable `a` will contain the amount of 麥 in 斛.
"""


"""
"""
