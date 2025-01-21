"""
今有圓亭下周三丈上周二丈高一丈問積幾何
術曰上下周相乘又各自乘并之以高乘之三十六而一
荅曰 a尺 
"""

"""
Suppose there is a circular pavilion with a lower circumference of 3 zhang, an upper circumference of 2 zhang, and a height of 1 zhang.
Question: what is the volume?

The procedure says: Multiply the upper and lower circumferences with each other, then multiply each of them by itself.
Add these results together, then multiply by the height.
Finally, divide by 36 to obtain the volume.

Answer: *a* chi³.
"""

# 下周三丈
下周 = 3 * 10  # Convert zhang to chi

# 上周二丈
上周 = 2 * 10  # Convert zhang to chi

# 高一丈
高 = 1 * 10  # Convert zhang to chi

# 上下周相乘
上下周積 = 上周 * 下周

# 又各自乘
下周平方 = 下周 * 下周
上周平方 = 上周 * 上周

# 并之
和 = 上下周積 + 下周平方 + 上周平方

# 以高乘之
積 = 和 * 高

# 三十六而一
a = Fraction(積, 36)  # Volume in chi³
"""
"""
