"""
今有圓困高一丈三尺三寸少半寸容米二千斛問周幾何
術曰置米積尺以十二乘之令高而一所得開方除之即周
荅曰 a丈 
"""

#----- content starts here -----
"""
Suppose there is a circular granary with a height of 1 zhang, 3 chi, 3 cun, and slightly less than half a cun. It can hold 2000 hu of rice.
Question: what is the circumference?

The procedure says: Place the volume of rice in chi, multiply it by 12, and let the height be the divisor.
Take the square root of the result, and that is the circumference.

Answer: *a* zhang.
"""

# 容米二千斛
米積 = 2000  # in hu

# Convert 米積 to 尺 (1 hu = 10 cubic chi)
米積尺 = 米積 * 10

# 高一丈三尺三寸少半寸
高 = 1 * 10 + 3 + Fraction(3, 10) - Fraction(1, 20)  # Convert height to chi (1 zhang = 10 chi, 1 chi = 10 cun)

# 置米積尺以十二乘之
積乘十二 = 米積尺 * 12

# 令高而一 (divide by height)
積除高 = Fraction(積乘十二, 高)

# 所得開方 (take the square root)
周 = 積除高 ** Fraction(1, 2)

# Convert 周 to 丈 (1 zhang = 10 chi)
a = Fraction(周, 10)  # Convert chi to zhang#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
