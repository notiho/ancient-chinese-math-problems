"""
今有粟七斗五升、七分升之四，欲為稻。問︰得幾何？
術曰：以粟求稻，六之，五而一。
荅曰：為稻 a斗 。
"""

#----- content starts here -----
"""
Suppose there is 7 dou, 5 sheng, and 4/7 of a sheng of millet. It is desired to convert it into rice.
Question: how much rice is obtained?

The procedure says: When seeking rice from millet, multiply by 6 and divide by 5.

Answer: it makes *a* dou of rice.
"""

from fractions import Fraction

# 粟七斗五升、七分升之四
粟 = 7 + Fraction(5, 10) + Fraction(4, 70)  # Convert everything to dou (1 dou = 10 sheng)

# 以粟求稻，六之
稻 = 6 * 粟

# 五而一
a = Fraction(稻, 5)

# Convert result back to dou and sheng for clarity
dou = int(a)  # Whole dou
sheng = (a - dou) * 10  # Remaining sheng

# Final result
a斗 = f"{dou}斗 {sheng}升"
a斗#----- content ends here -----

"""
"""
