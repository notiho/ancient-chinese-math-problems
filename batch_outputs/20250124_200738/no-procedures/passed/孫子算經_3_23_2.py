"""
今有竿，不知長短，度其影，得一丈五尺，別立一表，長一尺五寸，影得五寸。問：竿長幾何？
答曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is a pole of unknown length. Its shadow measures 1 zhang and 5 chi. Separately, a post is erected, which is 1 chi and 5 cun tall, and its shadow measures 5 cun.
Question: how long is the pole?

Answer: the pole is *a* zhang.
"""

# Shadow of the pole
竿影 = 1 + Fraction(5, 10)  # 1 zhang 5 chi = 1.5 zhang

# Height of the post
表高 = Fraction(1, 10) + Fraction(5, 100)  # 1 chi 5 cun = 0.15 zhang

# Shadow of the post
表影 = Fraction(5, 100)  # 5 cun = 0.05 zhang

# The ratio of height to shadow is the same for both the pole and the post
竿高 = (竿影 / 表影) * 表高

# Convert the pole's height into zhang
a = 竿高

# Output the result
a#----- content ends here -----

"""
"""
