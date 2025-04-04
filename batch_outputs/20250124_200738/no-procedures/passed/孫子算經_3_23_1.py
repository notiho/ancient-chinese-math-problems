"""
今有竿，不知長短，度其影，得一丈五尺，別立一表，長一尺五寸，影得五寸。問：竿長幾何？
答曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is a pole of unknown length. Measuring its shadow, it is found to be 1 zhang and 5 chi (15 chi). Separately, a post is erected with a height of 1 chi and 5 cun (1.5 chi), and its shadow is found to be 5 cun (0.5 chi).  
Question: how long is the pole?

Answer: the pole is *a* zhang.
"""

# Shadow of the pole
pole_shadow = 15  # in chi (1 zhang = 10 chi)

# Height and shadow of the post
post_height = 1 + Fraction(5, 10)  # 1 chi 5 cun = 1.5 chi
post_shadow = Fraction(5, 10)  # 5 cun = 0.5 chi

# The ratio of height to shadow is the same for both the pole and the post
pole_height = pole_shadow * (post_height / post_shadow)

# Convert pole height to zhang
a = pole_height / 10  # 1 zhang = 10 chi

# Final result
a#----- content ends here -----

"""
"""
