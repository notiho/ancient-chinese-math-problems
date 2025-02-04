"""
今有雉、兔同籠，上有三十五頭，下有九十四足。問：雉、兔各幾何？
術曰：上置三十五頭，下置九十四足。半其足，得四十七，以少減多，再命之，上三除下三，上五除下五，下有一除上一，下有二除上二，即得。
答曰：雉 a(=23) ，兔 b(=12) 。
"""

"""
Suppose there are pheasants and rabbits in the same cage. 
There are 35 heads above and 94 feet below.
Question: how many pheasants and rabbits are there respectively?

The procedure says: Place 35 heads above and 94 feet below.
Halve the feet, obtaining 47.
Subtract the smaller from the larger, and repeatedly command it.
Divide the upper by 3 and the lower by 3.
Divide the upper by 5 and the lower by 5.
If there is 1 below, divide the upper by 1.
If there are 2 below, divide the upper by 2.
This gives the answer.

Answer: There are *a*(=23) pheasants and *b*(=12) rabbits.
"""

# 上置三十五頭
頭 = 35

# 下置九十四足
足 = 94

# 半其足，得四十七
半足 = 足 // 2

# 雉有2足，兔有4足
雉足 = 2
兔足 = 4

# 以少減多，再命之
兔 = 半足 - 頭  # 47 - 35 = 12
雉 = 頭 - 兔    # 35 - 12 = 23

a = 雉  # 23
b = 兔  # 12
"""
"""
