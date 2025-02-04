"""
今有方物一束外周一市有三十二枚問積幾何
術曰重置二位左位減八餘加右位至盡虛加一即得
答曰 a枚 
"""

"""
Suppose there is a square bundle of items with an outer perimeter of 1 chi, and it contains 32 items.
Question: what is the total number of items in the bundle?

The procedure says: Double the number and place it in two positions.
Subtract 8 from the left position, and add the remainder to the right position until nothing remains.
Add 1 to the empty position, and the result is obtained.

Answer: *a* items.
"""

# 外周一市有三十二枚
外周 = 32

# 重置二位
左位 = 外周
右位 = 外周

# 左位減八，餘加右位，至盡
while 左位 >= 8:
    左位 -= 8
    右位 += 左位

# 虛加一
a = 右位 + 1
"""
"""
