"""
今有麥八斗六升、七分升之三，欲為小䵂，問︰得幾何？
術曰：以麥求小䵂，三之，十而一。
荅曰：為小䵂 a斗 。
"""

"""
To solve this problem, we need to calculate the total amount of wheat (given in "斗", "升", and fractions of "升") and then determine how many "小䵂" can be made. The rule provided states that for every 10 parts of wheat, 1 "小䵂" is produced.

Here is the Python code to compute the value of "a":


"""


from fractions import Fraction

# Given values
wheat_dou = 8  # 斗
wheat_sheng = 6  # 升
wheat_fraction_sheng = Fraction(3, 7)  # 3/7 升

# Convert everything to "升" (1 斗 = 10 升)
total_sheng = wheat_dou * 10 + wheat_sheng + wheat_fraction_sheng

# Rule: For every 10 parts of wheat (升), 1 小䵂 is produced
a = total_sheng / 10

# Result
a  # This is the number of 小䵂


"""


The variable `a` will contain the number of "小䵂" that can be made.
"""


"""
Variable 'a' has wrong value. Expected: 363/140, Actual: 121/14"""
