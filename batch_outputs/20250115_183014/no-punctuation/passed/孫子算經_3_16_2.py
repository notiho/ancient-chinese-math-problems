"""
今有木不知長短引繩度之餘繩四尺五寸屈繩量之不足一尺問幾何
術曰置餘繩四尺五寸加不足一尺共五尺五寸倍之得一丈一尺減四尺五寸即得
答曰 a尺 
"""

"""
Suppose there is a piece of wood of unknown length. When measured with a rope, there is an excess of 4 chi and 5 cun.
When the rope is folded and measured again, it is short by 1 chi.
Question: what is the length of the wood?

The procedure says: Place the excess rope of 4 chi and 5 cun, add the shortfall of 1 chi, obtaining 5 chi and 5 cun.
Double this, obtaining 1 zhang and 1 chi.
Subtract 4 chi and 5 cun, and the result is the length of the wood.

Answer: *a* chi.
"""

# 置餘繩四尺五寸
餘繩 = 4 + Fraction(5, 10)  # 4 chi and 5 cun (1 chi = 10 cun)

# 加不足一尺
不足 = 1
總長 = 餘繩 + 不足  # 共五尺五寸

# 倍之得一丈一尺
倍長 = 2 * 總長  # 1 zhang = 10 chi

# 減四尺五寸即得
a = 倍長 - 餘繩
"""
"""
