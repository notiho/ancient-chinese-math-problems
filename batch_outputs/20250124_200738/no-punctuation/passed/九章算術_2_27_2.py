"""
今有菽一斗欲為熟菽問得幾何
術曰以菽求熟菽二十三之十而一
荅曰為熟菽 a斗 
"""

#----- content starts here -----
"""
Suppose there is 1 dou of raw beans. It is desired to turn it into cooked beans.
Question: how much cooked beans does one obtain?

The procedure says: when seeking cooked beans from raw beans, multiply by 23 and divide by 10.

The answer says: it makes *a* dou of cooked beans.
"""

# 菽一斗
菽 = 1

# 以菽求熟菽，二十三之
熟菽 = 23 * 菽

# 十而一
a = Fraction(熟菽, 10)#----- content ends here -----

"""
"""
