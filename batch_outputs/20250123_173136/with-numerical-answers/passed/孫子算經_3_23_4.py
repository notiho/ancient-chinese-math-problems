"""
今有竿，不知長短，度其影，得一丈五尺，別立一表，長一尺五寸，影得五寸。問：竿長幾何？
術曰：置竿影一丈五尺，以表長一尺五寸乘之，上十之，得二十二丈五尺，以表影五寸除之，即得。
答曰： a(=9/2)丈 。
"""

"""
Suppose there is a pole of unknown length. Measuring its shadow, it is found to be 1 zhang 5 chi.
Separately, a post is erected, with a length of 1 chi 5 cun, and its shadow is found to be 5 cun.
Question: how long is the pole?

The procedure says: Place the shadow of the pole, 1 zhang 5 chi, and multiply it by the length of the post, 1 chi 5 cun.
Convert to chi (multiply by 10). The result is 22 zhang 5 chi.
Divide by the shadow of the post, 5 cun, to obtain the length of the pole.

The answer says: *a*(=9/2) zhang.
"""

# 竿影一丈五尺
竿影 = 1 * 10 + 5  # Convert to chi (1 zhang = 10 chi)

# 表長一尺五寸
表長 = 1 + Fraction(5, 10)  # Convert to chi (1 chi = 10 cun)

# 表影五寸
表影 = Fraction(5, 10)  # Convert to chi

# 以表長乘竿影，上十之
實 = 竿影 * 表長

# 以表影除之，即得
a = Fraction(實, 表影) / 10  # Convert back to zhang (divide by 10)

# a = 9/2 zhang
"""
"""
