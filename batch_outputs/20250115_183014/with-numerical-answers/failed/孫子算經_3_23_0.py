"""
今有竿，不知長短，度其影，得一丈五尺，別立一表，長一尺五寸，影得五寸。問：竿長幾何？
術曰：置竿影一丈五尺，以表長一尺五寸乘之，上十之，得二十二丈五尺，以表影五寸除之，即得。
答曰： a(=9/2)丈 。
"""

"""
Suppose there is a pole, but its length is unknown. Measure its shadow, obtaining 1 zhang and 5 chi. 
Separately set up a post, with a length of 1 chi and 5 cun, and its shadow is 5 cun.
Question: how long is the pole?

The procedure says: Place the shadow of the pole, 1 zhang and 5 chi, and multiply it by the length of the post, 1 chi and 5 cun.
Raise it by 10, obtaining 22 zhang and 5 chi.
Divide it by the shadow of the post, 5 cun, and the result is obtained.

The answer says: *a*(=9/2) zhang.
"""

# 竿影一丈五尺
竿影 = 1 + Fraction(5, 10)  # Convert to zhang (1 zhang = 10 chi)

# 表長一尺五寸
表長 = Fraction(1, 10) + Fraction(5, 100)  # Convert to zhang (1 chi = 1/10 zhang, 1 cun = 1/100 zhang)

# 表影五寸
表影 = Fraction(5, 100)  # Convert to zhang (1 cun = 1/100 zhang)

# 以表長乘竿影
實 = 竿影 * 表長

# 上十之
實 *= 10

# 以表影除之，即得
a = Fraction(實, 表影)  # 9/2 zhang
"""
Variable 'a' has wrong value. Expected: 9/2, Actual: 45"""
