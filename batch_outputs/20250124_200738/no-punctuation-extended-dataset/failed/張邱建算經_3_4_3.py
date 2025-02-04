"""
今有圓圌上周一丈八尺下周二丈七尺高一丈四尺問受幾何
術曰上下周相乘又各自乘併以高乘之以三十六而一所得為實實如斛法而一得斛數
答曰 a斛
"""

#----- content starts here -----
"""
Suppose there is a circular cylinder with the upper circumference being 1 zhang 8 chi, the lower circumference being 2 zhang 7 chi, and the height being 1 zhang 4 chi.
Question: how much volume does it hold?

The procedure says: Multiply the upper and lower circumferences with each other. Then, multiply each of them by themselves, and add these results together. Multiply this sum by the height. Divide the result by 36, obtaining the intermediate result. Divide this intermediate result by the hu-divisor (10), obtaining the number of hu.

Answer: *a* hu.
"""

# 上周一丈八尺
上周 = 1 * 10 + 8  # Convert zhang and chi to chi

# 下周二丈七尺
下周 = 2 * 10 + 7  # Convert zhang and chi to chi

# 高一丈四尺
高 = 1 * 10 + 4  # Convert zhang and chi to chi

# 上下周相乘
上下周積 = 上周 * 下周

# 又各自乘
上周平方 = 上周 * 上周
下周平方 = 下周 * 下周

# 併
和 = 上下周積 + 上周平方 + 下周平方

# 以高乘之
實 = 和 * 高

# 以三十六而一
實 = Fraction(實, 36)

# 按斛法，斛法為10
斛法 = 10
a = Fraction(實, 斛法)  # 得斛數#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 3325/9, Actual: 1197/20"""
