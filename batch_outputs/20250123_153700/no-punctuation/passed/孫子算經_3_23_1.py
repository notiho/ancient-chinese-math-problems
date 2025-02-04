"""
今有竿不知長短度其影得一丈五尺別立一表長一尺五寸影得五寸問竿長幾何
術曰置竿影一丈五尺以表長一尺五寸乘之上十之得二十二丈五尺以表影五寸除之即得
答曰 a丈 
"""

"""
Suppose there is a pole of unknown length. Its shadow measures 1 zhang 5 chi.
Separately, a post of 1 chi 5 cun is erected, and its shadow measures 5 cun.
Question: how long is the pole?

The procedure says: Place the shadow of the pole, 1 zhang 5 chi, and multiply it by the length of the post, 1 chi 5 cun.
Convert to chi, obtaining 22 chi 5 cun.
Divide by the shadow of the post, 5 cun, to obtain the length of the pole.

Answer: *a* zhang.
"""

# 竿影一丈五尺
竿影 = 1 * 10 + 5  # Convert to chi (1 zhang = 10 chi)

# 表長一尺五寸
表長 = 1 + Fraction(5, 10)  # Convert to chi (1 chi = 10 cun)

# 表影五寸
表影 = Fraction(5, 10)  # Convert to chi

# 以竿影乘表長
實 = 竿影 * 表長

# 以表影除之，即得竿長
竿長 = 實 / 表影

# Convert to zhang
a = Fraction(竿長, 10)  # Convert chi to zhang (10 chi = 1 zhang)
"""
"""
