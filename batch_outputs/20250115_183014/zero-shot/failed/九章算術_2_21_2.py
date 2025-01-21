"""
今有鑿米三斗、少半升，欲為粟。問︰得幾何？
術曰：以鑿米求粟，二十五之，十三而一。
荅曰：為粟 a斗 。
"""

"""
To solve this problem, we need to convert "鑿米" (hulled rice) into "粟" (unhulled rice). The conversion ratio is given as 25 to 13, meaning 25 units of hulled rice yield 13 units of unhulled rice. The input is "三斗、少半升" (3斗 and 0.5升), and we need to calculate the equivalent amount of unhulled rice in "斗".

Here is the Python code to compute the solution:


"""


from fractions import Fraction

# Input: 3斗 and 0.5升
hulled_rice = Fraction(3) + Fraction(1, 2)  # 3斗 + 0.5升

# Conversion ratio: 25 hulled rice -> 13 unhulled rice
conversion_ratio = Fraction(13, 25)

# Calculate the amount of unhulled rice
a = hulled_rice * conversion_ratio

# Result
a  # The amount of unhulled rice in 斗


"""


The variable `a` will contain the result in terms of "斗".
"""


"""
Variable 'a' has wrong value. Expected: 455/72, Actual: 91/50"""
