"""
今有麥八斗六升、七分升之三，欲為小䵂，問︰得幾何？
術曰：以麥求小䵂，三之，十而一。
荅曰：為小䵂 a斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem states that there are 8斗 (dou), 6升 (sheng), and 3/7 of a升. The goal is to compute how many 小䵂 (small units) can be made if 1小䵂 equals 1/10 of 3升.

Here is the Python code:


"""


from fractions import Fraction

# Given quantities
dou = 8  # 斗
sheng = 6  # 升
fraction_sheng = Fraction(3, 7)  # 3/7 升

# Total amount of 麥 in terms of 升
# 1斗 = 10升
total_sheng = dou * 10 + sheng + fraction_sheng

# Conversion rule: 1小䵂 = 1/10 of 3升 = 3/10 升
small_unit_volume = Fraction(3, 10)

# Calculate the number of 小䵂
a = total_sheng / small_unit_volume

# Result
a  # This is the number of 小䵂


"""


The variable `a` will contain the number of 小䵂.
"""


"""
Variable 'a' has wrong value. Expected: 363/140, Actual: 6050/21"""
