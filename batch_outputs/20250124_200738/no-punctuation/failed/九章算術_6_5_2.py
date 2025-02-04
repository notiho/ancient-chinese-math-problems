"""
今有人當稟粟二斛倉無粟欲與米一菽二以當所稟粟問各幾何
術曰置米一菽二求為粟之數并之得三九分之八以為法亦置米一菽二而以粟二斛乘之各自為實實如法得一斛
荅曰米 a斗 菽 b斛 
"""

#----- content starts here -----
"""
Suppose there is a person who is supposed to receive 2 hu of millet. However, the granary has no millet and instead wants to give rice and beans in the ratio of 1:2 to substitute for the millet.
Question: how much rice and beans should be given?

The procedure says: Place rice as 1 and beans as 2, and seek the equivalent amount of millet. Add them, obtaining 3. Take 8/9 as the divisor.
Also place rice as 1 and beans as 2, and multiply by the 2 hu of millet. Each becomes its own dividend.
Divide by the divisor, obtaining 1 hu.

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

# 置米一菽二而以粟二斛乘之
米實 = 米率 * 粟
菽實 = 菽率 * 粟

# 各自為實，實如法得
a = Fraction(米實, 總率) / 法  # 米的量，轉換為斗
b = Fraction(菽實, 總率) / 法  # 菽的量，轉換為斛#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 36/7, Actual: 3/4
Variable 'b' has wrong value. Expected: 36/35, Actual: 3/2"""
