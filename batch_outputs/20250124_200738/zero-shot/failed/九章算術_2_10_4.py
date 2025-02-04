"""
今有粟三斗少半升，欲為菽。問︰得幾何？
術曰：以粟求菽、答、麻、麥，皆九之，十而一。
荅曰：為菽 a斗 。
"""

"""
To solve this problem, we need to compute the amount of 菽 (a斗) obtained from 粟 (3斗少半升). The rule states that to convert 粟 into 菽, we multiply by 9/10.

### Definitions:
- 1斗 = 10升 (斗 and 升 are units of volume).
- "3斗少半升" means 3斗 minus 0.5升, which is equivalent to \( 3 \times 10 - 0.5 = 29.5 \) 升.

### Conversion:
- Multiply the total volume of 粟 by \( \frac{9}{10} \) to get the equivalent volume of 菽.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# 粟 in 升
粟 = Fraction(3 * 10 - 0.5)  # 3斗少半升 = 29.5升

# Conversion factor from 粟 to 菽
conversion_factor = Fraction(9, 10)

# 菽 in 升
菽 = 粟 * conversion_factor

# Convert 菽 back to 斗 (1斗 = 10升)
a = 菽 / 10

# Result
a  # This is the answer in 斗
#----- content ends here -----


"""


The variable `a` will contain the amount of 菽 in 斗.
"""


"""
Variable 'a' has wrong value. Expected: 273/100, Actual: 531/200"""
