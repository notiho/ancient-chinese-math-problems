"""
今有竿，不知長短，度其影，得一丈五尺，別立一表，長一尺五寸，影得五寸。問：竿長幾何？
術曰：置竿影一丈五尺，以表長一尺五寸乘之，上十之，得二十二丈五尺，以表影五寸除之，即得。
答曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is a pole of unknown length. Measuring its shadow, it is found to be 1 zhang 5 chi.
Separately, a measuring stick is placed, which is 1 chi 5 cun long, and its shadow is found to be 5 cun.
Question: how long is the pole?

The procedure says: Place the shadow of the pole, 1 zhang 5 chi, and multiply it by the length of the measuring stick, 1 chi 5 cun.
Convert the result to chi (by multiplying by 10). Divide this by the shadow of the measuring stick, 5 cun, to obtain the length of the pole.

Answer: *a* zhang.
"""

from fractions import Fraction

# 竿影一丈五尺 (convert to chi: 1 zhang = 10 chi)
竿影 = 10 + 5  # 1 zhang 5 chi = 10 + 5 = 15 chi

# 表長一尺五寸 (convert to chi: 1 chi = 10 cun)
表長 = 1 + Fraction(5, 10)  # 1 chi 5 cun = 1 + 0.5 = 1.5 chi

# 表影五寸 (convert to chi: 1 chi = 10 cun)
表影 = Fraction(5, 10)  # 5 cun = 0.5 chi

# 置竿影，以表長乘之，上十之
實 = 竿影 * 表長 * 10  # Multiply and convert to chi

# 以表影除之
竿長 = 實 / 表影  # Divide by the shadow of the measuring stick

# Convert the result back to zhang
a = Fraction(竿長, 10)  # Convert chi to zhang (1 zhang = 10 chi)

a  # The length of the pole in zhang#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 9/2, Actual: 45"""
