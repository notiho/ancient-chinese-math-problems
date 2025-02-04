"""
今有隄下廣二丈，上廣八尺，高四尺，袤一十二丈七尺。問︰積幾何？
荅曰：七千一百一十二尺。
冬程人功四百四十四尺。問︰用徒幾何？
術曰：以積尺為實，程功尺數為法，實如法而一，即用徒人數。
荅曰： a(=1778/111)人 。
"""

"""
Suppose there is a levee with a bottom width of 2 zhang, a top width of 8 chi, a height of 4 chi, and a length of 12 zhang 7 chi.
Question: what is the volume?

Answer: 7112 cubic chi.

The labor capacity of one person in winter is 444 cubic chi. 
Question: how many workers are required?

The procedure says: Take the volume in cubic chi as the dividend, and the labor capacity in cubic chi as the divisor. 
Divide the dividend by the divisor to obtain the number of workers.

Answer: *a*(=1778/111) workers.
"""

# 隄下廣二丈
隄下廣 = 2 * 10  # Convert zhang to chi

# 上廣八尺
上廣 = 8

# 高四尺
高 = 4

# 袤一十二丈七尺
袤 = 12 * 10 + 7  # Convert zhang and chi to chi

# 積幾何？
# Volume formula for a trapezoidal prism: V = (1/2) * (bottom width + top width) * height * length
積 = Fraction(1, 2) * (隄下廣 + 上廣) * 高 * 袤  # 7112 cubic chi

# 冬程人功四百四十四尺
程功 = 444

# 用徒幾何？
# Divide the volume by the labor capacity
a = Fraction(積, 程功)  # 1778/111 workers
"""
"""
