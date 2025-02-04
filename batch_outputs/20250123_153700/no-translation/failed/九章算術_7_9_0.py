"""
今有垣高九尺。瓜生其上，蔓日長七寸。瓠生其下，蔓日長一尺。問︰幾何日相逢？瓜、瓠各長幾何？
術曰：假令五日，不足五寸。令之六日，有餘一尺二寸。
荅曰： a日 。瓜長 b尺 ，瓠長 c尺 。
"""

"""

"""


# 垣高九尺
垣高 = 9

# 瓜蔓日長七寸
瓜日長 = Fraction(7, 10)  # 7寸 = 0.7尺

# 瓠蔓日長一尺
瓠日長 = 1

# 假令五日，不足五寸
假日1 = 5
不足 = Fraction(5, 10)  # 5寸 = 0.5尺

# 令之六日，有餘一尺二寸
假日2 = 6
有餘 = 1 + Fraction(2, 10)  # 1尺2寸 = 1.2尺

# 計算每日相差
每日相差 = 瓠日長 - 瓜日長

# 計算相逢日
a = (垣高 + 不足) / 每日相差

# 瓜長
b = 瓜日長 * a

# 瓠長
c = 瓠日長 * a

# 結果
a日 = a
b尺 = b
c尺 = c


"""

"""


"""
Variable 'a' has wrong value. Expected: 90/17, Actual: 95/3
Variable 'b' has wrong value. Expected: 63/17, Actual: 133/6
Variable 'c' has wrong value. Expected: 90/17, Actual: 95/3"""
