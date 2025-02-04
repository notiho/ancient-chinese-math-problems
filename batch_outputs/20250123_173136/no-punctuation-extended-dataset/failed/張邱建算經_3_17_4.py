"""
今有好粟五斗舂之得糳米二斗五升今有御米十斗問得好粟幾何
術曰置糳米數求御米之數為法又置今御米數以本粟乘之為實實如法得一
答曰 a斛
"""

"""
Suppose there are 5 dou of good millet, and after pounding it, 2 dou and 5 sheng of polished millet are obtained.
Now, if there are 10 dou of polished millet, how much good millet is required?

The procedure says: Place the amount of polished millet as the divisor.
Then place the current amount of polished millet and multiply it by the original amount of good millet, making it the dividend.
Divide the dividend by the divisor to obtain the result.

Answer: *a* hu.
"""

from fractions import Fraction

# 好粟五斗
好粟 = 5

# 舂之得糳米二斗五升 (convert to sheng)
糳米 = 2 * 10 + 5  # 1 dou = 10 sheng

# 今有御米十斗 (convert to sheng)
御米 = 10 * 10  # 1 dou = 10 sheng

# 置糳米數求御米之數為法
法 = 糳米

# 又置今御米數以本粟乘之為實
實 = 御米 * 好粟

# 實如法得一
a = Fraction(實, 法) / 10  # Convert back to hu (1 hu = 10 dou)

a
"""
Variable 'a' has wrong value. Expected: 16/7, Actual: 2"""
