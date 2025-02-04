"""
今有菽一斗，欲為熟菽。問︰得幾何？
術曰：以菽求熟菽，二十三之，十而一。
荅曰：為熟菽 a斗 。
"""

#----- content starts here -----
"""
Suppose there is one dou of beans. It is desired to turn it into cooked beans.
Question: how much does one obtain?

The procedure says: when seeking cooked beans from beans, multiply by 23 and divide by 10.

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
