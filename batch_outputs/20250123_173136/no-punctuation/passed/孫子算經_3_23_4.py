"""
今有竿不知長短度其影得一丈五尺別立一表長一尺五寸影得五寸問竿長幾何
術曰置竿影一丈五尺以表長一尺五寸乘之上十之得二十二丈五尺以表影五寸除之即得
答曰 a丈 
"""

"""
Suppose there is a pole of unknown length. Its shadow measures 1 zhang and 5 chi.
Separately, a post is erected with a length of 1 chi and 5 cun, and its shadow measures 5 cun.
Question: how long is the pole?

The procedure says: Place the shadow of the pole, 1 zhang and 5 chi, and multiply it by the length of the post, 1 chi and 5 cun.
Convert the result into chi (by multiplying by 10), obtaining 22 zhang and 5 chi.
Divide this by the shadow of the post, 5 cun, to obtain the length of the pole.

The answer says: *a* zhang.
"""

# 竿影一丈五尺
竿影 = 1 * 10 + 5  # Convert to chi (1 zhang = 10 chi)

# 表長一尺五寸
表長 = 1 + Fraction(5, 10)  # Convert to chi (1 chi = 10 cun)

# 表影五寸
表影 = Fraction(5, 10)  # Convert to chi

# 以竿影乘表長
實 = 竿影 * 表長

# 上十之 (convert to chi, already in chi so no further action needed)
# 得二十二丈五尺 (calculation happens here)
# 以表影除之，即得
竿長 = 實 / 表影

# Convert result back to zhang
a = Fraction(竿長, 10)  # Convert chi to zhang

a
"""
"""
