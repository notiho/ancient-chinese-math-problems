"""
今有圓圌上周一丈八尺下周二丈七尺高一丈四尺問受幾何
術曰上下周相乘又各自乘併以高乘之以三十六而一所得為實實如斛法而一得斛數
答曰 a斛
"""

"""
Suppose there is a cylindrical container with an upper circumference of 1 zhang 8 chi, a lower circumference of 2 zhang 7 chi, and a height of 1 zhang 4 chi.
Question: how much volume does it hold?

The procedure says: Multiply the upper and lower circumferences with each other. Then multiply each circumference by itself, and add these together. Multiply the result by the height. Divide by 36 to obtain the intermediate result. Divide this result by the volume unit (1 hu) to obtain the number of hu.

Answer: it holds *a* hu.
"""

from fractions import Fraction

# 上周一丈八尺 (convert to chi)
上周 = 1 * 10 + 8  # 1 zhang = 10 chi

# 下周二丈七尺 (convert to chi)
下周 = 2 * 10 + 7  # 1 zhang = 10 chi

# 高一丈四尺 (convert to chi)
高 = 1 * 10 + 4  # 1 zhang = 10 chi

# 術曰：上下周相乘
上下周相乘 = 上周 * 下周

# 又各自乘
上周自乘 = 上周 * 上周
下周自乘 = 下周 * 下周

# 併以高乘之
實 = (上下周相乘 + 上周自乘 + 下周自乘) * 高

# 以三十六而一
實 = Fraction(實, 36)

# 實如斛法而一 (1 hu = 1 unit)
a = 實  # The result is in hu
"""
Variable 'a' has wrong value. Expected: 3325/9, Actual: 1197/2"""
