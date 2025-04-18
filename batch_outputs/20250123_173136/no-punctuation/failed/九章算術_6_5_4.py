"""
今有人當稟粟二斛倉無粟欲與米一菽二以當所稟粟問各幾何
術曰置米一菽二求為粟之數并之得三九分之八以為法亦置米一菽二而以粟二斛乘之各自為實實如法得一斛
荅曰米 a斗 菽 b斛 
"""

"""
Suppose there is a person who is supposed to receive 2 hu of millet as rations.
The granary has no millet, so it is desired to substitute rice and beans in the ratio of 1:2 (1 part rice, 2 parts beans) to fulfill the rations.
Question: how much rice and beans are needed?

The procedure says: Place the ratio of rice to beans as 1:2. Add them together, obtaining 3, and take 8/9 as the divisor.
Also, place the ratio of rice to beans as 1:2, and multiply it by the 2 hu of millet. Each becomes its own dividend.
Divide by the divisor to obtain the quantities.

The answer says: *a* dou of rice, and *b* hu of beans.
"""

# 當稟粟二斛
粟 = 2

# 米一菽二
米率 = 1
菽率 = 2

# 并之得三
總率 = 米率 + 菽率

# 九分之八以為法
法 = Fraction(8, 9)

# 置米一菽二而以粟二斛乘之
米實 = 米率 * 粟
菽實 = 菽率 * 粟

# 各自為實，實如法得一斛
a = Fraction(米實, 總率) * 法
b = Fraction(菽實, 總率) * 法
"""
Variable 'a' has wrong value. Expected: 36/7, Actual: 16/27
Variable 'b' has wrong value. Expected: 36/35, Actual: 32/27"""
