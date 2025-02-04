"""
今有圓亭下周三丈上周二丈高一丈問積幾何
術曰上下周相乘又各自乘并之以高乘之三十六而一
荅曰 a尺 
"""

#----- content starts here -----
"""
Suppose there is a circular pavilion with a lower circumference of 3 zhang, an upper circumference of 2 zhang, and a height of 1 zhang.
Question: what is the volume?

The procedure says: Multiply the upper and lower circumferences with each other.
Then, multiply each circumference by itself.
Add these results together.
Multiply the sum by the height.
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
上下相乘 = 上周 * 下周

# 又各自乘
下自乘 = 下周 * 下周
上自乘 = 上周 * 上周

# 并之
并之 = 上下相乘 + 下自乘 + 上自乘

# 以高乘之
乘高 = 并之 * 高

# 三十六而一
a = Fraction(乘高, 36)  # Volume in chi³#----- content ends here -----

"""
"""
