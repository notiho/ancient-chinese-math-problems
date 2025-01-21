"""
今有築城髙三丈上闊一丈五尺下闊二丈五尺長一百丈毎方二尺用一功問功幾何
術曰先置上下闊并之折半以髙乗之又以長乗之為
答曰 a功
"""

"""
Suppose there is a city wall being built. The height is 3 zhang, the top width is 1 zhang 5 chi, the bottom width is 2 zhang 5 chi, and the length is 100 zhang. For every 2 cubic chi, 1 unit of labor is required.
Question: how many units of labor are needed?

The procedure says: First, place the top and bottom widths, add them together, and halve the result. Multiply this by the height, then multiply it by the length. This gives the total volume. Divide the volume by 2 to find the required labor.

Answer: *a* units of labor.
"""

# 髙三丈
髙 = 3

# 上闊一丈五尺 (convert to chi: 1 zhang = 10 chi)
上闊 = 10 + 5

# 下闊二丈五尺 (convert to chi: 1 zhang = 10 chi)
下闊 = 20 + 5

# 長一百丈 (convert to chi: 1 zhang = 10 chi)
長 = 100 * 10

# 每方二尺用一功
每功體積 = 2

# 先置上下闊并之
上下闊和 = 上闊 + 下闊

# 折半
平均闊 = Fraction(上下闊和, 2)

# 以髙乘之
體積_截面 = 平均闊 * 髙

# 又以長乘之
總體積 = 體積_截面 * 長

# 每方二尺用一功，計算功數
a = Fraction(總體積, 每功體積)
"""
Variable 'a' has wrong value. Expected: 75000, Actual: 30000"""
