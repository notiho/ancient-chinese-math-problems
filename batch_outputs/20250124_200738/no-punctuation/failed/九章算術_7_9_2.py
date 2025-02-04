"""
今有垣高九尺瓜生其上蔓日長七寸瓠生其下蔓日長一尺問幾何日相逢瓜瓠各長幾何
術曰假令五日不足五寸令之六日有餘一尺二寸
荅曰 a日 瓜長 b尺 瓠長 c尺 
"""

#----- content starts here -----
"""
Suppose there is a wall 9 chi high. A melon grows on top of it, with its vine extending upward by 7 cun per day.
A gourd grows at the bottom of the wall, with its vine extending upward by 1 chi (10 cun) per day.
Question: after how many days do the vines meet, and how long are the melon and gourd vines at that time?

The procedure says: Suppose 5 days are insufficient by 5 cun. Then, in 6 days, it exceeds by 1 chi 2 cun.

Answer: *a* days, the melon vine is *b* chi long, and the gourd vine is *c* chi long.
"""

# 垣高九尺
垣高 = 9  # in chi

# 瓜蔓日長七寸
瓜日長 = Fraction(7, 10)  # in chi (7 cun = 7/10 chi)

# 瓠蔓日長一尺
瓠日長 = 1  # in chi

# 假令五日不足五寸
假日1 = 5  # days
不足 = Fraction(5, 10)  # in chi (5 cun = 5/10 chi)

# 瓜蔓長 after 假日1
瓜蔓長1 = 瓜日長 * 假日1

# 瓠蔓長 after 假日1
瓠蔓長1 = 瓠日長 * 假日1

# 瓠蔓長1 - 瓜蔓長1
差1 = 瓠蔓長1 - 瓜蔓長1

# 差1 + 不足 = 垣高
if 差1 + 不足 < 垣高:
    # 假令六日有餘一尺二寸
    假日2 = 6  # days
    瓜蔓長2 = 瓜日長 * 假日2
    瓠蔓長2 = 瓠日長 * 假日2
    差2 = 瓠蔓長2 - 瓜蔓長2
    餘 = Fraction(1, 10) * 12  # 1 chi 2 cun = 1.2 chi

    # 差2 - 餘 = 垣高
    if 差2 - 餘 == 垣高:
        a = 假日2
        b = 瓜蔓長2
        c = 瓠蔓長2
else:
    a = 假日1
    b = 瓜蔓長1
    c = 瓠蔓長1#----- content ends here -----

"""
Missing variable in output: 'a'
Missing variable in output: 'b'
Missing variable in output: 'c'"""
