"""
今有垣高九尺。瓜生其上，蔓日長七寸。瓠生其下，蔓日長一尺。問︰幾何日相逢？瓜、瓠各長幾何？
術曰：假令五日，不足五寸。令之六日，有餘一尺二寸。
荅曰： a日 。瓜長 b尺 ，瓠長 c尺 。
"""

#----- content starts here -----
"""
Suppose there is a wall 9 chi high. A melon vine grows upward from the top of the wall, extending 7 cun per day. A gourd vine grows upward from the bottom of the wall, extending 1 chi per day.
Question: after how many days do they meet? How long are the melon vine and the gourd vine respectively?

The procedure says: Assume 5 days, it is short by 5 cun. Assume 6 days, it exceeds by 1 chi and 2 cun.

Answer: *a* days. The melon vine is *b* chi long, and the gourd vine is *c* chi long.
"""

# 垣高九尺
垣高 = 9

# 瓜蔓日長七寸
瓜日長 = Fraction(7, 10)  # Convert 7 cun to chi (1 chi = 10 cun)

# 瓠蔓日長一尺
瓠日長 = 1

# 假令五日，不足五寸
假日1 = 5
不足 = Fraction(5, 10)  # Convert 5 cun to chi

# 瓜與瓠在5日的總長
總長1 = 瓜日長 * 假日1 + 瓠日長 * 假日1

# 瓜與瓠在5日的差距
差距1 = 總長1 - 垣高

# 差距1應該等於 -不足
assert 差距1 == -不足

# 令之六日，有餘一尺二寸
假日2 = 6
有餘 = 1 + Fraction(2, 10)  # Convert 1 chi 2 cun to chi

# 瓜與瓠在6日的總長
總長2 = 瓜日長 * 假日2 + 瓠日長 * 假日2

# 瓜與瓠在6日的差距
差距2 = 總長2 - 垣高

# 差距2應該等於 有餘
assert 差距2 == 有餘

# 設瓜與瓠相逢的天數為 a 日
# 瓜日長 * a + 瓠日長 * a = 垣高
a = 垣高 / (瓜日長 + 瓠日長)

# 瓜長 b 尺
b = 瓜日長 * a

# 瓠長 c 尺
c = 瓠日長 * a

a日 = a
b尺 = b
c尺 = c#----- content ends here -----

"""
"""
