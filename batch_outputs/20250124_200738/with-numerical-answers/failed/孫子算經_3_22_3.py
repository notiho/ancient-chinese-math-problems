"""
今有方物一束外周，一市有三十二枚。問：積幾何？
術曰：重置二位左位減八餘加右位，至盡虛加一，即得。
答曰： a(=81)枚 。
"""

#----- content starts here -----
"""
Suppose there is a square bundle of objects, with an external perimeter of one chi. 
Each side of the square contains 32 objects.
Question: how many objects are there in total?

The procedure says: Repeatedly place two digits. Subtract 8 from the left digit, and add the remainder to the right digit.
Continue until exhausted, then add 1 to the result. This gives the total.

Answer: *a*(=81) objects.
"""

# 一市有三十二枚
每邊物數 = 32

# 計算方形的總物數
# 方形的邊數為 4
邊數 = 4

# 積幾何
a = 每邊物數 * 邊數 # 81#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 81, Actual: 128"""
