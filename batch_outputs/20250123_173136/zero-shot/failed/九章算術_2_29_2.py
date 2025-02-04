"""
今有麥八斗六升、七分升之三，欲為小䵂，問︰得幾何？
術曰：以麥求小䵂，三之，十而一。
荅曰：為小䵂 a斗 。
"""

"""
To solve this problem, we need to compute the value of "a" (the number of small "䵂") based on the given amount of wheat. The problem states that the total amount of wheat is 8斗6升 and 7/3升, and the conversion rule is "三之，十而一" (divide by 3, then divide by 10).

Here is the Python code to compute the value of "a":


"""


from fractions import Fraction

# Total amount of wheat in terms of 斗
total_wheat = 8 + Fraction(6, 10) + Fraction(7, 30)  # 1斗 = 10升, 1升 = 10分升

# Conversion rule: divide by 3, then divide by 10
a = total_wheat / 3 / 10

# Result
a  # Value of "a" in 斗


"""


The variable `a` will contain the number of small "䵂" in terms of 斗.
"""


"""
Variable 'a' has wrong value. Expected: 363/140, Actual: 53/180"""
