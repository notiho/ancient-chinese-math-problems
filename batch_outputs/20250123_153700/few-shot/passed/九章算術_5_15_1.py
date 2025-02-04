"""
今有圓亭，下周三丈，上周二丈，高一丈。問︰積幾何？
術曰：上、下周相乘，又各自乘，并之，以高乘之，三十六而一。
荅曰： a尺 。
"""

"""
Suppose there is a circular pavilion with a lower circumference of 3 zhang, an upper circumference of 2 zhang, and a height of 1 zhang.
Question: what is the volume?

The procedure says: Multiply the upper and lower circumferences with each other. Then, multiply each of them by itself. Add these together. Multiply the result by the height. Divide by 36 to obtain the volume.

Answer: *a* chi.
"""

# 下周三丈
下周 = 3 * 10  # Convert zhang to chi (1 zhang = 10 chi)

# 上周二丈
上周 = 2 * 10  # Convert zhang to chi

# 高一丈
高 = 1 * 10  # Convert zhang to chi

# 上、下周相乘
上下相乘 = 上周 * 下周

# 又各自乘
下周自乘 = 下周 * 下周
上周自乘 = 上周 * 上周

# 并之
總和 = 上下相乘 + 下周自乘 + 上周自乘

# 以高乘之
積 = 總和 * 高

# 三十六而一
a = Fraction(積, 36)  # Volume in chi³
"""
"""
