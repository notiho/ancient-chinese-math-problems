"""
今有木，不知長短，引繩度之，餘繩四尺五寸；屈繩量之，不足一尺。問：幾何？
術曰：置餘繩四尺五寸，加不足一尺，共五尺五寸，倍之，得一丈一尺，減四尺五寸，即得。
答曰： a(=13/2)尺 。
"""

#----- content starts here -----
"""
Suppose there is a piece of wood of unknown length. When measured with a stretched rope, the rope exceeds the wood by 4 chi and 5 cun. 
When the rope is bent to measure, it falls short by 1 chi.
Question: what is the length of the wood?

The procedure says: Place the excess rope of 4 chi and 5 cun, add the shortfall of 1 chi, obtaining 5 chi and 5 cun. 
Double this, obtaining 1 zhang and 1 chi. Subtract 4 chi and 5 cun, and the result is the length of the wood.

Answer: *a*(=13/2) chi.
"""

# 餘繩四尺五寸
餘繩 = Fraction(4, 1) + Fraction(5, 10)  # 4 chi 5 cun = 4 + 5/10 chi

# 不足一尺
不足 = Fraction(1, 1)  # 1 chi

# 加不足一尺，共五尺五寸
總長 = 餘繩 + 不足  # 4 chi 5 cun + 1 chi = 5 chi 5 cun
總長 = 總長 * 2  # 倍之，得一丈一尺 = 2 * (5 chi 5 cun)

# 減四尺五寸，即得
a = 總長 - 餘繩  # 1 zhang 1 chi - 4 chi 5 cun = 13/2 chi or 6.5 chi#----- content ends here -----

"""
"""
