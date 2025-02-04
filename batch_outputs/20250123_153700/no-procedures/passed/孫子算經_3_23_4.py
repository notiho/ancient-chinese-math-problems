"""
今有竿，不知長短，度其影，得一丈五尺，別立一表，長一尺五寸，影得五寸。問：竿長幾何？
答曰： a丈 。
"""

"""
Suppose there is a pole of unknown length. Measuring its shadow, the shadow is 1 zhang and 5 chi (15 chi).
Separately, a post is set up with a height of 1 chi and 5 cun (1.5 chi), and its shadow is 5 cun (0.5 chi).
Question: how long is the pole?

Answer: the pole is *a* zhang.
"""

# Shadow of the pole
竿影 = 15  # in chi (1 zhang = 10 chi)

# Height of the post
表高 = Fraction(15, 10)  # 1 chi 5 cun = 1.5 chi

# Shadow of the post
表影 = Fraction(5, 10)  # 5 cun = 0.5 chi

# The ratio of height to shadow is the same for both the pole and the post
竿高 = 竿影 * (表高 / 表影)

# Convert the pole's height to zhang
a = 竿高 / 10  # 1 zhang = 10 chi

# Result
a
"""
"""
