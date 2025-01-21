"""
今有隄下廣二丈，上廣八尺，高四尺，袤一十二丈七尺。問︰積幾何？
荅曰：七千一百一十二尺。
冬程人功四百四十四尺。問︰用徒幾何？
術曰：以積尺為實，程功尺數為法，實如法而一，即用徒人數。
荅曰： a(=1778/111)人 。
"""

"""
Suppose there is an embankment with a bottom width of 2 zhang, a top width of 8 chi, a height of 4 chi, and a length of 12 zhang 7 chi.
Question: what is the volume?

Answer: 7112 cubic chi.

For winter labor, one person can complete 444 cubic chi of work.
Question: how many laborers are required?

The procedure says: Take the volume in cubic chi as the dividend, and the amount of work one person can complete as the divisor. Divide the dividend by the divisor, and the result is the number of laborers required.

Answer: *a*(=1778/111) people.
"""

# 隄下廣二丈
下廣 = 2 * 10  # Convert zhang to chi

# 上廣八尺
上廣 = 8

# 高四尺
高 = 4

# 袤一十二丈七尺
袤 = 12 * 10 + 7  # Convert zhang and chi to chi

# 積幾何？
# Volume formula for a trapezoidal prism: (1/2) * (bottom width + top width) * height * length
積 = Fraction(1, 2) * (下廣 + 上廣) * 高 * 袤  # 7112 cubic chi

# 冬程人功四百四十四尺
程功 = 444

# 用徒幾何？
# Divide the volume by the work per person
a = Fraction(積, 程功)  # 1778/111 people
"""
"""
