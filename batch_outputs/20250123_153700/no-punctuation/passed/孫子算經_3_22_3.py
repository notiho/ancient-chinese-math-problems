"""
今有方物一束外周一市有三十二枚問積幾何
術曰重置二位左位減八餘加右位至盡虛加一即得
答曰 a枚 
"""

"""
Suppose there is a square bundle of objects, with an outer perimeter of 1 shi (market unit) and 32 pieces.
Question: what is the total number of pieces in the bundle?

The procedure says: Double the number and place it in two positions.
From the left position, subtract 8, and add the remainder to the right position.
Continue until the remainder is zero.
Finally, add 1 to the result, and this gives the total.

Answer: *a* pieces.
"""

# 外周一市有三十二枚
外周 = 32

# 重置二位 (double the number)
左位 = 外周
右位 = 外周

# 左位減八，餘加右位，至盡虛
while 左位 >= 8:
    左位 -= 8
    右位 += 左位

# 虛加一，即得
a = 右位 + 1
"""
"""
