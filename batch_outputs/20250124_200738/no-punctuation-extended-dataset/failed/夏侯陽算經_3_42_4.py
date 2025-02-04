"""
今有開城濠深二丈闊三丈長一里毎三尺用一功問功幾何
術曰先置深闊相乗又以長里通尺乗之為實以功數方三尺再自乗為法除之即得
答曰 a功
"""

#----- content starts here -----
"""
Suppose there is a moat around a city, with a depth of 2 zhang, a width of 3 zhang, and a length of 1 li.
For every 3 chi of volume, 1 unit of labor is required.
Question: how many units of labor are needed?

The procedure says: First, multiply the depth and the width.
Then, multiply by the length in li converted to chi, obtaining the dividend.
Take the volume corresponding to 1 unit of labor (3 chi cubed), square it, and use it as the divisor.
Divide the dividend by the divisor, obtaining the result.

Answer: *a* units of labor.
"""

# 深二丈
深 = 2 * 10  # Convert zhang to chi (1 zhang = 10 chi)

# 闊三丈
闊 = 3 * 10  # Convert zhang to chi

# 長一里
長 = 1 * 300  # Convert li to chi (1 li = 300 chi)

# 每三尺用一功
功數方 = 3  # 3 chi

# 先置深闊相乘
深闊積 = 深 * 闊

# 又以長里通尺乘之，為實
實 = 深闊積 * 長

# 以功數方三尺再自乘，為法
法 = 功數方**3

# 除之，即得
a = Fraction(實, 法)  # Result in units of labor#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 40000, Actual: 20000/3"""
