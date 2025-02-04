"""
今有雉、兔同籠，上有三十五頭，下有九十四足。問：雉、兔各幾何？
術曰：上置三十五頭，下置九十四足。半其足，得四十七，以少減多，再命之，上三除下三，上五除下五，下有一除上一，下有二除上二，即得。
答曰：雉 a ，兔 b 。
"""

#----- content starts here -----
"""
Suppose there are pheasants and rabbits in the same cage. 
There are 35 heads in total and 94 feet in total.
Question: how many pheasants and rabbits are there respectively?

The procedure says: Place the 35 heads above and the 94 feet below. 
Halve the number of feet, obtaining 47. 
Subtract the smaller number (heads) from the larger number (halved feet). 
Divide the result by 2 to determine the number of rabbits. 
Subtract the number of rabbits from the total number of heads to determine the number of pheasants.

Answer: there are *a* pheasants and *b* rabbits.
"""

# 上有三十五頭
heads = 35

# 下有九十四足
feet = 94

# 半其足，得四十七
half_feet = feet // 2

# 以少減多，再命之
difference = half_feet - heads

# Divide the difference by 2 to find the number of rabbits
b = difference

# Subtract the number of rabbits from the total number of heads to find the number of pheasants
a = heads - b

a, b  # Output the number of pheasants and rabbits#----- content ends here -----

"""
"""
