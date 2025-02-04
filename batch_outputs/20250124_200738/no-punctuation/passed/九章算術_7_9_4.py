"""
今有垣高九尺瓜生其上蔓日長七寸瓠生其下蔓日長一尺問幾何日相逢瓜瓠各長幾何
術曰假令五日不足五寸令之六日有餘一尺二寸
荅曰 a日 瓜長 b尺 瓠長 c尺 
"""

#----- content starts here -----
"""
Suppose there is a wall 9 chi high. A melon grows on top of the wall, and its vine grows upward at a rate of 7 cun per day.
A bottle gourd grows at the bottom of the wall, and its vine grows downward at a rate of 1 chi per day.
Question: after how many days do the vines meet, and how long are the melon and bottle gourd vines?

The procedure says: Suppose 5 days are insufficient by 5 cun, and 6 days exceed by 1 chi and 2 cun.

Answer: *a* days, the melon vine is *b* chi long, and the bottle gourd vine is *c* chi long.
"""

# 垣高九尺
垣高 = 9  # chi

# 瓜蔓日長七寸
瓜日長 = Fraction(7, 10)  # chi per day (convert 7 cun to chi)

# 瓠蔓日長一尺
瓠日長 = 1  # chi per day

# 假令五日不足五寸
日數_1 = 5  # days
不足 = Fraction(5, 10)  # chi (convert 5 cun to chi)

# 瓜蔓長 after 5 days
瓜長_1 = 瓜日長 * 日數_1

# 瓠蔓長 after 5 days
瓠長_1 = 瓠日長 * 日數_1

# Total distance covered by both vines after 5 days
總長_1 = 瓜長_1 + 瓠長_1

# 假令六日有餘一尺二寸
日數_2 = 6  # days
有餘 = 1 + Fraction(2, 10)  # chi (convert 1 chi 2 cun to chi)

# 瓜蔓長 after 6 days
瓜長_2 = 瓜日長 * 日數_2

# 瓠蔓長 after 6 days
瓠長_2 = 瓠日長 * 日數_2

# Total distance covered by both vines after 6 days
總長_2 = 瓜長_2 + 瓠長_2

# Solve for the exact day when the vines meet
# Let x be the number of days
# 瓜日長 * x + 瓠日長 * x = 垣高
x = Fraction(垣高, 瓜日長 + 瓠日長)

# 瓜長 after x days
b = 瓜日長 * x

# 瓠長 after x days
c = 瓠日長 * x

# Number of days
a = x#----- content ends here -----

"""
"""
