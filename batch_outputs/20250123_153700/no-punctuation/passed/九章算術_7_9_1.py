"""
今有垣高九尺瓜生其上蔓日長七寸瓠生其下蔓日長一尺問幾何日相逢瓜瓠各長幾何
術曰假令五日不足五寸令之六日有餘一尺二寸
荅曰 a日 瓜長 b尺 瓠長 c尺 
"""

"""
Suppose there is a wall 9 chi high. A melon vine grows upward from the top of the wall, extending 7 cun per day.
A bottle gourd vine grows downward from the top of the wall, extending 1 chi per day.
Question: after how many days do the two vines meet, and how long are the melon and bottle gourd vines at that time?

The procedure says: Suppose 5 days are insufficient by 5 cun. Then suppose 6 days exceed by 1 chi and 2 cun.

Answer: *a* days, the melon vine is *b* chi long, and the bottle gourd vine is *c* chi long.
"""

# 垣高九尺
垣高 = 9  # chi

# 瓜蔓日長七寸
瓜日長 = Fraction(7, 10)  # chi per day (7 cun = 7/10 chi)

# 瓠蔓日長一尺
瓠日長 = 1  # chi per day

# 假令五日不足五寸
假日1 = 5  # days
不足 = Fraction(5, 10)  # chi (5 cun = 5/10 chi)

# 瓜長 after 假日1
瓜長1 = 瓜日長 * 假日1

# 瓠長 after 假日1
瓠長1 = 瓠日長 * 假日1

# Total distance between the two vines after 假日1
距離1 = 瓠長1 + 瓜長1 - 垣高

# 確認不足
assert 距離1 == -不足  # Should match the "不足" condition

# 假令六日有餘一尺二寸
假日2 = 6  # days
有餘 = 1 + Fraction(2, 10)  # chi (1 chi 2 cun = 1 + 2/10 chi)

# 瓜長 after 假日2
瓜長2 = 瓜日長 * 假日2

# 瓠長 after 假日2
瓠長2 = 瓠日長 * 假日2

# Total distance between the two vines after 假日2
距離2 = 瓠長2 + 瓜長2 - 垣高

# 確認有餘
assert 距離2 == 有餘  # Should match the "有餘" condition

# Solve for the exact meeting day using linear interpolation
a = 假日1 + (假日2 - 假日1) * (不足 / (不足 + 有餘))

# 瓜長 at meeting day
b = 瓜日長 * a

# 瓠長 at meeting day
c = 瓠日長 * a

a日 = a
b尺 = b
c尺 = c
"""
"""
