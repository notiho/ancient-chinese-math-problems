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

Question: What is the volume?

Answer: 10943 chi 8 cun.

Additionally:
- The standard labor output is 871 chi.
- Subtract 1/5 of the labor for removing soil.
- Subtract half of the labor for gravel, water, and stones.
- The remaining labor is the divisor.
- Use the trench volume as the dividend.
- Divide to determine the number of workers needed.

Answer: *a*(=164157/3484) workers.
"""

from fractions import Fraction

# Dimensions of the trench
上廣 = 1 * 10 + 6 + Fraction(3, 10)  # Convert to chi
下廣 = 1 * 10  # Convert to chi
深 = 6 + Fraction(3, 10)  # Convert to chi
袤 = 13 * 10 + 2 + Fraction(1, 10)  # Convert to chi

# Volume calculation (trapezoidal prism formula)
積 = Fraction(1, 2) * (上廣 + 下廣) * 深 * 袤  # Volume in cubic chi

# Standard labor output
本人功 = 871

# Remove 1/5 of the labor for removing soil
出土功 = Fraction(1, 5) * 本人功

# Remove half of the labor for gravel, water, and stones
沙礫水石功 = Fraction(1, 2) * (本人功 - 出土功)

# Remaining labor is the divisor
法 = 本人功 - 出土功 - 沙礫水石功

# Use the trench volume as the dividend
實 = 積

# Determine the number of workers needed
a = Fraction(實, 法)  # Number of workers#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 164157/3484, Actual: 21887649/696800"""
