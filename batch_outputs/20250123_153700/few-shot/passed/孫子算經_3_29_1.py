"""
今有雉、兔同籠，上有三十五頭，下有九十四足。問：雉、兔各幾何？
術曰：上置三十五頭，下置九十四足。半其足，得四十七，以少減多，再命之，上三除下三，上五除下五，下有一除上一，下有二除上二，即得。
答曰：雉 a ，兔 b 。
"""

"""
Suppose there are pheasants and rabbits in the same cage. 
There are 35 heads above and 94 feet below.
Question: how many pheasants and rabbits are there respectively?

The procedure says: Place the 35 heads above and the 94 feet below.
Halve the feet, obtaining 47.
Subtract the smaller number from the larger, and divide repeatedly:
Divide the heads by 3 for the pheasants, and divide the heads by 5 for the rabbits.
Divide the remaining feet by 1 for pheasants, and divide the remaining feet by 2 for rabbits.
This gives the result.

Answer: pheasants *a*, rabbits *b*.
"""

# 上置三十五頭
頭 = 35

# 下置九十四足
足 = 94

# 半其足，得四十七
半足 = 足 // 2

# 以少減多，再命之
差 = 半足 - 頭

# 上三除下三
pheasants = 頭 - 差

# 上五除下五
rabbits = 差

# 答曰：雉 a ，兔 b
a = pheasants
b = rabbits
"""
"""
