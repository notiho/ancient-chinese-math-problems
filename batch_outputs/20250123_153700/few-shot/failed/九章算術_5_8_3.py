"""
今有塹上廣一丈六尺三寸，下廣一丈，深六尺三寸，袤一十三丈二尺一寸。問︰積幾何？
荅曰：一萬九百四十三尺八寸。
夏程人功八百七十一尺。并出土功五分之一，沙礫水石之功作太半，定功二百三十二尺、一十五分尺之四。問︰用徒幾何？
術曰：置本人功，去其出土功五分之一，又去沙礫水石之功太半，餘為法。以塹積尺為實。實如法而一，即用徒人數。
荅曰： a人 。
"""

"""
Suppose there is a trench with the following dimensions:
- Top width: 1 zhang 6 chi 3 cun
- Bottom width: 1 zhang
- Depth: 6 chi 3 cun
- Length: 13 zhang 2 chi 1 cun

Question: What is the volume of the trench?

Answer: 10,943 chi 8 cun.

The labor calculation is as follows:
- A single worker's capacity is 871 chi.
- Subtract 1/5 of the capacity for the effort of removing the soil.
- Subtract half of the remaining capacity for dealing with sand, gravel, water, and stones.
- The remainder is the effective capacity.

Question: How many workers are required?

The procedure says:
- Place the capacity of one worker, subtract 1/5 for the soil removal effort, and subtract half for the sand, gravel, water, and stones. The remainder is the divisor.
- Take the trench volume in chi as the dividend.
- Divide the dividend by the divisor to determine the number of workers required.

Answer: *a* workers.
"""

from fractions import Fraction

# Dimensions of the trench
上廣 = 1 * 10 + 6 + Fraction(3, 10)  # Convert zhang, chi, cun to chi
下廣 = 1 * 10  # Convert zhang to chi
深 = 6 + Fraction(3, 10)  # Convert chi, cun to chi
袤 = 13 * 10 + 2 + Fraction(1, 10)  # Convert zhang, chi, cun to chi

# Volume calculation
積 = (上廣 + 下廣) * 深 * 袤 / 2  # Trapezoidal prism formula

# Single worker's capacity
本人功 = 871

# Subtract 1/5 for soil removal
出土功 = Fraction(1, 5) * 本人功
餘功 = 本人功 - 出土功

# Subtract half for sand, gravel, water, and stones
沙礫功 = Fraction(1, 2) * 餘功
有效功 = 餘功 - 沙礫功

# Calculate the number of workers required
a = Fraction(積, 有效功)

# Results
積_result = 積  # Volume of the trench
a_result = a  # Number of workers required
"""
Variable 'a' has wrong value. Expected: 164157/3484, Actual: 21887649/696800"""
