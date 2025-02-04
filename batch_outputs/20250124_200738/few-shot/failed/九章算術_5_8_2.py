"""
今有塹上廣一丈六尺三寸，下廣一丈，深六尺三寸，袤一十三丈二尺一寸。問︰積幾何？
荅曰：一萬九百四十三尺八寸。
夏程人功八百七十一尺。并出土功五分之一，沙礫水石之功作太半，定功二百三十二尺、一十五分尺之四。問︰用徒幾何？
術曰：置本人功，去其出土功五分之一，又去沙礫水石之功太半，餘為法。以塹積尺為實。實如法而一，即用徒人數。
荅曰： a人 。
"""

#----- content starts here -----
"""
Suppose there is a trench with an upper width of 1 zhang 6 chi 3 cun, a lower width of 1 zhang, a depth of 6 chi 3 cun, and a length of 13 zhang 2 chi 1 cun.
Question: what is the volume?

Answer: 10943 chi 8 cun.

The labor capacity of a worker is 871 chi. Including the effort for removing the soil (1/5 of the total), and the effort for dealing with sand, gravel, water, and stones (more than half of the total), the adjusted capacity is 232 chi and 4/15 chi.
Question: how many workers are required?

The procedure says: Place the labor capacity of a worker, subtract the effort for removing soil (1/5 of the total), and subtract the effort for sand, gravel, water, and stones (more than half of the total). The remainder is the divisor.
Take the trench volume in chi as the dividend.
Divide the dividend by the divisor to obtain the number of workers required.

Answer: *a* workers.
"""

# 塹上廣一丈六尺三寸
上廣 = 1 * 10 + 6 + Fraction(3, 10)

# 下廣一丈
下廣 = 1 * 10

# 深六尺三寸
深 = 6 + Fraction(3, 10)

# 袤一十三丈二尺一寸
袤 = 13 * 10 + 2 + Fraction(1, 10)

# 計算塹積
# (上廣 + 下廣) / 2 * 深 * 袤
塹積 = Fraction((上廣 + 下廣), 2) * 深 * 袤

# 夏程人功八百七十一尺
人功 = 871

# 出土功五分之一
出土功 = Fraction(1, 5) * 人功

# 沙礫水石之功作太半
沙礫水石功 = Fraction(1, 2) * 人功 + Fraction(1, 10) * 人功

# 去其出土功五分之一，又去沙礫水石之功太半，餘為法
法 = 人功 - 出土功 - 沙礫水石功

# 以塹積尺為實
實 = 塹積

# 實如法而一，即用徒人數
a = Fraction(實, 法)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 164157/3484, Actual: 21887649/348400"""
