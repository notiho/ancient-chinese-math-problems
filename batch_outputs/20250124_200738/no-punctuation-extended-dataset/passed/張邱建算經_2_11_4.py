"""
今有築圓堢壔周九丈六尺髙一丈三尺問用壤土㡬何
術曰周自相乗以髙乗之又以五乗為實以三乗十二為法實如法而一
答曰 a尺
"""

#----- content starts here -----
"""
Suppose there is a circular embankment with a circumference of 9 zhang and 6 chi, and a height of 1 zhang and 3 chi.
Question: how much loose earth is used?

The procedure says: Multiply the circumference by itself, then multiply it by the height, and then multiply it by 5 to get the dividend.
Take 3 multiplied by 12 as the divisor.
Divide the dividend by the divisor to get the result.

Answer: *a* chi.
"""

# 周九丈六尺
周 = 9 * 10 + 6  # Convert zhang to chi (1 zhang = 10 chi)

# 高一丈三尺
高 = 1 * 10 + 3  # Convert zhang to chi (1 zhang = 10 chi)

# 周自相乘
周平方 = 周 * 周

# 以高乘之
積 = 周平方 * 高

# 又以五乘為實
實 = 5 * 積

# 以三乘十二為法
法 = 3 * 12

# 實如法而一
a = Fraction(實, 法)  # Result in chi#----- content ends here -----

"""
"""
