"""
今有塹上廣一丈六尺三寸，下廣一丈，深六尺三寸，袤一十三丈二尺一寸。問︰積幾何？
荅曰：一萬九百四十三尺八寸。
夏程人功八百七十一尺。并出土功五分之一，沙礫水石之功作太半，定功二百三十二尺、一十五分尺之四。問︰用徒幾何？
術曰：置本人功，去其出土功五分之一，又去沙礫水石之功太半，餘為法。以塹積尺為實。實如法而一，即用徒人數。
荅曰： a(=164157/3484)人 。
"""

#----- content starts here -----
"""
Suppose there is a trench with an upper width of 1 zhang 6 chi 3 cun, a lower width of 1 zhang, a depth of 6 chi 3 cun, and a length of 13 zhang 2 chi 1 cun.
Question: what is the volume?

Answer: 10943 chi 8 cun.

The procedure for determining the number of workers says: Place the standard work rate of a person, subtract the work for removing soil (1/5), and subtract the work for gravel, water, and stones (1/2). The remainder is the divisor.
Take the trench volume in chi as the dividend. Divide the dividend by the divisor to determine the number of workers.

Answer: *a*(=164157/3484) workers.
"""

# Dimensions of the trench
上廣 = 1 * 10 + 6 + Fraction(3, 10)  # Convert to chi
下廣 = 1 * 10  # Convert to chi
深 = 6 + Fraction(3, 10)  # Convert to chi
袤 = 13 * 10 + 2 + Fraction(1, 10)  # Convert to chi

# Calculate the volume of the trench
積 = Fraction((上廣 + 下廣), 2) * 深 * 袤  # Trapezoidal prism formula

# Standard work rate of a person
本人功 = 871

# Subtract the work for removing soil (1/5)
出土功 = Fraction(1, 5) * 本人功

# Subtract the work for gravel, water, and stones (1/2)
沙礫水石功 = Fraction(1, 2) * (本人功 - 出土功)

# Remaining work rate (divisor)
法 = 本人功 - 出土功 - 沙礫水石功

# Use the trench volume as the dividend
實 = 積

# Determine the number of workers
a = Fraction(實, 法)  # 164157/3484 workers#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 164157/3484, Actual: 21887649/696800"""
