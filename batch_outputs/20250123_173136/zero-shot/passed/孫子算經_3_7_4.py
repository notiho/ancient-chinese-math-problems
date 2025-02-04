"""
今有絹，七萬八千七百三十二匹，令一百六十二人分之。問：人得幾何？
術曰：置絹七萬八千七百三十二匹為實，以一百六十二人為法。實如法，即得。
答曰： a匹 。
"""

"""
To solve the problem, we divide the total number of silk pieces (絹) by the number of people (人). Here's the Python code:


"""


from fractions import Fraction

# Given data
絹 = 78732  # Total silk pieces
人 = 162    # Number of people

# Calculation
a = Fraction(絹, 人)  # Silk pieces per person

# Result
a  # Answer in terms of Fraction


"""


The variable `a` will hold the result in terms of silk pieces per person.
"""


"""
"""
