"""
今有雉、兔同籠，上有三十五頭，下有九十四足。問：雉、兔各幾何？
術曰：上置三十五頭，下置九十四足。半其足，得四十七，以少減多，再命之，上三除下三，上五除下五，下有一除上一，下有二除上二，即得。
答曰：雉 a(=23) ，兔 b(=12) 。
"""

#----- content starts here -----
"""
Suppose there are pheasants and rabbits in the same cage. 
There are 35 heads above and 94 feet below.
Question: how many pheasants and rabbits are there respectively?

The procedure says: Place 35 heads above and 94 feet below.
Halve the feet, obtaining 47.
Subtract the smaller from the larger, and repeat the process.
Divide the remainder by 3 for the pheasants and by 5 for the rabbits.
When the remainder is 1, divide by 1 for the pheasants.
When the remainder is 2, divide by 2 for the rabbits.
This gives the answer.

Answer: There are *a*(=23) pheasants and *b*(=12) rabbits.
"""

# 上置三十五頭
頭 = 35

# 下置九十四足
足 = 94

# 半其足，得四十七
半足 = 足 // 2  # 47

# 以少減多，再命之
兔 = 半足 - 頭  # Rabbits = 47 - 35 = 12
雉 = 頭 - 兔    # Pheasants = 35 - 12 = 23

# 答曰
a = 雉  # 23
b = 兔  # 12#----- content ends here -----

"""
"""
