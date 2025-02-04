"""
今有好粟五斗舂之得糳米二斗五升今有御米十斗問得好粟幾何
術曰置糳米數求御米之數為法又置今御米數以本粟乘之為實實如法得一
答曰 a斛
"""

#----- content starts here -----
"""
Suppose there are 5 dou of good millet, which when pounded yield 2 dou and 5 sheng of coarse rice.
Now, suppose there are 10 dou of coarse rice.
Question: how much good millet is required?

The procedure says: Place the number of coarse rice [obtained from the good millet] as the divisor.
Then place the current number of coarse rice and multiply it by the original good millet, giving the dividend.
Divide the dividend by the divisor to obtain the result.

Answer: *a* hu.
"""

from fractions import Fraction

# 好粟五斗
好粟 = 5

# 舂之得糳米二斗五升
糳米 = 2 + Fraction(5, 10)  # Convert 5升 to dou (1斗 = 10升)

# 今有御米十斗
御米 = 10

# 置糳米數求御米之數為法
法 = 糳米

# 又置今御米數以本粟乘之為實
實 = 御米 * 好粟

# 實如法得一
a = Fraction(實, 法) / 10  # Convert result from dou to hu (1斛 = 10斗)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 16/7, Actual: 2"""
