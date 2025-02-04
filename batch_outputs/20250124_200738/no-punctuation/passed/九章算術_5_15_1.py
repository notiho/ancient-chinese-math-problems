"""
今有圓亭下周三丈上周二丈高一丈問積幾何
術曰上下周相乘又各自乘并之以高乘之三十六而一
荅曰 a尺 
"""

#----- content starts here -----
"""
Suppose there is a circular pavilion with a bottom circumference of 3 zhang, a top circumference of 2 zhang, and a height of 1 zhang.
Question: what is the volume?

The procedure says: Multiply the top and bottom circumferences with each other.
Then, multiply each of them with itself and add the results.
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
上下周積 = 上周 * 下周

# 又各自乘并之
各自平方和 = (上周 ** 2) + (下周 ** 2)

# 并之以高乘之
體積積 = (上下周積 + 各自平方和) * 高

# 三十六而一
a = Fraction(體積積, 36)  # Volume in chi³#----- content ends here -----

"""
"""
