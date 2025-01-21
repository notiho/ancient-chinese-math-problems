"""
今有竿，不知長短，度其影，得一丈五尺，別立一表，長一尺五寸，影得五寸。問：竿長幾何？
術曰：置竿影一丈五尺，以表長一尺五寸乘之，上十之，得二十二丈五尺，以表影五寸除之，即得。
答曰： a(=9/2)丈 。
"""

"""
Suppose there is a pole of unknown length. Measuring its shadow, it is found to be 1 zhang 5 chi.
Separately, a marker is set up, which is 1 chi 5 cun tall, and its shadow is found to be 5 cun.
Question: how long is the pole?

The procedure says: Place the shadow of the pole, 1 zhang 5 chi, and multiply it by the height of the marker, 1 chi 5 cun.
Convert to chi by multiplying by 10. This gives 22 zhang 5 chi.
Divide by the shadow of the marker, 5 cun, to obtain the length of the pole.

Answer: *a*(=9/2) zhang.
"""

# 竿影一丈五尺
竿影 = 1 * 10 + 5  # Convert to chi: 1 zhang = 10 chi

# 表長一尺五寸
表長 = 1 * 10 + 5 / 10  # Convert to chi: 1 chi = 10 cun

# 表影五寸
表影 = 5 / 10  # Convert to chi: 5 cun = 0.5 chi

# 以表長一尺五寸乘之，上十之
實 = 竿影 * 表長

# 得二十二丈五尺
實 = 實  # Already calculated in chi

# 以表影五寸除之，即得
竿長 = Fraction(實, 表影)

# Convert to zhang
a = Fraction(竿長, 10)  # 9/2 zhang
"""
Code error: both arguments should be Rational instances"""
