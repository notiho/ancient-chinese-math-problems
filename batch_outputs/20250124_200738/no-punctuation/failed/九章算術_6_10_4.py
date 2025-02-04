"""
今有惡粟二十斗舂之得糲米九斗今欲求粺米十斗問惡粟幾何
術曰置糲米九斗以九乘之為法亦置粺米十斗以十乘之又以惡粟二十斗乘之為實實如法得一斗
荅曰 a斗 
"""

#----- content starts here -----
"""
Suppose there are 20 dou of coarse millet. After pounding, 9 dou of roughly husked millet are obtained.
Now, it is desired to obtain 10 dou of finely husked millet.
Question: how much coarse millet is required?

The procedure says: Place the 9 dou of roughly husked millet and multiply it by 9, obtaining the divisor.
Also place the 10 dou of finely husked millet and multiply it by 10.
Then multiply the 20 dou of coarse millet, obtaining the dividend.
Divide the dividend by the divisor, obtaining 1 dou.

Answer: *a* dou of coarse millet.
"""

# 糲米九斗
糲米 = 9

# 惡粟二十斗
惡粟 = 20

# 粺米十斗
粺米 = 10

# 以九乘之，為法
法 = 9 * 糲米

# 以十乘之
實 = 10 * 惡粟

# 實如法得一斗
a = Fraction(實, 法)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2000/81, Actual: 200/81"""
