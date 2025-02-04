"""
今有塹上廣一丈六尺三寸，下廣一丈，深六尺三寸，袤一十三丈二尺一寸。問︰積幾何？
荅曰：一萬九百四十三尺八寸。
夏程人功八百七十一尺。并出土功五分之一，沙礫水石之功作太半，定功二百三十二尺、一十五分尺之四。問︰用徒幾何？
術曰：置本人功，去其出土功五分之一，又去沙礫水石之功太半，餘為法。以塹積尺為實。實如法而一，即用徒人數。
荅曰： a(=164157/3484)人 。
"""

#----- content starts here -----
"""
Suppose there is a trench with the following dimensions:
- Top width: 1 zhang 6 chi 3 cun
- Bottom width: 1 zhang
- Depth: 6 chi 3 cun
- Length: 13 zhang 2 chi 1 cun

Question: What is the volume of the trench?

Answer: 10943 chi 8 cun.

Additionally, the labor calculation is as follows:
- A single worker's capacity is 871 chi.
- Subtract 1/5 for the effort of removing the soil.
- Subtract half for the effort of dealing with sand, gravel, water, and stones.
- The remainder is the effective capacity of a worker.
- Divide the trench volume by the effective capacity to determine the number of workers required.

Answer: *a*(=164157/3484) workers.
"""

from fractions import Fraction

# Dimensions of the trench
上廣 = 1 * 10 + 6 + Fraction(3, 10)  # 1丈6尺3寸 = 16.3尺
下廣 = 1 * 10  # 1丈 = 10尺
深 = 6 + Fraction(3, 10)  # 6尺3寸 = 6.3尺
袤 = 13 * 10 + 2 + Fraction(1, 10)  # 13丈2尺1寸 = 132.1尺

# Trapezoidal cross-section area calculation
# (上廣 + 下廣) * 深 / 2
橫截面積 = (上廣 + 下廣) * 深 / 2

# Volume of the trench
# 橫截面積 * 袤
塹積 = 橫截面積 * 袤  # Volume in cubic chi

# Single worker's capacity
本人功 = 871

# Subtract 1/5 for removing soil
出土功 = Fraction(1, 5) * 本人功

# Subtract half for sand, gravel, water, and stones
沙礫水石功 = Fraction(1, 2) * (本人功 - 出土功)

# Effective capacity of a worker
法 = 本人功 - 出土功 - 沙礫水石功

# Number of workers required
實 = 塹積
a = Fraction(實, 法)  # Number of workers required#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 164157/3484, Actual: 21887649/696800"""
