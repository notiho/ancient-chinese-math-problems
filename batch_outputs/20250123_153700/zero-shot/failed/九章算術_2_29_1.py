"""
今有麥八斗六升、七分升之三，欲為小䵂，問︰得幾何？
術曰：以麥求小䵂，三之，十而一。
荅曰：為小䵂 a斗 。
"""

"""
To solve this problem, we need to compute the value of `a`, which represents the number of "小䵂" (small units). The problem states that the total amount of 麥 (wheat) is 8斗6升 and 7分升之3 (3/7 of a 分升). The conversion rule is given as "三之，十而一," which means that 1小䵂 is equivalent to 3升, and 10小䵂 make up 1斗.

Here is the Python code to compute `a`:


"""


from fractions import Fraction

# Total wheat in terms of 斗, 升, and 分升
total_wheat = 8 + Fraction(6, 10) + Fraction(3, 7 * 10)

# Conversion: 1小䵂 = 3升 = 3/10斗
small_unit_in_dou = Fraction(3, 10)

# Compute the number of 小䵂
a = total_wheat / small_unit_in_dou

# Result
a


"""


The variable `a` will contain the number of 小䵂.
"""


"""
Variable 'a' has wrong value. Expected: 363/140, Actual: 605/21"""
