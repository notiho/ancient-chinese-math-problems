"""
今有木，不知長短，引繩度之，餘繩四尺五寸；屈繩量之，不足一尺。問：幾何？
術曰：置餘繩四尺五寸，加不足一尺，共五尺五寸，倍之，得一丈一尺，減四尺五寸，即得。
答曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a piece of wood of unknown length. When measured with a stretched rope, the rope exceeds the wood by 4 chi and 5 cun. When the rope is folded in half and used to measure, it falls short by 1 chi.
Question: what is the length of the wood?

The procedure says: Place the excess rope of 4 chi and 5 cun, add the shortfall of 1 chi, obtaining 5 chi and 5 cun. Double this, obtaining 1 zhang and 1 chi. Subtract 4 chi and 5 cun, and the result is the length of the wood.

Answer: *a* chi.
"""

from fractions import Fraction

# Define units in chi (1 chi = 10 cun)
餘繩 = 4 + Fraction(5, 10)  # 4 chi 5 cun
不足 = 1  # 1 chi

# Add the excess and shortfall
總長 = 餘繩 + 不足  # 4 chi 5 cun + 1 chi = 5 chi 5 cun

# Double the total
倍長 = 2 * 總長  # 2 * 5 chi 5 cun = 1 zhang 1 chi = 11 chi

# Subtract the excess rope
木長 = 倍長 - 餘繩  # 11 chi - 4 chi 5 cun

# Final result
a = 木長
a#----- content ends here -----

"""
"""
