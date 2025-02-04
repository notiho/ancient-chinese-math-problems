"""
今有方物一束外周一市有三十二枚問積幾何
術曰重置二位左位減八餘加右位至盡虛加一即得
答曰 a枚 
"""

#----- content starts here -----
"""
Suppose there is a square bundle of objects with an outer perimeter of 1 shi (market unit) and 32 pieces.
Question: what is the total number of pieces in the bundle?

The procedure says: Repeatedly place two positions.
Subtract 8 from the left position, and add the remainder to the right position until exhausted.
When exhausted, add 1 to the empty position, and the result is obtained.

Answer: *a* pieces.
"""

# 外周一市有三十二枚
外周 = 1 * 32  # Convert to total pieces

# Initialize variables
左位 = 外周 // 4  # Divide the perimeter into 4 sides (left position)
右位 = 0          # Start with 0 for the right position

# 重置二位
while 左位 >= 8:
    # 左位減八
    左位 -= 8
    # 餘加右位
    右位 += 左位

# 至盡虛加一
右位 += 1

# 即得
a = 右位#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 81, Actual: 1"""
