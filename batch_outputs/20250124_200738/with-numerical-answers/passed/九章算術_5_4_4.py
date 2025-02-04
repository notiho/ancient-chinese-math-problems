"""
今有隄下廣二丈，上廣八尺，高四尺，袤一十二丈七尺。問︰積幾何？
荅曰：七千一百一十二尺。
冬程人功四百四十四尺。問︰用徒幾何？
術曰：以積尺為實，程功尺數為法，實如法而一，即用徒人數。
荅曰： a(=1778/111)人 。
"""

#----- content starts here -----
"""
Suppose there is a dike with the following dimensions:
The width at the bottom is 2 zhang, the width at the top is 8 chi, the height is 4 chi, and the length is 12 zhang and 7 chi.
Question: what is the volume?

Answer: 7112 cubic chi.

Additionally, if the winter work rate is 444 cubic chi per person, how many workers are required?

The procedure says: Take the volume in cubic chi as the dividend, and the work rate in cubic chi as the divisor.
Divide the dividend by the divisor, obtaining the number of workers.

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
# Volume formula for a trapezoidal prism: (1/2) * (bottom width + top width) * height * length
積 = Fraction(1, 2) * (隄下廣 + 上廣) * 高 * 袤  # 7112 cubic chi

# 冬程人功四百四十四尺
程功 = 444

# 用徒幾何？
# Divide the total volume by the work rate
a = Fraction(積, 程功)  # 1778/111 workers#----- content ends here -----

"""
"""
