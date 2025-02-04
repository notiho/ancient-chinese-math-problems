"""
今有粟一十斗八升、五分升之二，欲為麥。問︰得幾何？
術曰：以粟求菽、答、麻、麥，皆九之，十而一。
荅曰：為麥 a斗 。
"""

"""
To solve this problem, we need to convert the given amount of 粟 (millet) into 麥 (wheat) using the rule provided: "以粟求菽、答、麻、麥，皆九之，十而一." This means multiplying the amount of 粟 by 9/10 to get the equivalent amount of 麥.

Here is the Python code:


"""


from fractions import Fraction

# Given amount of 粟
粟 = Fraction(10, 1) + Fraction(8, 10) + Fraction(2, 50)  # 10斗8升5分升之2

# Conversion rule: multiply by 9/10
a = 粟 * Fraction(9, 10)

# Result
a  # a斗


"""


The variable `a` will contain the result in terms of "斗".
"""


"""
"""
