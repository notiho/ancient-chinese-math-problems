"""
今有木，不知長短，引繩度之，餘繩四尺五寸；屈繩量之，不足一尺。問：幾何？
術曰：置餘繩四尺五寸，加不足一尺，共五尺五寸，倍之，得一丈一尺，減四尺五寸，即得。
答曰： a尺 。
"""

"""
Suppose there is a piece of wood of unknown length.
When measured with a stretched rope, the rope exceeds the wood by 4 chi and 5 cun.
When measured with the rope folded in half, the rope falls short by 1 chi.
Question: what is the length of the wood?

The procedure says: Place the excess rope of 4 chi and 5 cun, add the shortfall of 1 chi, obtaining 5 chi and 5 cun.
Double this, obtaining 1 zhang and 1 chi.
Subtract 4 chi and 5 cun, and the result is the length of the wood.

Answer: *a* chi.
"""

# 餘繩四尺五寸
餘繩 = 4 + Fraction(5, 10)  # 5寸 = 5/10尺

# 不足一尺
不足 = 1

# 加不足一尺，共五尺五寸
總長 = 餘繩 + 不足  # 4尺5寸 + 1尺 = 5尺5寸

# 倍之，得一丈一尺
倍長 = 2 * 總長  # 2 * 5尺5寸 = 11尺 = 1丈1尺

# 減四尺五寸，即得
a = 倍長 - 餘繩  # 11尺 - 4尺5寸 = 6尺5寸

a
"""
"""
