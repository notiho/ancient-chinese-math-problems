"""
今有隄下廣二丈上廣八尺高四尺袤一十二丈七尺問積幾何
荅曰七千一百一十二尺
冬程人功四百四十四尺問用徒幾何
術曰以積尺為實程功尺數為法實如法而一即用徒人數
荅曰 a人 
"""

#----- content starts here -----
"""
Suppose there is a levee with a bottom width of 2 zhang, a top width of 8 chi, a height of 4 chi, and a length of 12 zhang and 7 chi.
Question 1: What is the total volume in cubic chi?
Answer: 7112 cubic chi.

Question 2: If the winter work rate is 444 cubic chi per person, how many workers are needed?
The procedure says: Take the total volume in cubic chi as the dividend, and the work rate in cubic chi per person as the divisor. Divide the dividend by the divisor, and the result is the number of workers needed.

Answer: *a* workers.
"""

# 隄下廣二丈
下廣 = 2 * 10  # Convert zhang to chi

# 上廣八尺
上廣 = 8

# 高四尺
高 = 4

# 袤一十二丈七尺
袤 = 12 * 10 + 7  # Convert zhang to chi and add chi

# 積幾何 (Volume calculation)
積 = Fraction((下廣 + 上廣) * 高 * 袤, 2)  # Trapezoidal prism formula

# 積尺 = 7112 (Given in the problem)
積尺 = 7112

# 冬程人功四百四十四尺
程功尺數 = 444

# 以積尺為實，程功尺數為法
實 = 積尺
法 = 程功尺數

# 實如法而一，即用徒人數
a = Fraction(實, 法)  # Number of workers needed#----- content ends here -----

"""
"""
