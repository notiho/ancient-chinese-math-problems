"""
今有圓圌上周一丈八尺下周二丈七尺高一丈四尺問受幾何
術曰上下周相乘又各自乘併以高乘之以三十六而一所得為實實如斛法而一得斛數
答曰 a斛
"""

"""
Suppose there is a circular cylinder with an upper circumference of 1 zhang 8 chi, a lower circumference of 2 zhang 7 chi, and a height of 1 zhang 4 chi.
Question: how much volume does it hold?

The procedure says: Multiply the upper and lower circumferences with each other, and also multiply each of them by themselves.
Add these together, then multiply by the height.
Divide by 36, obtaining the result.
Divide the result by the hu divisor to obtain the number of hu.

Answer: *a* hu.
"""

from fractions import Fraction

# 上周一丈八尺 (convert to chi)
上周 = 1 * 10 + 8

# 下周二丈七尺 (convert to chi)
下周 = 2 * 10 + 7

# 高一丈四尺 (convert to chi)
高 = 1 * 10 + 4

# 上下周相乘
上下周相乘 = 上周 * 下周

# 又各自乘
上周自乘 = 上周 * 上周
下周自乘 = 下周 * 下周

# 併以高乘之
實 = (上下周相乘 + 上周自乘 + 下周自乘) * 高

# 以三十六而一
實 = Fraction(實, 36)

# 斛法 (1 hu = 10 cubic chi)
斛法 = 10

# 實如斛法而一，得斛數
a = Fraction(實, 斛法)
"""
Variable 'a' has wrong value. Expected: 3325/9, Actual: 1197/20"""
