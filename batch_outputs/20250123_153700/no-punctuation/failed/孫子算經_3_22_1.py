"""
今有方物一束外周一市有三十二枚問積幾何
術曰重置二位左位減八餘加右位至盡虛加一即得
答曰 a枚 
"""

"""
Suppose there is a square bundle of items with an outer perimeter of 1 chi, containing 32 items.
Question: what is the total number of items in the bundle?

The procedure says: Repeatedly place two positions.
Subtract 8 from the left position, and add the remainder to the right position.
Continue until the left position is empty, then add 1 to the result.
This gives the total.

Answer: *a* items.
"""

# 外周一市有三十二枚
外周 = 32

# Initialize variables
左位 = 外周
右位 = 0

# 重置二位，左位減八，餘加右位，至盡虛加一即得
while 左位 > 0:
    餘 = 左位 % 8
    左位 = 左位 // 8
    右位 += 餘

a = 右位 + 1
"""
Variable 'a' has wrong value. Expected: 81, Actual: 5"""
