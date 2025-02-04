"""
今有隄下廣二丈，上廣八尺，高四尺，袤一十二丈七尺。問︰積幾何？
荅曰：七千一百一十二尺。
冬程人功四百四十四尺。問︰用徒幾何？
術曰：以積尺為實，程功尺數為法，實如法而一，即用徒人數。
荅曰： a(=1778/111)人 。
"""

#----- content starts here -----
"""
Suppose there is a levee with a bottom width of 2 zhang, a top width of 8 chi, a height of 4 chi, and a length of 12 zhang and 7 chi.
Question: what is the volume?

Answer: 7112 cubic chi.

The labor rate is 444 cubic chi per person per day. 
Question: how many workers are needed?

The procedure says: Take the volume in cubic chi as the dividend, and the labor rate in cubic chi as the divisor. 
Divide the dividend by the divisor, obtaining the number of workers.

Answer: *a*(=1778/111) workers.
"""

# 隄下廣二丈
下廣 = 2 * 10  # Convert zhang to chi

# 上廣八尺
上廣 = 8

# 高四尺
高 = 4

# 袤一十二丈七尺
袤 = 12 * 10 + 7  # Convert zhang to chi and add chi

# 計算梯形橫截面積
# 梯形面積公式: (上廣 + 下廣) * 高 / 2
橫截面積 = (上廣 + 下廣) * 高 / 2

# 計算體積
積 = 橫截面積 * 袤  # 體積 = 橫截面積 * 長度

# 冬程人功四百四十四尺
程功 = 444

# 以積尺為實
實 = 積

# 程功尺數為法
法 = 程功

# 實如法而一，即用徒人數
a = Fraction(實, 法)  # 1778/111 workers#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
