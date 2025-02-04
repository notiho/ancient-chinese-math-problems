"""
今有圓圌上周一丈八尺下周二丈七尺高一丈四尺問受幾何
術曰上下周相乘又各自乘併以高乘之以三十六而一所得為實實如斛法而一得斛數
答曰 a斛
"""

#----- content starts here -----
"""
Suppose there is a circular cylinder with the top circumference being 1 zhang 8 chi, the bottom circumference being 2 zhang 7 chi, and the height being 1 zhang 4 chi.
Question: how much volume does it hold?

The procedure says: Multiply the top and bottom circumferences with each other. Then, multiply each circumference by itself. Add these together, and multiply by the height. Divide by 36, obtaining the result. Use the hu-divisor to convert the result into hu.

Answer: it holds *a* hu.
"""

from fractions import Fraction

# 上周一丈八尺 (convert to chi: 1 zhang = 10 chi)
上周 = 1 * 10 + 8  # 18 chi

# 下周二丈七尺
下周 = 2 * 10 + 7  # 27 chi

# 高一丈四尺
高 = 1 * 10 + 4  # 14 chi

# 上下周相乘
上下周積 = 上周 * 下周

# 又各自乘
上周平方 = 上周 * 上周
下周平方 = 下周 * 下周

# 併以高乘之
實 = (上下周積 + 上周平方 + 下周平方) * 高

# 以三十六而一
實 = Fraction(實, 36)

# 按斛法 (1斛 = 1 unit here)
a = 實  # Volume in hu#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 3325/9, Actual: 1197/2"""
