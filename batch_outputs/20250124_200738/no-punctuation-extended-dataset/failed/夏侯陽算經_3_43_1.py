"""
今有築城髙三丈上闊一丈五尺下闊二丈五尺長一百丈毎方二尺用一功問功幾何
術曰先置上下闊并之折半以髙乗之又以長乗之為
答曰 a功
"""

#----- content starts here -----
"""
Suppose there is a city wall being built. Its height is 3 zhang, the top width is 1 zhang and 5 chi, the bottom width is 2 zhang and 5 chi, and its length is 100 zhang. 
For every 2 cubic chi, 1 unit of labor is required.
Question: how many units of labor are needed?

The procedure says: First, place the top and bottom widths, add them together, and take half of the sum. 
Multiply this by the height, and then multiply it by the length. 
Finally, divide by 2 cubic chi per unit of labor to find the total labor required.

Answer: *a* units of labor.
"""

# 髙三丈
髙 = 3  # in zhang

# 上闊一丈五尺
上闊 = 1 + Fraction(5, 10)  # convert 5 chi to zhang (10 chi = 1 zhang)

# 下闊二丈五尺
下闊 = 2 + Fraction(5, 10)  # convert 5 chi to zhang

# 長一百丈
長 = 100  # in zhang

# 每方二尺用一功
每功體積 = Fraction(2, 10 * 10 * 10)  # 2 cubic chi converted to cubic zhang (1 zhang³ = 1000 chi³)

# 置上下闊并之
上下闊和 = 上闊 + 下闊

# 折半
平均闊 = Fraction(上下闊和, 2)

# 以髙乘之
體積 = 平均闊 * 髙

# 又以長乘之
總體積 = 體積 * 長

# 每方二尺用一功，計算功數
a = 總體積 / 每功體積#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 75000, Actual: 300000"""
