"""
今有開城濠深二丈闊三丈長一里毎三尺用一功問功幾何
術曰先置深闊相乗又以長里通尺乗之為實以功數方三尺再自乗為法除之即得
答曰 a功
"""

"""
Suppose there is a city moat to be dug, with a depth of 2 zhang, a width of 3 zhang, and a length of 1 li.
For every 3 chi, 1 unit of labor (gong) is required.
Question: how many units of labor are needed?

The procedure says: First, multiply the depth and the width together.
Then, multiply it by the length converted from li to chi, obtaining the dividend.
Take the unit of labor (3 chi) squared, and square it again, obtaining the divisor.
Divide the dividend by the divisor, and the result is the number of labor units.

Answer: *a* units of labor.
"""

# 深二丈
深 = 2 * 10  # Convert zhang to chi (1 zhang = 10 chi)

# 闊三丈
闊 = 3 * 10  # Convert zhang to chi (1 zhang = 10 chi)

# 長一里
長 = 1 * 300  # Convert li to chi (1 li = 300 chi)

# 每三尺用一功
功數 = 3

# 先置深闊相乘
深闊積 = 深 * 闊

# 又以長里通尺乘之，為實
實 = 深闊積 * 長

# 以功數方三尺再自乘，為法
法 = (功數 ** 2) ** 2

# 除之，即得
a = Fraction(實, 法)
"""
Variable 'a' has wrong value. Expected: 40000, Actual: 20000/9"""
