"""
今有隄下廣二丈上廣八尺高四尺袤一十二丈七尺問積幾何
荅曰七千一百一十二尺
冬程人功四百四十四尺問用徒幾何
術曰以積尺為實程功尺數為法實如法而一即用徒人數
荅曰 a人 
"""

"""
Suppose there is a dike with a bottom width of 2 zhang, a top width of 8 chi, a height of 4 chi, and a length of 12 zhang and 7 chi.
Question 1: What is the volume of the dike?
Answer: 7112 chi³.

Suppose the winter work rate is 444 chi³ per person.
Question 2: How many workers are needed?

The procedure says: Take the volume in chi³ as the dividend, and the work rate in chi³ as the divisor.
Divide the dividend by the divisor, and the result is the number of workers.

Answer: *a* workers.
"""

# 隄下廣二丈
下廣 = 2 * 10  # Convert zhang to chi

# 上廣八尺
上廣 = 8

# 高四尺
高 = 4

# 袤一十二丈七尺
袤 = 12 * 10 + 7  # Convert zhang and chi to chi

# 積幾何 (Volume calculation)
# Volume formula for a trapezoidal prism: V = (1/2 * (bottom_width + top_width) * height) * length
積 = Fraction(1, 2) * (下廣 + 上廣) * 高 * 袤

# Winter work rate: 444 chi³ per person
程功 = 444

# 用徒幾何 (Number of workers calculation)
a = Fraction(積, 程功)  # Number of workers needed
"""
"""
