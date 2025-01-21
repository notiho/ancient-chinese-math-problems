#今有穿地積一萬尺。問︰為堅、壤各幾何？
#荅曰：為堅 a尺 。為壤 b尺 。

"""
Suppose there is 10000 chi of dug out earth.
Question: how much solid earth and loose earth does it make respectively?

Answer: it makes *a* chi of solid earth, and it makes *b* chi of loose earth.
"""

# 穿地積一萬尺
穿地 = 10000

# solid earth is excavated earth times 5 divided by 4
a = 5 * 穿地 / 4

# loose earth is excavated earth times 3 divided by 4
b = 3 * 穿地 / 4
