"""
今有惡粟二十斗舂之得糲米九斗今欲求粺米十斗問惡粟幾何
術曰置糲米九斗以九乘之為法亦置粺米十斗以十乘之又以惡粟二十斗乘之為實實如法得一斗
荅曰 a斗 
"""

"""
Suppose there are 20 dou of coarse millet. After pounding, 9 dou of roughly husked millet is obtained.
Now, it is desired to obtain 10 dou of finely husked millet.
Question: how much coarse millet is required?

The procedure says: Place 9 dou of roughly husked millet. Multiply it by 9 to obtain the divisor.
Also, place 10 dou of finely husked millet. Multiply it by 10.
Then, multiply 20 dou of coarse millet to obtain the dividend.
Divide the dividend by the divisor to obtain the number of dou.

The answer says: *a* dou.
"""

# 惡粟二十斗
惡粟 = 20

# 舂之得糲米九斗
糲米 = 9

# 欲求粺米十斗
粺米 = 10

# 置糲米九斗，以九乘之，為法
法 = 9 * 糲米

# 置粺米十斗，以十乘之
實 = 10 * 惡粟

# 實如法得一斗
a = Fraction(實, 法)
"""
Variable 'a' has wrong value. Expected: 2000/81, Actual: 200/81"""
