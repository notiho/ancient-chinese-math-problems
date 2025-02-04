"""
今有婦人河上蕩桮，津吏問曰：「桮何以多？」婦人曰：「家有客。」津吏曰：「客幾何？」婦人曰：「二人共飯，三人共羹，四人共肉，凡用桮六十五，不知客幾何？」
術曰：置六十五桮，以十二乘之，得七百八十；以十三除之，即得。
答曰：「 a人 。」
"""

"""
To solve this problem, we translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given total cups
total_cups = 65

# Multiply by 12
multiplied = total_cups * 12

# Divide by 13
a = Fraction(multiplied, 13)

# The number of guests
a


"""


The variable `a` will hold the number of guests.
"""


"""
"""
