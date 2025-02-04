"""
今有方物一束外周，一市有三十二枚。問：積幾何？
術曰：重置二位左位減八餘加右位，至盡虛加一，即得。
答曰： a(=81)枚 。
"""

"""
Suppose there is a square bundle of items, with an outer perimeter of one shu (束). 
One side of the square contains 32 items. 
Question: how many items are in total?

The procedure says: 
Rearrange the number into two positions. Subtract 8 from the left position, and add the remainder to the right position. 
Continue until the left position is exhausted, then add 1 to the result. This gives the total.

Answer: *a*(=81) items.
"""

# 一市有三十二枚
一市 = 32

# 重置二位
左位 = 一市 // 10  # Tens place
右位 = 一市 % 10   # Units place

# 左位減八餘加右位
左位 -= 8
右位 += 左位

# 至盡虛加一
a = 右位 + 1  # 81
"""
Variable 'a' has wrong value. Expected: 81, Actual: -2"""
