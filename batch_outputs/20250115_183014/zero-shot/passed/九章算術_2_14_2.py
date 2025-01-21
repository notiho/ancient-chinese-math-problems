"""
今有粟七斗五升、七分升之四，欲為稻。問︰得幾何？
術曰：以粟求稻，六之，五而一。
荅曰：為稻 a斗 。
"""

"""
To solve this problem, we need to compute the amount of rice ("稻") obtained from the given amount of millet ("粟"). The conversion rule is: multiply the amount of millet by 6, then divide by 5.

Here is the Python code to compute the value of "a" (in "斗"):


"""


from fractions import Fraction

# Given amount of millet in "斗", "升", and "分升"
millet = Fraction(7) + Fraction(5, 10) + Fraction(4, 70)  # 7斗5升4/7升

# Conversion rule: multiply by 6, then divide by 5
a = millet * Fraction(6, 5)

# Result
a  # in "斗"


"""


The variable `a` will contain the result in "斗".
"""


"""
"""
