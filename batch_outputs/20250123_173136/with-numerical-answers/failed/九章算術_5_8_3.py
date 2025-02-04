"""
今有塹上廣一丈六尺三寸，下廣一丈，深六尺三寸，袤一十三丈二尺一寸。問︰積幾何？
荅曰：一萬九百四十三尺八寸。
夏程人功八百七十一尺。并出土功五分之一，沙礫水石之功作太半，定功二百三十二尺、一十五分尺之四。問︰用徒幾何？
術曰：置本人功，去其出土功五分之一，又去沙礫水石之功太半，餘為法。以塹積尺為實。實如法而一，即用徒人數。
荅曰： a(=164157/3484)人 。
"""

"""
Suppose there is a trench with the following dimensions:
- Top width: 1 zhang 6 chi 3 cun
- Bottom width: 1 zhang
- Depth: 6 chi 3 cun
- Length: 13 zhang 2 chi 1 cun

Question: What is the total volume?

Answer: 10,943 chi 8 cun.

Additionally:
- The standard labor capacity is 871 chi.
- The effort for removing soil is 1/5 of the total.
- The effort for gravel, water, and stones is more than half (3/5) of the total.
- The adjusted labor capacity is 232 chi and 4/15 chi.

Question: How many workers are required?

The procedure says:
- Place the standard labor capacity, subtract 1/5 for removing soil, and subtract 3/5 for gravel, water, and stones. The remainder is the divisor.
- Use the trench volume as the dividend.
- Divide the dividend by the divisor to determine the number of workers.

Answer: *a*(=164157/3484) workers.
"""

from fractions import Fraction

# Dimensions of the trench
上廣 = 1 * 10 + 6 + Fraction(3, 10)  # Convert zhang, chi, cun to chi
下廣 = 1 * 10  # Convert zhang to chi
深 = 6 + Fraction(3, 10)  # Convert chi, cun to chi
袤 = 13 * 10 + 2 + Fraction(1, 10)  # Convert zhang, chi, cun to chi

# Calculate the trench volume
積 = (上廣 + 下廣) * 深 * 袤 / 2  # Trapezoidal prism formula
積 = Fraction(積).limit_denominator()  # Simplify the fraction

# Standard labor capacity
本人功 = 871

# Subtract 1/5 for removing soil
去出土功 = Fraction(1, 5)
本人功 -= 本人功 * 去出土功

# Subtract 3/5 for gravel, water, and stones
去沙礫水石功 = Fraction(3, 5)
本人功 -= 本人功 * 去沙礫水石功

# Adjusted labor capacity is the divisor
法 = 本人功

# Use the trench volume as the dividend
實 = 積

# Divide the volume by the adjusted labor capacity to determine the number of workers
a = Fraction(實, 法).limit_denominator()  # 164157/3484 workers
"""
Variable 'a' has wrong value. Expected: 164157/3484, Actual: 21887649/557440"""
