"""
今有菽二斗欲為豉問得幾何
術曰以菽求豉七之五而一
荅曰為豉 a斗 
"""

#----- content starts here -----
"""
Suppose there are 2 dou of beans (shu). It is desired to turn them into fermented beans (chi).
Question: how much fermented beans does one obtain?

The procedure says: when seeking fermented beans using beans, multiply by 7 and divide by 5.

The answer says: it makes *a* dou of fermented beans.
"""

# 菽二斗
菽 = 2

# 以菽求豉，七之
豉 = 7 * 菽

# 五而一
a = Fraction(豉, 5)#----- content ends here -----

"""
"""
