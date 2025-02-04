"""
今有垣高九尺瓜生其上蔓日長七寸瓠生其下蔓日長一尺問幾何日相逢瓜瓠各長幾何
術曰假令五日不足五寸令之六日有餘一尺二寸
荅曰 a日 瓜長 b尺 瓠長 c尺 
"""

#----- content starts here -----
"""
Suppose there is a wall 9 chi high. A melon grows on top of the wall, and its vine grows upward at a rate of 7 cun per day.
A gourd grows at the bottom of the wall, and its vine grows upward at a rate of 1 chi (10 cun) per day.
Question: after how many days will the two vines meet, and how long will the melon and gourd vines be at that time?

The procedure says: Suppose 5 days are insufficient by 5 cun. Then, suppose 6 days exceed by 1 chi and 2 cun.

Answer: *a* days, the melon vine is *b* chi long, and the gourd vine is *c* chi long.
"""

# 垣高九尺
垣高 = 9  # chi

# 瓜蔓日長七寸
瓜蔓日長 = 7  # cun/day

# 瓠蔓日長一尺
瓠蔓日長 = 10  # cun/day (1 chi = 10 cun)

# 假令五日不足五寸
假日1 = 5  # days
不足 = 5  # cun

# 瓜蔓長 after 假日1
瓜蔓長1 = 瓜蔓日長 * 假日1  # cun

# 瓠蔓長 after 假日1
瓠蔓長1 = 瓠蔓日長 * 假日1  # cun

# Relative position after 假日1
相對位置1 = 瓠蔓長1 - 瓜蔓長1  # cun
# 相對位置1 should be less than 垣高 by 不足
assert 相對位置1 + 不足 == 垣高 * 10  # convert 垣高 to cun

# 假令六日有餘一尺二寸
假日2 = 6  # days
有餘 = 12  # cun (1 chi = 10 cun + 2 cun)

# 瓜蔓長 after 假日2
瓜蔓長2 = 瓜蔓日長 * 假日2  # cun

# 瓠蔓長 after 假日2
瓠蔓長2 = 瓠蔓日長 * 假日2  # cun

# Relative position after 假日2
相對位置2 = 瓠蔓長2 - 瓜蔓長2  # cun
# 相對位置2 should exceed 垣高 by 有餘
assert 相對位置2 - 有餘 == 垣高 * 10  # convert 垣高 to cun

# Solve for the exact number of days (a)
a = Fraction(垣高 * 10, 瓠蔓日長 - 瓜蔓日長)  # days

# 瓜長 (b) and 瓠長 (c) at that time
瓜長 = Fraction(瓜蔓日長 * a, 10)  # convert to chi
瓠長 = Fraction(瓠蔓日長 * a, 10)  # convert to chi

b = 瓜長
c = 瓠長#----- content ends here -----

"""
Code error: """
