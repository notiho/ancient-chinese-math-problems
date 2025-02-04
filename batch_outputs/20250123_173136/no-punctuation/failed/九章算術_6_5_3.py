"""
今有人當稟粟二斛倉無粟欲與米一菽二以當所稟粟問各幾何
術曰置米一菽二求為粟之數并之得三九分之八以為法亦置米一菽二而以粟二斛乘之各自為實實如法得一斛
荅曰米 a斗 菽 b斛 
"""

"""
Suppose there is a person who is supposed to receive 2 hu of millet as rations. However, the granary has no millet, and it is desired to substitute rice and beans in the ratio of 1 rice to 2 beans to fulfill the ration.
Question: how much rice and beans are needed?

The procedure says: Place the ratio of rice to beans as 1 and 2, respectively. Add them, obtaining 3. Divide 8 by 9, using this as the divisor.
Also, place the ratio of rice to beans as 1 and 2, and multiply it by the 2 hu of millet. Each becomes its own dividend.
Divide the dividends by the divisor, obtaining 1 hu.

The answer says: *a* dou of rice, and *b* hu of beans.
"""

# 粟二斛
粟 = 2

# 米一菽二
米率 = 1
菽率 = 2

# 并之得三
總率 = 米率 + 菽率

# 九分之八以為法
法 = Fraction(8, 9)

# 置米一菽二而以粟二斛乘之，各自為實
米實 = 米率 * 粟
菽實 = 菽率 * 粟

# 實如法得
a = 米實 / 法
b = 菽實 / 法
"""
Variable 'a' has wrong value. Expected: 36/7, Actual: 9/4
Variable 'b' has wrong value. Expected: 36/35, Actual: 9/2"""
