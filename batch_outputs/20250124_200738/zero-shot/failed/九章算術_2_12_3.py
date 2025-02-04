"""
今有粟五斗、太半升，欲為麻。問︰得幾何？
術曰：以粟求菽、答、麻、麥，皆九之，十而一。
荅曰：為麻 a斗 。
"""

"""
To solve this problem, we need to translate the ancient Chinese math problem into Python code. The problem states that we have 5斗 (dou) and 太半升 (which means 0.5升 or 0.5 sheng). The conversion rule is that to calculate 麻 (ma), we multiply the total amount of 粟 (su) by 9/10.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
dou = 5  # 斗
sheng = Fraction(1, 2)  # 太半升 = 0.5 升

# Convert everything to 斗 (1 斗 = 10 升)
total_su = dou + sheng / 10  # Convert 升 to 斗

# Rule: Multiply by 9/10 to get 麻
a = total_su * Fraction(9, 10)

# The result is stored in variable 'a'
a
#----- content ends here -----


"""


The variable `a` will contain the amount of 麻 in 斗.
"""


"""
Variable 'a' has wrong value. Expected: 114/25, Actual: 909/200"""
