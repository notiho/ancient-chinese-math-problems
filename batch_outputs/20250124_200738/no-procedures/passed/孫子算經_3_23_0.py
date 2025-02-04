"""
今有竿，不知長短，度其影，得一丈五尺，別立一表，長一尺五寸，影得五寸。問：竿長幾何？
答曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is a pole of unknown length. Measuring its shadow, it is found to be 1 zhang 5 chi (15 chi).  
Separately, a post is erected, which is 1 chi 5 cun (1.5 chi) tall, and its shadow is 5 cun (0.5 chi).  
Question: how long is the pole?

Answer: the pole is *a* zhang.
"""

# Shadow of the pole
竿影 = 15  # in chi (1 zhang = 10 chi)

# Height of the post
表高 = Fraction(15, 10)  # 1 chi 5 cun = 1.5 chi

# Shadow of the post
表影 = Fraction(5, 10)  # 5 cun = 0.5 chi

# Using proportionality: 竿高 / 表高 = 竿影 / 表影
竿高 = (竿影 / 表影) * 表高

# Convert the pole's height into zhang
a = 竿高 / 10  # 1 zhang = 10 chi

a  # The length of the pole in zhang#----- content ends here -----

"""
"""
