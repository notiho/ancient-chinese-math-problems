"""
今有婦人河上蕩桮，津吏問曰：「桮何以多？」婦人曰：「家有客。」津吏曰：「客幾何？」婦人曰：「二人共飯，三人共羹，四人共肉，凡用桮六十五，不知客幾何？」
術曰：置六十五桮，以十二乘之，得七百八十；以十三除之，即得。
答曰：「 a人 。」
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves determining the number of guests ("a") based on the given conditions.

Here is the Python code:


"""


from fractions import Fraction

# Total number of cups
total_cups = 65

# Multiply by 12
step1 = total_cups * 12

# Divide by 13
a = Fraction(step1, 13)

# The number of guests
a


"""


The solution is stored in the variable `a`, which represents the number of guests.
"""


"""
"""
