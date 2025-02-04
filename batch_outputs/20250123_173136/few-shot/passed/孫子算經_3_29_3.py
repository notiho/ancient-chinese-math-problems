"""
今有雉、兔同籠，上有三十五頭，下有九十四足。問：雉、兔各幾何？
術曰：上置三十五頭，下置九十四足。半其足，得四十七，以少減多，再命之，上三除下三，上五除下五，下有一除上一，下有二除上二，即得。
答曰：雉 a ，兔 b 。
"""

"""
Suppose there are pheasants and rabbits in the same cage. There are 35 heads above and 94 feet below.
Question: how many pheasants and rabbits are there respectively?

The procedure says: Place 35 heads above and 94 feet below.
Halve the feet, obtaining 47. Subtract the smaller from the larger, and divide repeatedly:
- Divide the heads by 3 for pheasants,
- Divide the heads by 5 for rabbits,
- Subtract 1 from the remainder for pheasants,
- Subtract 2 from the remainder for rabbits.
This gives the answer.

Answer: there are *a* pheasants and *b* rabbits.
"""

# 上置三十五頭
頭 = 35

# 下置九十四足
足 = 94

# 半其足，得四十七
半足 = 足 // 2

# 以少減多，再命之
差 = 半足 - 頭

# 上三除下三 (pheasants have 2 legs)
雉 = 頭 - 差

# 上五除下五 (rabbits have 4 legs)
兔 = 差

# 答曰
a = 雉
b = 兔
"""
"""
