"""
今有垣高九尺瓜生其上蔓日長七寸瓠生其下蔓日長一尺問幾何日相逢瓜瓠各長幾何
術曰假令五日不足五寸令之六日有餘一尺二寸
荅曰 a日 瓜長 b尺 瓠長 c尺 
"""

#----- content starts here -----
"""
Suppose there is a wall 9 chi high. A melon grows on top of the wall, and its vine grows upward at a rate of 7 cun per day.
A gourd grows at the bottom of the wall, and its vine grows upward at a rate of 1 chi per day.
Question: after how many days do the melon and gourd vines meet, and how long are the vines of the melon and gourd at that time?

The procedure says: Suppose 5 days are insufficient by 5 cun. Then, suppose 6 days exceed by 1 chi and 2 cun.

Answer: *a* days, the melon vine is *b* chi long, and the gourd vine is *c* chi long.
"""

# 垣高九尺
垣高 = 9  # chi

# 瓜蔓日長七寸
瓜蔓日長 = Fraction(7, 10)  # chi per day (7 cun = 7/10 chi)

# 瓠蔓日長一尺
瓠蔓日長 = 1  # chi per day

# 假令五日不足五寸
假日1 = 5  # days
不足 = Fraction(5, 10)  # chi (5 cun = 5/10 chi)

# 瓜蔓長度 after 假日1
瓜長1 = 瓜蔓日長 * 假日1

# 瓠蔓長度 after 假日1
瓠長1 = 瓠蔓日長 * 假日1

# 瓠蔓長度 + 垣高 - 瓜蔓長度
相差1 = 瓠長1 + 垣高 - 瓜長1

# 相差1 should equal 不足
assert 相差1 == 不足

# 假令六日有餘一尺二寸
假日2 = 6  # days
有餘 = 1 + Fraction(2, 10)  # chi (1 chi 2 cun = 1 + 2/10 chi)

# 瓜蔓長度 after 假日2
瓜長2 = 瓜蔓日長 * 假日2

# 瓠蔓長度 after 假日2
瓠長2 = 瓠蔓日長 * 假日2

# 瓠蔓長度 + 垣高 - 瓜蔓長度
相差2 = 瓠長2 + 垣高 - 瓜長2

# 相差2 should equal 有餘
assert 相差2 == 有餘

# Solve for the exact meeting day
# Let x be the number of days when the vines meet
# 瓠蔓長度 + 垣高 = 瓜蔓長度
# 瓠蔓日長 * x + 垣高 = 瓜蔓日長 * x
# (瓠蔓日長 - 瓜蔓日長) * x = 垣高
x = 垣高 / (瓠蔓日長 - 瓜蔓日長)

# 瓜長 = 瓜蔓日長 * x
瓜長 = 瓜蔓日長 * x

# 瓠長 = 瓠蔓日長 * x
瓠長 = 瓠蔓日長 * x

a = x
b = 瓜長
c = 瓠長#----- content ends here -----

"""
Code error: """
